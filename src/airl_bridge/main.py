"""The FastAPI application: the Bridge's HTTP surface.

Seven ``GET`` endpoints (health, readiness, sources, search, detail, categories,
duplicates) and three ``POST`` endpoints (ingest, project, sync).

**The mutating endpoints require ``X-AIRL-Token`` and every request must carry a
known ``Host`` (finding M1, closed).** Loopback binding narrows the surface and
does not close it, for two distinct reasons that need two distinct fixes:

* a page in a browser can issue a **preflight-free** ``POST /v1/sync`` whose side
  effect runs even though the response is unreadable — so the mutating endpoints
  demand a **custom header**, which is not on the CORS safelist and therefore
  forces a preflight the attacker's page cannot satisfy;
* without ``Host`` validation a **DNS-rebinding** attacker is treated as
  same-origin and can read the whole registry over ``GET /v1/sources`` — so every
  request, read or write, is checked against ``allowed_hosts``.

**An unset ``AIRL_API_TOKEN`` refuses the mutating endpoints rather than opening
them.** Failing open on missing configuration is how a control becomes optional
in practice while remaining mandatory on paper.

``HealthResponse.zotero_write_enabled`` is still a constant, and it is now backed
by a behavioural test (finding **H3**): ``tests/test_zotero.py`` drives the whole
sync through a transport that raises on any method other than ``GET``.
"""
from __future__ import annotations

from contextlib import asynccontextmanager

import hmac

from fastapi import Depends, FastAPI, Header, HTTPException, Query, Request
from fastapi.responses import JSONResponse

from . import __version__
from .config import Settings
from .catalog import duplicate_source_groups, normalized_title_key, source_category
from .database import Database
from .models import (
    CategorySummary,
    DuplicateGroup,
    HealthResponse,
    IngestResult,
    ProjectionResult,
    SourceRecord,
    SyncResult,
)
from .obsidian import ObsidianProjector, ProjectionError
from .service import BridgeService
from .zotero import ZoteroClient, ZoteroUnavailable


def create_app(settings: Settings | None = None) -> FastAPI:
    resolved_settings = settings or Settings.from_env()
    database = Database(resolved_settings.database_path)
    zotero = ZoteroClient(resolved_settings)
    projector = ObsidianProjector(resolved_settings)
    service = BridgeService(database, zotero, projector)

    @asynccontextmanager
    async def lifespan(_: FastAPI):
        database.initialize()
        yield

    app = FastAPI(
        title="AIRL Bridge API",
        version=__version__,
        description=(
            "Local, read-only Zotero intake into an AIRL SQLite registry with "
            "generated Obsidian projections. This service never writes to Zotero."
        ),
        lifespan=lifespan,
    )
    app.state.settings = resolved_settings
    app.state.database = database
    app.state.zotero = zotero
    app.state.service = service

    @app.middleware("http")
    async def enforce_known_host(request: Request, call_next):
        """Reject a request whose Host header is not one we recognise.

        This is the DNS-rebinding defence, and it protects the READ endpoints as
        much as the writes: rebinding turns `http://attacker.example` into
        `127.0.0.1` after the page has loaded, and the browser then treats
        `GET /v1/sources` as same-origin. A token on the mutating endpoints does
        nothing about that, which is why this is a separate control.
        """
        host = (request.headers.get("host") or "").split(":")[0]
        allowed = {h.split(":")[0].strip("[]") for h in resolved_settings.allowed_hosts}
        if host.strip("[]") not in allowed:
            return JSONResponse(
                status_code=421,
                content={"detail": f"unrecognised Host {host!r}; "
                                   f"AIRL_ALLOWED_HOSTS governs this"},
            )
        return await call_next(request)

    def require_token(x_airl_token: str = Header(default="")) -> None:
        """Gate the three mutating endpoints — finding M1.

        A custom header is the whole mechanism. `X-AIRL-Token` is not on the
        CORS safelist, so a cross-site page cannot send it without a preflight,
        and the preflight fails. The secret comparison is constant-time because
        there is no reason for it not to be.
        """
        if not resolved_settings.api_token:
            raise HTTPException(
                status_code=503,
                detail="AIRL_API_TOKEN is not configured; the mutating "
                       "endpoints refuse rather than defaulting to open",
            )
        if not hmac.compare_digest(x_airl_token, resolved_settings.api_token):
            raise HTTPException(status_code=401, detail="invalid or missing X-AIRL-Token")

    @app.exception_handler(ZoteroUnavailable)
    async def zotero_unavailable(_: Request, exc: ZoteroUnavailable):
        return JSONResponse(status_code=503, content={"detail": str(exc)})

    @app.exception_handler(ProjectionError)
    async def projection_error(_: Request, exc: ProjectionError):
        return JSONResponse(status_code=422, content={"detail": str(exc)})

    @app.get("/health", response_model=HealthResponse)
    async def health() -> HealthResponse:
        return HealthResponse(
            status="ok",
            version=__version__,
            database=str(resolved_settings.database_path),
            zotero_base_url=resolved_settings.zotero_base_url,
            obsidian_vault=str(resolved_settings.obsidian_vault),
        )

    @app.get("/ready")
    async def ready() -> dict[str, object]:
        await zotero.ping()
        return {
            "status": "ready",
            "zotero": "reachable",
            "obsidian_vault": resolved_settings.obsidian_vault.is_dir(),
            "source_count": database.count_sources(),
        }

    @app.get("/v1/sources", response_model=list[SourceRecord])
    async def list_sources(
        limit: int = Query(default=100, ge=1, le=1000),
        offset: int = Query(default=0, ge=0),
    ) -> list[SourceRecord]:
        return database.list_sources(limit=limit, offset=offset)

    @app.get("/v1/sources/search", response_model=list[SourceRecord])
    async def search_sources(
        q: str = Query(min_length=2, max_length=200),
        limit: int = Query(default=25, ge=1, le=100),
    ) -> list[SourceRecord]:
        return database.search_sources(q, limit=limit)

    @app.get("/v1/sources/{airl_id}", response_model=SourceRecord)
    async def get_source(airl_id: str) -> SourceRecord:
        source = database.get_source(airl_id)
        if source is None:
            raise HTTPException(status_code=404, detail="source not found")
        return source

    @app.get("/v1/categories", response_model=list[CategorySummary])
    async def list_categories() -> list[CategorySummary]:
        return [
            CategorySummary(
                item_type=item_type,
                display_name=source_category(item_type),
                source_count=count,
            )
            for item_type, count in database.list_category_counts()
        ]

    @app.get("/v1/duplicates", response_model=list[DuplicateGroup])
    async def list_duplicates() -> list[DuplicateGroup]:
        groups = duplicate_source_groups(database.list_sources(limit=10_000))
        return [
            DuplicateGroup(
                normalized_title=normalized_title_key(group[0].title),
                source_count=len(group),
                sources=group,
            )
            for group in groups
        ]

    @app.post("/v1/ingest/zotero", response_model=IngestResult,
              dependencies=[Depends(require_token)])
    async def ingest_zotero(
        limit: int | None = Query(default=None, ge=1)
    ) -> IngestResult:
        """`limit` defaults to the whole library.

        It used to default to 100 and be capped at 100, so the ordinary call
        was a partial sync reported as `SUCCEEDED` (finding H1).
        """
        return await service.ingest_zotero(limit=limit)

    @app.post("/v1/project/obsidian", response_model=ProjectionResult,
              dependencies=[Depends(require_token)])
    async def project_obsidian(
        dry_run: bool = Query(default=False)
    ) -> ProjectionResult:
        return service.projector.project_sources(
            database.list_sources(limit=None), dry_run=dry_run)

    @app.post("/v1/sync", response_model=SyncResult,
              dependencies=[Depends(require_token)])
    async def sync(
        limit: int | None = Query(default=None, ge=1)
    ) -> SyncResult:
        return await service.sync(limit=limit)

    return app


app = create_app()

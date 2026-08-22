"""The FastAPI application: the Bridge's HTTP surface.

Seven ``GET`` endpoints (health, readiness, sources, search, detail, categories,
duplicates) and three ``POST`` endpoints (ingest, project, sync).

⚠️ **The mutating endpoints are unauthenticated (finding M1).** There is no
token, no CSRF protection and no ``TrustedHostMiddleware``. Binding to loopback
narrows but does not close this: a page in the browser can issue a preflight-free
``POST /v1/sync`` whose side effect still runs, and without ``Host`` validation a
DNS-rebinding attacker is treated as same-origin and can read the entire registry
over ``GET /v1/sources``.

The two low-cost fixes are a trusted-host middleware and an ``X-AIRL-Token``
header on the mutating endpoints — a custom header alone forces a preflight and
closes CSRF.

⚠️ **``HealthResponse.zotero_write_enabled`` is a constant**, not a measured
control (finding **H3**). It should either be removed or bound to a computed
value; as it stands it invites the reader to trust it.
"""
from __future__ import annotations

from contextlib import asynccontextmanager

from fastapi import FastAPI, HTTPException, Query, Request
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

    @app.post("/v1/ingest/zotero", response_model=IngestResult)
    async def ingest_zotero(
        limit: int = Query(default=100, ge=1, le=100)
    ) -> IngestResult:
        return await service.ingest_zotero(limit=limit)

    @app.post("/v1/project/obsidian", response_model=ProjectionResult)
    async def project_obsidian() -> ProjectionResult:
        return service.project_obsidian()

    @app.post("/v1/sync", response_model=SyncResult)
    async def sync(
        limit: int = Query(default=100, ge=1, le=100)
    ) -> SyncResult:
        return await service.sync(limit=limit)

    return app


app = create_app()

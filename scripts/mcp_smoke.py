"""Smoke check for the Hermes MCP surface — and it asserts.

Closes audit finding **M2**. The previous version of this script *reported*
``isError`` without checking it and contained no ``assert``, ``raise`` or
``sys.exit``: it printed JSON and exited 0 even with the Bridge completely down.
The README and the operations guide presented it as a verification step, so a
reader who did not read the output saw green.

What it now proves:

1. The server exposes **exactly** the five expected read-only tools — no more.
   This is the claim made in ``README.md`` and ``docs/OPERATIONS.md``; until now
   nothing checked it.
2. Neither ``bridge_status`` nor a source search returns an error.
3. The search returns at least one content block.

It exits non-zero on any failure, so it is usable as a CI step or a
pre-cutover gate.

Note the boundary of this check: it verifies what **this** MCP server exposes.
The `tools.include` restriction on the Hermes side lives in Hermes'
configuration, outside this repository, and is not verified here.

Usage:
    uv run python scripts/mcp_smoke.py [--query TERM]
"""
from __future__ import annotations

import argparse
import asyncio
import json
import sys
from pathlib import Path

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client


PROJECT_ROOT = Path(__file__).resolve().parents[1]
SERVER_COMMAND = PROJECT_ROOT / ".venv/bin/airl-bridge-mcp"

# The complete, closed set. A new tool appearing here is a boundary change and
# must fail this check until it is reviewed and this list is updated.
EXPECTED_TOOLS = [
    "bridge_status",
    "get_source",
    "list_categories",
    "list_possible_duplicates",
    "search_sources",
]


async def smoke(query: str) -> dict[str, object]:
    parameters = StdioServerParameters(command=str(SERVER_COMMAND))
    async with stdio_client(parameters) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            tools = await session.list_tools()
            status = await session.call_tool("bridge_status", {})
            search = await session.call_tool(
                "search_sources", {"query": query, "limit": 2}
            )

    names = sorted(tool.name for tool in tools.tools)
    failures: list[str] = []

    if names != EXPECTED_TOOLS:
        failures.append(
            f"tool set mismatch: expected {EXPECTED_TOOLS}, got {names}"
        )
    if status.isError:
        failures.append("bridge_status returned isError=True")
    if search.isError:
        failures.append("search_sources returned isError=True")
    if not search.content:
        failures.append("search_sources returned no content block")

    return {
        "tools": names,
        "expected_tools": EXPECTED_TOOLS,
        "status_is_error": status.isError,
        "search_is_error": search.isError,
        "search_content_blocks": len(search.content),
        "query": query,
        "failures": failures,
        "result": "PASS" if not failures else "FAIL",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--query",
        default="in",
        help="search term (minimum two characters); the default matches broadly so "
        "the check does not depend on any particular source existing",
    )
    args = parser.parse_args()

    report = asyncio.run(smoke(args.query))
    print(json.dumps(report, ensure_ascii=False, indent=2))

    if report["failures"]:
        for failure in report["failures"]:
            print(f"FAIL: {failure}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

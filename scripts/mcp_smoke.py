from __future__ import annotations

import asyncio
import json
from pathlib import Path

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client


PROJECT_ROOT = Path(__file__).resolve().parents[1]
SERVER_COMMAND = PROJECT_ROOT / ".venv/bin/airl-bridge-mcp"


async def smoke() -> None:
    parameters = StdioServerParameters(command=str(SERVER_COMMAND))
    async with stdio_client(parameters) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            tools = await session.list_tools()
            status = await session.call_tool("bridge_status", {})
            search = await session.call_tool(
                "search_sources", {"query": "LiDAR", "limit": 2}
            )
    report = {
        "tools": [tool.name for tool in tools.tools],
        "status_is_error": status.isError,
        "search_is_error": search.isError,
        "search_content_blocks": len(search.content),
    }
    print(json.dumps(report, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    asyncio.run(smoke())

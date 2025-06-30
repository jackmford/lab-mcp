import asyncio
import requests
from fastmcp import FastMCP, Client

# Create a server instance
mcp = FastMCP(name="vimtricks-mcp")

@mcp.tool
async def get_vimtrick() -> str:
    trick = requests.request("GET", "https://vimtricks.jackmitchellfordyce.com/daily-tip")

    return trick.json()["tip"]

async def main():
    async with Client(mcp) as client:
        await client.call_tool("get_vimtrick")

if __name__ == "__main__":
    asyncio.run(main())

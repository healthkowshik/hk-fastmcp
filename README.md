# hk-fastmcp

> The fast, Pythonic way to build MCP servers and clients.

## Setup

```bash
uv init
uv add "fastmcp[tasks]==3.0.0b2"
uv run fastmcp version

uv add "cyclopts>=5.0.0a1"
```

## MCP server

```bash
# Run the MCP server with the default stdio transport.
uv run fastmcp run server.py:mcp

# Run the MCP server with the HTTP transport.
uv run fastmcp run server.py:mcp --transport http --port 8000
```

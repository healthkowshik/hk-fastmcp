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
# Run the MCP server with the HTTP transport.
uv run fastmcp run server.py:mcp --transport http --port 8000
```


## MCP client

Using the following configuration, one can connect to the MCP client.

```json
{
    "mcpServers": {
        "hk-fastmcp": {
            "url": "http://127.0.0.1:8000/mcp"
        }
    }
}
```

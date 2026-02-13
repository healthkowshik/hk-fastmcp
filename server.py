import json
from datetime import UTC, datetime

from fastmcp import FastMCP, Context
from fastmcp.prompts import Message, PromptResult
from fastmcp.resources import ResourceContent, ResourceResult

mcp = FastMCP(
    name = "HK FastMCP",
    instructions = "MCP server from Health Kowshik to practice with FastMCP library.",
    website_url = "https://github.com/healthkowshik/hk-fastmcp",
    strict_input_validation = True,
    list_page_size = 10
)

# Tools
@mcp.tool()
def greet(name: str) -> dict:
    return { "greeting": f"Namaskar, {name}!" }

@mcp.tool()
def multiply(a: float, b: float) -> dict:
    """Multiplies two numbers together."""
    return { "a": a, "b": b, "product": a * b }

# Resources
@mcp.resource("data://config")
def get_config() -> ResourceResult:
    """Provides the application configuration."""
    return ResourceResult([ResourceContent({"theme": "dark", "version": "1.0"})])


@mcp.resource("resource://system-status")
async def get_system_status(ctx: Context) -> ResourceResult:
    """Provides system status information."""
    return ResourceResult([ResourceContent({"status": "operational", "request_id": ctx.request_id})])


@mcp.resource("resource://context")
async def get_context(ctx: Context) -> ResourceResult:
    """Returns all available context properties for the current request (request ID, client, session, transport, etc.)."""
    payload = {
        "request_timestamp": datetime.now(UTC).isoformat(),
        "transport": ctx.transport,
        "is_background_task": ctx.is_background_task,
        "task_id": ctx.task_id,
        "client_id": ctx.client_id,
        "lifespan_context": ctx.lifespan_context,
    }
    if ctx.request_context is not None:
        payload["request_id"] = ctx.request_id
        try:
            payload["session_id"] = ctx.session_id
        except RuntimeError:
            payload["session_id"] = None
    else:
        payload["request_id"] = None
        payload["session_id"] = None
    return ResourceResult([ResourceContent(payload)])

@mcp.resource("resource://{name}/details")
async def get_details(name: str, ctx: Context) -> ResourceResult:
    """Get details for a specific name."""
    return ResourceResult([ResourceContent({"name": name, "accessed_at": ctx.request_id})])

# Resource Templates
@mcp.resource("users://{user_id}/profile")
def get_user_profile(user_id: int) -> ResourceResult:
    """Retrieves a user's profile by ID."""
    return ResourceResult([ResourceContent({"id": user_id, "name": f"User {user_id}", "status": "active"})])


# Prompts
@mcp.prompt
def analyze_data(data_points: list[float]) -> PromptResult:
    """Creates a prompt asking for analysis of numerical data."""
    formatted_data = ", ".join(str(point) for point in data_points)
    return PromptResult(
        messages=[
            Message(f"Please analyze these data points: {formatted_data}"),
        ],
        description="Data analysis prompt",
    )


if __name__ == "__main__":
    mcp.run()

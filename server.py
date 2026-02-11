from fastmcp import FastMCP
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

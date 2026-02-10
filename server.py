import json

from fastmcp import FastMCP

mcp = FastMCP(
    name = "HK FastMCP",
    instructions = "MCP server from Health Kowshik to practice with FastMCP library.",
    website_url = "https://github.com/healthkowshik/hk-fastmcp",
    strict_input_validation = True,
    list_page_size = 10
)

# Tools
@mcp.tool(output_schema=None)
def greet(name: str) -> str:
    return f"Namaskar, {name}!"

@mcp.tool(output_schema=None)
def multiply(a: float, b: float) -> float:
    """Multiplies two numbers together."""
    return a * b


# Resources
@mcp.resource("data://config")
def get_config() -> str:
    """Provides the application configuration."""
    return json.dumps({"theme": "dark", "version": "1.0"})


# Resource Templates
@mcp.resource("users://{user_id}/profile")
def get_user_profile(user_id: int) -> str:
    """Retrieves a user's profile by ID."""
    return json.dumps({"id": user_id, "name": f"User {user_id}", "status": "active"})


# Prompts
@mcp.prompt
def analyze_data(data_points: list[float]) -> str:
    """Creates a prompt asking for analysis of numerical data."""
    formatted_data = ", ".join(str(point) for point in data_points)
    return f"Please analyze these data points: {formatted_data}"


if __name__ == "__main__":
    mcp.run()

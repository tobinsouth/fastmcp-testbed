# app/app.py
import logging
import os
from fastmcp import FastMCP
from fastmcp.server.auth.providers.workos import AuthKitProvider
from starlette.requests import Request
from starlette.responses import JSONResponse

logger = logging.getLogger("mcp")

# Deployment-friendly configuration via environment variables
host = os.getenv("HOST", "0.0.0.0")
port = int(os.getenv("PORT", "8080"))
base_url = os.getenv("BASE_URL", f"http://localhost:{port}")
authkit_domain = os.getenv(
    "AUTHKIT_DOMAIN",
    "https://interested-solitude-28-staging.authkit.app",
)
transport = os.getenv("TRANSPORT", "http")

mcp = FastMCP("Tobin's MCP", auth=AuthKitProvider(
    authkit_domain=authkit_domain,
    base_url=base_url
))

@mcp.tool
def greet(name: str) -> str:
    return f"Hello, {name}!"

mcp.run(transport=transport, host=host, port=port)
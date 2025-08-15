# app/app.py
import logging
import os
from fastmcp import FastMCP
from fastmcp.server.auth.providers.workos import AuthKitProvider
from starlette.requests import Request
from starlette.responses import JSONResponse

logger = logging.getLogger("mcp")

mcp = FastMCP("Tobin's MCP", auth=AuthKitProvider(
    authkit_domain="https://interested-solitude-28-staging.authkit.app",
    base_url="http://localhost:8080"
))

@mcp.tool
def greet(name: str) -> str:
    return f"Hello, {name}!"

mcp.run(transport="http", host="localhost", port=8080)



# # app/app.py
# import logging
# import os
# from fastmcp import FastMCP
# from fastmcp.server.auth.providers.workos import AuthKitProvider
# from starlette.requests import Request
# from starlette.responses import JSONResponse

# logger = logging.getLogger("mcp")

# mcp = FastMCP("korzo AI", auth=AuthKitProvider(
#     authkit_domain="https://protective-champion-19-staging.authkit.app",
#     base_url="http://127.0.0.1:8080"
# ))

# @mcp.tool
# def greet(name: str) -> str:
#     return f"Hello, {name}!"

# mcp.run(transport="streamable-http", host="0.0.0.0", port=8080)
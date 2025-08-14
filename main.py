from fastmcp import FastMCP, Context
from loguru import logger
from config import settings
import asyncio
from typing import Dict, Any

# 创建FastMCP服务器实例
mcp = FastMCP(name="Development MCP Server")

# 配置日志
logger.add(
    settings.LOG_FILE,
    rotation=settings.LOG_ROTATION,
    level=settings.LOG_LEVEL
)

@mcp.tool
async def execute_command(command: str, ctx: Context) -> Dict[str, Any]:
    """Execute a command and return its result"""
    logger.info(f"Executing command: {command}")
    
    # 记录到客户端
    await ctx.info(f"Processing command: {command}")
    
    # 模拟命令执行
    await asyncio.sleep(0.1)  # 模拟处理时间
    
    result = {
        "status": "success",
        "command": command,
        "result": f"Command '{command}' executed successfully",
        "timestamp": str(asyncio.get_event_loop().time())
    }
    
    logger.info(f"Command executed: {result}")
    return result

@mcp.tool
async def get_server_status(ctx: Context) -> Dict[str, Any]:
    """Get the current server status"""
    await ctx.info("Checking server status...")
    
    return {
        "status": "running",
        "server_name": "Development MCP Server",
        "version": "1.0.0",
        "uptime": "running"
    }

@mcp.tool
async def echo_message(message: str, ctx: Context) -> str:
    """Echo a message back to the client"""
    await ctx.info(f"Echoing message: {message}")
    return f"Echo: {message}"

if __name__ == "__main__":
    # 使用Streamable HTTP传输运行MCP服务器（推荐）
    mcp.run(
        transport="streamable-http",
        host=settings.HOST,
        port=settings.PORT,
        path="/mcp"
    )
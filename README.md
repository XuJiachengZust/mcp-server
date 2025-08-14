# MCP Server

一个基于Python FastMCP框架实现的MCP（Mars Code Protocol）服务器。

## 功能特点

- 基于Streamable HTTP实现的高性能服务
- 内置三个基础工具：
  - execute_command：执行命令并返回结果
  - get_server_status：获取服务器状态
  - echo_message：消息回显
- 完整的日志系统，支持日志轮转
- 可配置的服务器设置
- 支持异步命令执行
- 支持上下文感知的工具执行

## 安装

1. 克隆项目：
```bash
git clone https://github.com/yourusername/mcp-server.git
cd mcp-server
```

2. 安装依赖：
```bash
pip install -r requirements.txt
```

## 使用方法

### 启动服务器

```bash
python main.py
```

服务器将在配置的地址和端口上启动（默认为 http://127.0.0.1:8082/mcp）。

### 配置说明

主要配置项（在config.py文件中）：

- HOST: 服务器监听地址（默认：127.0.0.1）
- PORT: 服务器端口（默认：8082）
- LOG_LEVEL: 日志级别（默认：INFO）
- LOG_FILE: 日志文件路径（默认：mcp_server.log）
- LOG_ROTATION: 日志轮转设置（默认：500 MB）

## 内置工具

### execute_command
执行命令并返回结果。支持异步执行，并会记录命令执行过程。

### get_server_status
获取服务器当前状态，包括运行状态、服务器名称、版本等信息。

### echo_message
简单的消息回显工具，用于测试服务器连接和消息传递。

## 开发计划

- [ ] 添加更多实用工具
- [ ] 增强安全性和认证机制
- [ ] 优化性能和资源使用
- [ ] 添加更多配置选项
- [ ] 实现插件系统

## 贡献

欢迎提交Issue和Pull Request！

## 许可证

MIT License
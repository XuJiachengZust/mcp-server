# Trae IDE 配置 MCP 服务器指南

## 概述

本指南将帮助您在 Trae IDE 中配置 MCP (Model Context Protocol) 服务器连接。

## 前提条件

1. 确保 MCP 服务器正在运行：
   ```bash
   python main.py
   ```
   服务器将在 `http://127.0.0.1:8082/mcp` 上运行

2. 验证服务器状态：
   ```bash
   python cli.py connect
   ```

## Trae IDE MCP 配置

### 方法一：通过 Trae 设置界面

1. **打开设置**
   - 点击 Trae IDE 右上角的设置图标
   - 或使用快捷键 `Ctrl + ,`

2. **找到 MCP 配置**
   - 在设置页面中搜索 "MCP" 或 "Model Context Protocol"
   - 或导航到 "Extensions" > "MCP Servers"

3. **添加 MCP 服务器**
   - 点击 "Add MCP Server" 或 "+" 按钮
   - 填写以下配置：

   ```json
   {
     "name": "Development MCP Server",
     "url": "http://127.0.0.1:8082/mcp",
     "transport": "streamable-http",
     "enabled": true
   }
   ```

### 方法二：通过配置文件

1. **找到 Trae 配置文件**
   - Windows: `%APPDATA%\Trae\settings.json`
   - macOS: `~/Library/Application Support/Trae/settings.json`
   - Linux: `~/.config/Trae/settings.json`

2. **编辑配置文件**
   在 `settings.json` 中添加或修改 `mcpServers` 部分：

   ```json
   {
     "mcpServers": [
       {
         "name": "Development MCP Server",
         "url": "http://127.0.0.1:8082/mcp",
         "transport": "streamable-http",
         "enabled": true,
         "capabilities": {
           "tools": true,
           "prompts": true,
           "resources": true
         }
       }
     ]
   }
   ```

3. **重启 Trae IDE**
   保存配置文件后重启 Trae IDE 以应用更改。

## 验证连接

### 检查连接状态

1. **在 Trae IDE 中**
   - 查看状态栏是否显示 MCP 连接状态
   - 绿色图标表示连接成功
   - 红色图标表示连接失败

2. **使用开发者工具**
   - 按 `F12` 打开开发者工具
   - 查看 Console 标签页中的 MCP 相关日志

### 测试 MCP 功能

1. **工具调用测试**
   - 在 Trae 中尝试使用 MCP 提供的工具
   - 检查工具列表是否正确加载

2. **命令行验证**
   ```bash
   # 测试服务器响应
   python cli.py connect
   
   # 在交互模式中测试
   MCP> help
   MCP> tools
   MCP> status
   ```

## 常见问题排查

### 连接失败

1. **检查服务器状态**
   ```bash
   # 确保服务器正在运行
   python main.py
   ```

2. **检查端口占用**
   ```bash
   netstat -an | findstr 8082
   ```

3. **检查防火墙设置**
   - 确保端口 8082 未被防火墙阻止
   - 允许 Python 程序通过防火墙

### 配置错误

1. **URL 格式**
   - 确保 URL 格式正确：`http://127.0.0.1:8082/mcp`
   - 注意协议、主机、端口和路径

2. **传输方式**
   - 使用 `streamable-http` 而不是 `sse`
   - 确保 Content-Type 为 `text/event-stream`

3. **JSON 格式**
   - 验证配置文件的 JSON 语法正确性
   - 使用 JSON 验证工具检查格式

## 高级配置

### 自定义配置选项

```json
{
  "name": "Development MCP Server",
  "url": "http://127.0.0.1:8082/mcp",
  "transport": "streamable-http",
  "enabled": true,
  "timeout": 10000,
  "retryAttempts": 3,
  "retryDelay": 1000,
  "headers": {
    "User-Agent": "Trae-IDE/1.0",
    "Accept": "application/json, text/event-stream"
  },
  "capabilities": {
    "tools": true,
    "prompts": true,
    "resources": true,
    "experimental": false
  }
}
```

### 环境变量配置

可以使用环境变量来配置 MCP 服务器：

```bash
# Windows
set MCP_SERVER_URL=http://127.0.0.1:8082/mcp
set MCP_SERVER_TRANSPORT=streamable-http

# Linux/macOS
export MCP_SERVER_URL=http://127.0.0.1:8082/mcp
export MCP_SERVER_TRANSPORT=streamable-http
```

## 总结

1. 确保 MCP 服务器在 `http://127.0.0.1:8082/mcp` 上运行
2. 在 Trae IDE 中配置 MCP 服务器连接
3. 使用 `streamable-http` 传输方式
4. 验证连接状态和功能
5. 根据需要调整高级配置选项

配置完成后，您就可以在 Trae IDE 中使用 MCP 服务器提供的工具和功能了。
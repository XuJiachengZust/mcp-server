# Trae集成指南

本文档介绍如何将FastMCP服务器集成到Trae环境中。

## 配置说明

FastMCP服务器可以通过Trae的配置文件进行集成。在项目根目录下创建`trae.config.json`文件，配置内容如下：

```json
{
  "mcpServers": {
    "fastmcp-server": {
      "command": "python",
      "args": [
        "cli.py",
        "start"
      ],
      "cwd": ".",
      "env": {
        "HOST": "0.0.0.0",
        "PORT": "8000",
        "DEBUG": "false"
      }
    }
  }
}
```

### 配置项说明

- `mcpServers`: MCP服务器配置对象
  - `fastmcp-server`: 服务器实例名称（可自定义）
    - `command`: 启动命令（python）
    - `args`: 命令参数数组
    - `cwd`: 工作目录
    - `env`: 环境变量配置

### 环境变量

- `HOST`: 服务器监听地址
- `PORT`: 服务器端口
- `DEBUG`: 调试模式开关

## 使用方法

1. 确保已安装所有依赖：
```bash
pip install -r requirements.txt
```

2. 复制环境配置文件：
```bash
cp .env.example .env
```

3. 启动Trae，它会自动加载和运行MCP服务器。

## WebSocket连接

客户端可以通过以下WebSocket URL连接到服务器：
```
ws://localhost:8000/ws/{client_id}
```

## 示例客户端

可以使用项目提供的示例客户端进行测试：
```bash
python example_client.py
```

## 注意事项

1. 确保端口号没有被其他服务占用
2. 检查环境变量配置是否正确
3. 保持工作目录路径配置正确
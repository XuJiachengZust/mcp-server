# FastMCP Server

一个基于FastAPI实现的高性能MCP（Minecraft Control Protocol）服务器。

## 功能特点

- 基于WebSocket的实时通信
- 支持多客户端连接
- 完整的日志系统
- 可配置的服务器设置
- 命令行界面

## 安装

1. 克隆项目：
```bash
git clone https://github.com/yourusername/fastmcp.git
cd fastmcp
```

2. 安装依赖：
```bash
pip install -r requirements.txt
```

3. 配置环境：
```bash
cp .env.example .env
# 编辑.env文件，根据需要修改配置
```

## 使用方法

### 命令行界面

启动服务器：
```bash
python cli.py start
```

查看版本：
```bash
python cli.py version
```

查看服务器状态：
```bash
python cli.py status
```

### WebSocket API

连接WebSocket：
```
ws://your-server:8000/ws/{client_id}
```

## 配置说明

主要配置项（在.env文件中）：

- HOST: 服务器监听地址
- PORT: 服务器端口
- DEBUG: 调试模式开关
- LOG_LEVEL: 日志级别
- LOG_FILE: 日志文件路径
- MAX_MESSAGE_SIZE: 最大消息大小
- HEARTBEAT_INTERVAL: 心跳间隔

## 开发计划

- [ ] 实现更多MCP协议功能
- [ ] 添加认证系统
- [ ] 优化性能
- [ ] 添加更多管理命令
- [ ] 实现插件系统

## 贡献

欢迎提交Issue和Pull Request！

## 许可证

MIT License
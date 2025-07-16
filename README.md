# AI Agent Project

## Overview

AI Agent 演示项目，展示了在 Python 中使用 AI Agent、提示词（Prompt）和 MCP（多上下文处理）的应用。

## Installation

This Project is managed by uv, a Python package manager. To install the project dependencies, run:

```bash
uv install
```

Init project with:

```bash
uv init
```

Install the required packages:

```bash
uv sync
```

## Usage

Run the AI agent with:

```bash
uv run ai-agent-demo.py
```

## Extra tasking

1. 注意到当前代码中，每一次会话无法调用之前的上下文信息。扩展 AI Agent 使得每次会话都能调用之前的上下文信息。
2. 实现功能：能够自动创建 markdown 文档，并将 test 文件中的每份代码简介写入到 markdown 文档中。

## Resources

- [10 分钟讲清楚 Prompt, Agent, MCP 是什么](https://www.bilibili.com/video/BV1aeLqzUE6L?vd_source=bde7c0fa35aba01c4e164a3fb9ec7ec3)

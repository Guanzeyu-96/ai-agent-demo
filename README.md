# AI Agent Project

## Overview

AI Agent 演示项目。

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
2. 实现功能：让AI创建 markdown 文档，并将 test 文件中的每份代码简介写入到 markdown 文档中。

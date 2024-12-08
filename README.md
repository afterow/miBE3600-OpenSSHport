# Token 验证与 HTTP 请求工具

## 项目简介

小米BE3600开启SSH的python工具

## 功能

- 获取用户输入的 token，并验证其长度和格式。
- 发送 HTTP POST 请求。
- 检查响应内容以确定操作是否成功。
- 输出每次请求的响应结果。

## 依赖

- Python 3.x
- `http.client` 模块（Python 标准库，无需额外安装）
- `re` 模块（Python 标准库，无需额外安装）

## 使用方法

1. 确保你的环境中已安装 Python 3.x。
2. 将代码保存为 `token_request.py`。
3. 在终端中运行以下命令：

   ```bash
   python token_request.py

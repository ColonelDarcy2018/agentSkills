# 工具与链路映射

## 1. MCP Tools（AI 自动化主通道）

| Tool | 作用 | 典型时机 |
|------|------|----------|
| `list_connected_devices` | 列出已连接设备 | 每次执行前 |
| `list_adb_devices` | 发现 ADB 设备 | 无已连接设备时 |
| `connect_device` | 连接设备并检测塔斯 | 首次连接/重连 |
| `execute_rpa_code` | 下发并执行脚本 | 脚本准备后 |
| `get_execution_logs` | 获取执行日志 | 执行中轮询 |
| `take_screenshot` | 获取页面证据 | 元素/状态疑难时 |
| `stop_execution` | 停止任务 | 卡死或用户中止 |

## 2. Daemon API（MCP 兜底）

| API | 作用 |
|-----|------|
| `GET /api/devices` | 查询设备 |
| `POST /api/devices/connect` | 连接设备 |
| `POST /api/execute` | 执行脚本 |
| `GET /api/execute/{job_id}/logs` | 查询任务日志 |
| `POST /api/devices/{serial}/screenshot` | 截图 |

## 3. 插件能力（人工协同）

| 命令 | 作用 |
|------|------|
| `RPA: 连接设备` | 可视化连接设备 |
| `RPA: 运行代码` | 从编辑器直接执行 |
| `RPA: 查看日志` | 查看输出日志 |
| `RPA: 截图` | 快速抓图诊断 |

## 4. Android 端真实执行路径

1. `HttpServer /api/run` 接收脚本。
2. `RpaJobManager.newDebugJob` 解压 `mobile_package.zip` 并替换 `project/app.py`。
3. `JobRunner` 入队执行，`RpaRunThread` 循环消费。
4. `RpaPyJob.mainTask -> PythonExecutor.runTask`。
5. `run.py` 动态加载并执行 `RPAProject.main`。
6. 日志经 `JobRecoder -> NanoHTTPDSSE` 推送。

## 5. 链路决策

- 默认：MCP（自动闭环）
- MCP 不可用：Daemon API
- 用户希望人工控制：插件命令


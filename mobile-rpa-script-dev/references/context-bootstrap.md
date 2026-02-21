# 上下文启动（必读）

## 1. 什么是“高级指令”

在本项目语境中，“高级指令”是指在手机端调试页（如 `/code`）直接编写并执行 Python 脚本的能力，底层通过 `HttpServer /api/run` 把脚本转为调试任务。

核心链路：

1. 调试页提交 `script` 与 `packageName` 到 `/api/run`。
2. `RpaJobManager.newDebugJob` 解压 `mobile_package.zip` 到 runtime。
3. 将脚本写入 `project/app.py`。
4. `JobRunner` 入队，`RpaRunThread` 执行。
5. `PythonExecutor -> run.py` 动态加载并执行 `RPAProject.main`。

## 2. 脚本入口规范

默认入口统一按以下形式输出：

```python
def main(zbot, *args, **kwargs):
    ...
```

说明：

- 文档中强调新版本流程包使用 `main(zbot, *args, **kwargs)`。
- `run.py` 对 `main` 参数做兼容检测，但本 skill 统一要求带 `zbot`，避免跨版本差异。

## 3. 运行前硬性前置条件

来自 Android 端 `RpaPyJob.onPrepare` 的真实约束：

1. 文件读取权限可用。
2. 悬浮窗（塔斯助手）开启。
3. 无障碍服务开启。
4. 当前不处于拾取状态。
5. 当前不处于布局检查状态。

任何一项失败，都应先修复环境再调脚本。

## 4. 日志与证据

- 调试页日志：SSE 推送（`JobRecoder -> HttpServer.sendMessage -> NanoHTTPDSSE`）。
- 开发平台日志：Daemon 通过 `adb logcat` 轮询采集。
- 交付时至少保留：`job_id + 关键日志 + 必要截图`。

## 5. 关于“报错行号偏移”的处理

`塔斯AI助理高级指令文档.md` 提到“报错行号-34”的旧机制（脚本插入固定偏移）。

在当前代码链路中，调试脚本是直接替换 `project/app.py`，不再是旧的固定插入位。若遇到旧环境或历史包仍出现偏移，再使用该换算规则。


---
name: mobile-rpa-script-dev
description: 开发、执行与调试 Android 手机 RPA Python 脚本（zbot）并形成闭环。使用 rpa-dev-platform 的 MCP Tools、Daemon API 与 Trae/VSCode 插件能力完成设备检查、脚本生成、运行、日志分析和定向修复。适用于“写手机 RPA 脚本/运行到手机看结果/根据报错修复/排查设备权限元素定位/生成最小复现脚本”等执行型请求；不用于纯需求拆解或纯业务逻辑建模。
---

# Mobile RPA Script Dev

## 作用
- 以“最小可运行脚本 + 执行证据 + 迭代修复”完成手机 RPA 开发闭环。

## 触发边界

### 触发
- 写脚本、跑脚本、看日志、按报错修脚本、设备权限元素定位排障。

### 不触发
- 纯需求拆解（交给“任务分解”）。
- 纯业务流程建模（交给“业务逻辑图谱”）。

## 协议引用
- 公共规则：`KCOS/protocol/p0-rules.md`
- 会话清单：`KCOS/protocol/ai-playbook.md`

## 上下文加载
1. `references/context-bootstrap.md`
2. `references/advanced-instruction-essentials.md`
3. `references/complex-script-playbook.md`（复杂脚本时）
4. `references/advanced-doc-routing.md`（查大文档时）

## 最小流程
1. 明确目标、成功标准、前置条件；不明确先提澄清问题。
2. 检查环境：`list_connected_devices`（必要时 `list_adb_devices` / `connect_device`）。
3. 先产出最小可运行脚本（入口必须 `def main(zbot, *args, **kwargs):`）。
4. 执行并观测：`execute_rpa_code` + `get_execution_logs`（必要时 `take_screenshot`）。
5. 失败时按单一根因迭代修复并复跑。

## 工具优先级
1. MCP Tools：`list_connected_devices`、`list_adb_devices`、`connect_device`、`execute_rpa_code`、`get_execution_logs`、`take_screenshot`
2. Daemon API：`/api/devices`、`/api/devices/connect`、`/api/execute`、`/api/execute/{job_id}/logs`
3. 插件命令：`RPA: 连接设备`、`RPA: 运行代码`、`RPA: 查看日志`、`RPA: 截图`

## 输出契约
- 环境状态：设备连接、塔斯可达、阻塞前置条件。
- 脚本：完整可执行脚本（含规范入口）。
- 执行证据：`job_id` + 关键日志 + 必要截图。
- 修复建议：最可能根因 + 下一步动作 + 重试条件。
- 方案对比（如适用）：成熟基线方案 + 更优备选 + 推荐结论。

## 执行规则
- 先环境检查，再执行脚本。
- 先最小可运行，再增量增强。
- 关键节点必须有可观测日志。
- 每次修复只改一类根因。
- 优先成熟方案，存在更优路径时给备选与权衡。

## References
- `references/context-bootstrap.md`
- `references/advanced-instruction-essentials.md`
- `references/workflow.md`
- `references/complex-script-playbook.md`
- `references/code-patterns.md`
- `references/troubleshooting.md`
- `references/tooling-map.md`
- `references/advanced-doc-routing.md`
- `scripts/split_advanced_doc.py`
- `KCOS/knowledge/business-logic/mobile-rpa-script-dev-skill-logic.md`

---
name: kcos-protocol-bootstrap
description: 初始化 KCOS 协议目录与基线文件（p0-rules、ai-playbook、protocol README），并按当前 KCOS P0 约束补齐最小目录骨架。适用于“新仓落地 KCOS 协议”“修复 protocol 缺失”“统一项目协议基线”等请求；不用于具体业务代码开发。
---

# KCOS Protocol Bootstrap

## 作用
- 用统一、可复用的方式初始化 `KCOS/protocol/` 与 P0 必需目录骨架。
- 提供当前 KCOS 的权威协议说明，避免模型继续输出混乱或过时约定。

## 权威协议说明（当前版本）

### 规范层级
1. **规则权威源**：`KCOS/protocol/p0-rules.md`
2. **会话操作清单**：`KCOS/protocol/ai-playbook.md`
3. **知识入口**：`KCOS/knowledge/README.md`

### P0 关键约束
- `KCOS/knowledge/**` 是知识权威源（Single Source of Truth）。
- `KCOS/.index.json`、`KCOS/.kcos/**` 是机器派生资产，不手工编辑。
- P0 必需目录：`context/`、`knowledge/`、`templates/`、`assets/`、`scripts/`、`.kcos/`。
- `KCOS/knowledge/` 每个一级子目录必须有 `README.md`。
- 仅允许项目内相对路径链接，禁止绝对路径。
- 新增/修改知识文档后必须执行：`python3 KCOS/scripts/kcos_p0.py sync`。

### AI 会话基线
- 会话开始必须读取 `KCOS/knowledge/README.md`。
- 用户要求恢复上下文时，读取 `KCOS/context/current-task.md` 与 `session-latest.md`。
- 会话结束若改动知识文档，必须执行一次 `sync`。

### 常见失败模式
- 缺少必需目录或 `knowledge/*/README.md`：`validate` 失败。
- `KCOS-Index.id` 重复：`validate` 失败。
- `KCOS-Index` 缺失/链接目标缺失：`validate` 告警。

## 触发边界

### 触发
- 新项目要初始化 KCOS 协议目录。
- 现有项目缺少 `KCOS/protocol` 或基础目录。
- 需要统一并重置协议基线（P0）。

### 不触发
- 纯业务流程梳理（交给 `业务逻辑图谱`）。
- 纯任务拆解排期（交给 `任务分解`）。

## 最小流程
1. 确认目标仓库根目录（默认当前目录）。
2. 执行初始化脚本：`python3 scripts/init_kcos_protocol.py --root <repo_root>`。
3. 若需要覆盖已有协议文件，追加 `--force`。
4. 检查脚本输出中的 created/updated/skipped 统计。
5. 执行 `python3 KCOS/scripts/kcos_p0.py sync`。

## 输出契约
- 已创建/更新的目录与文件清单。
- 是否触发覆盖写入（`--force`）。
- 是否具备 `kcos_p0.py` 并完成 `sync`。
- 后续建议（例如补齐知识域文档）。

## 脚本
- `scripts/init_kcos_protocol.py`
- `assets/protocol/p0-rules.md`
- `assets/protocol/ai-playbook.md`
- `assets/protocol/README.md`
- `assets/scripts/kcos_p0.py`

# KCOS AI Playbook（会话操作清单）

本文件是 AI 在 KCOS 下执行任务的标准操作清单。

## 1) 会话开始

### MUST
- 读取 `KCOS/knowledge/README.md` 作为知识入口。

### SHOULD
- 若用户明确要求恢复上下文，读取：
  - `KCOS/context/current-task.md`
  - `KCOS/context/session-latest.md`

## 2) 执行中

### SHOULD
- 按问题类型选择知识域：
  - 业务流程：`knowledge/business-logic/`
  - 架构方案：`knowledge/architecture/`
  - 需求资产：`knowledge/requirements/`
  - 决策记录：`knowledge/decisions/`
  - 可复用模式：`knowledge/patterns/`
  - 脚本案例规范：`knowledge/rpa/`
- 优先链接现有知识，避免重复内联长文本。
- 信息不明确时，先向用户提澄清问题。

## 3) 会话结束

### SHOULD
- 如有上下文管理诉求，更新：
  - `KCOS/context/current-task.md`
  - `KCOS/context/session-{YYYYMMDD}-{n}.md`
  - `KCOS/context/session-latest.md`

### MUST
- 若新增/修改了知识文档，执行：

```bash
python3 KCOS/scripts/kcos_p0.py sync
```

## 4) 输出约定（建议）

- 给出“当前状态 + 证据 + 下一步”。
- 若存在多方案，默认先给成熟基线，再给更优备选与权衡理由。
- 明确标注需要用户确认的决策点。

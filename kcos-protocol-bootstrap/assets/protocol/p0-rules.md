# KCOS P0 公共约束（规则权威源）

本文件定义 KCOS P0 的公共约束，供所有技能和知识文档统一引用。

## 1. 资产分区

### MUST
- 将 `KCOS/knowledge/**` 视为知识权威源（Single Source of Truth）。
- 将 `KCOS/.index.json`、`KCOS/.kcos/**` 视为机器派生资产。
- 禁止手工编辑 `KCOS/.index.json`。

### SHOULD
- 优先将人类可读决策写入 `knowledge/` 或 `context/`，再由脚本派生索引。

## 2. 目录与结构

### MUST
- 保持以下目录存在：
  - `KCOS/context/`
  - `KCOS/knowledge/`
  - `KCOS/templates/`
  - `KCOS/assets/`
  - `KCOS/scripts/`
  - `KCOS/.kcos/`
- `KCOS/knowledge/` 的每个一级子目录必须包含 `README.md`。

## 3. 链接规范

### MUST
- 仅使用相对路径链接项目内文件。
- 禁止使用绝对路径链接（如 `file:///...`、`/Users/...`、`C:\...`）。

### SHOULD
- 链接目标应存在；不存在时尽快修复。

## 4. KCOS-Index 元数据

### SHOULD（P0 当前级别）
- 知识文档建议包含 `KCOS-Index` front matter。
- `id`、`domain`、`tags`、`related`、`created`、`updated` 建议完整填写。

### MUST
- 若填写了 `KCOS-Index.id`，必须保证在知识库内唯一。

## 5. 命令约束

### MUST
- 在新增/修改知识文档后，至少执行一次：

```bash
python3 KCOS/scripts/kcos_p0.py sync
```

### SHOULD
- 在大批量调整前先执行 `validate`，降低返工。

## 6. 规则级别映射（与当前脚本行为对齐）

| 规则 | 级别 | 当前脚本行为 |
|------|------|--------------|
| 必需目录缺失 | error | `validate` 失败 |
| `knowledge/*/README.md` 缺失 | error | `validate` 失败 |
| `KCOS-Index.id` 重复 | error | `validate` 失败 |
| 绝对路径链接 | error | `validate` 失败 |
| `KCOS-Index` 缺失 | warning | `validate` 通过但告警 |
| `KCOS-Index.id` 缺失 | warning | `validate` 通过但告警 |
| 链接目标不存在 | warning | `validate` 通过但告警 |
| `related` 引用缺失 | warning | `validate` 通过但告警 |

> 注：上述等级是 P0 当前约定。若未来引入 strict 模式，可将部分 warning 升级为 error。

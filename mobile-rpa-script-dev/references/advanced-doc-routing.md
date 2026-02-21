# 大文档路由：塔斯AI助理高级指令文档.md

## 结论

`塔斯AI助理高级指令文档.md` 信息量很大（超大单文件）。不建议每次任务把全文加载进上下文。

应采用“精简版先读 -> 目录定位 -> 关键词检索 -> 按段加载”的策略。

## 0. 先读精简版

先加载：`references/advanced-instruction-essentials.md`。

只有精简版无法覆盖当前问题时，再继续本文件的路由流程。

## 1. 推荐读取顺序

1. 先看“开发入门 + FAQ”
2. 再看目标能力所在组件章节（如 selector / automator / app / device）
3. 仅在遇到特定问题时，加载对应 FAQ 段落

## 2. 主题到章节映射

- 入口规范：`新版流程包结构调整`
- 权限问题：`无障碍权限...`、`没有悬浮窗权限`、`剪切板权限异常`
- 元素问题：`元素不可见`、`元素点击无反应`、`无法拾取的悬浮窗口`
- API 能力：`3 自动化组件手册` 下对应子章节
- 代码模板：`6 项目流程代码模板参考`（若后续补全）

## 3. 实操检索建议

示例检索关键词：

- `main(zbot`
- `元素不可见`
- `detectAllWindow`
- `clickable=true`
- `adb logcat`
- `app.launch`

## 4. Skill 使用规则

当触发以下场景时，才补读大文档片段：

1. 用户明确要求“按高级指令规范输出”。
2. 脚本运行出现权限/窗口/定位疑难。
3. 需要查某个 `zbot` API 的细节参数。

其余场景优先使用本 skill 的 `references/*.md`。

## 5. 优化建议（工程化）

建议将大文档拆分为结构化小文档（可逐步落地）：

1. `advanced/00-index.md`（总目录）
2. `advanced/10-bootstrap.md`（入门与入口规范）
3. `advanced/20-faq.md`（常见故障）
4. `advanced/30-api-selector.md`
5. `advanced/31-api-automator.md`
6. `advanced/32-api-app-device.md`

拆分后，AI 可按任务加载最小片段，显著降低上下文噪音。

## 6. 自动切分工具

可直接使用：`scripts/split_advanced_doc.py`

示例：

```bash
scripts/split_advanced_doc.py --source 塔斯AI助理高级指令文档.md --out /tmp/tars-advanced-split
```

输出会包含：

- `00-index.md`：切分目录
- `NN-*.md`：分章节片段


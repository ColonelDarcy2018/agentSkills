# 塔斯高级指令精简要点（给新 AI / 新项目）

## 1. 最小认知模型

- 你在写的是手机端 RPA Python 脚本。
- 执行入口使用 `main(zbot, *args, **kwargs)`。
- 脚本会下发到设备端运行，日志是排障主依据。

## 2. 最小开发闭环

1. 连接设备并确认塔斯可达。
2. 写最小可运行脚本（启动 app + 一个关键动作 + 日志）。
3. 执行并拿到 `job_id`。
4. 轮询日志并定位失败步骤。
5. 单点修复后重跑。

## 3. 高频 API 组（优先掌握）

1. 日志/控制：`zbot.log`、`zbot.error`、`zbot.console.show`
2. 应用操作：`zbot.app.launchApp`、`zbot.app.getPackageName`
3. 元素定位：`zbot.selector().text()/id()/desc()/className()`
4. 自动化动作：`click`、`zbot.automator.click/swipe/back/home`
5. 设备信息：`zbot.device.width/height`

## 4. 高频故障与首选动作

- 权限异常：先修环境，不先改脚本。
- 元素不可见：加 `boundsInside(0,0,width,height)`。
- 点击无效：定位到 `clickable=true`，再做父层/坐标回退。
- 悬浮窗场景：`detectAllWindow()` 后必须 `detectActiveWindow()` 还原。

## 5. 复杂脚本最小工程化要求

- 分阶段函数，不要全部堆在 main。
- 每阶段至少一条成功/失败日志。
- 每个关键动作有 fallback。
- 输出可复现实验条件（设备、账号、页面前置）。

## 6. 何时再去读完整大文档

只有在以下情况才按需加载完整文档片段：

1. 某个 API 参数不确定。
2. 权限/窗口异常无法解释。
3. 用户明确要求“严格按高级指令文档”。


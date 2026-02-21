# 代码模式与模板

## 1. 最小可运行模板

```python
def main(zbot, *args, **kwargs):
    zbot.console.show()
    zbot.log("[STEP] 启动目标应用")
    zbot.app.launchApp("微信")
    zbot.sleep(2000)

    zbot.log("[STEP] 检查页面元素")
    target = zbot.selector().text("通讯录").findOne(5000)
    if target:
        zbot.log("[OK] 命中目标元素")
    else:
        zbot.error("[FAIL] 未命中目标元素")

    zbot.log("[DONE] 执行完成")
```

## 2. 可见区域过滤

用于规避“元素不可见”：

```python
visible_selector = zbot.selector().boundsInside(
    0, 0, zbot.device.width, zbot.device.height
)
node = visible_selector.text("发送").findOne(3000)
if node:
    node.click()
```

## 3. 点击分层回退

用于“click 无响应”：

```python
btn = zbot.selector().text("发送").findOne(3000)
if btn:
    if btn.clickable():
        btn.click()
    else:
        parent = btn.parent()
        if parent and parent.clickable():
            parent.click()
        else:
            bounds = btn.bounds()
            zbot.automator.click(bounds.centerX(), bounds.centerY())
```

## 4. 多窗口拾取策略

用于悬浮窗或多窗口场景：

```python
zbot.element.findOneEnsure(
    zbot.selector().detectAllWindow().text("通讯录"),
    "通讯录标签",
    timeout=20000
).click()

zbot.selector().detectActiveWindow()
```

## 5. 产出约束

- 入口函数必须为 `main(zbot, *args, **kwargs)`。
- 核心步骤必须写日志，便于远程排障。
- 优先输出“可执行且可观测”的版本，而不是一次性追求完整自动化。


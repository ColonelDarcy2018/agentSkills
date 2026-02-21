# 复杂脚本开发打法

## 1. 先拆阶段，不写“一坨脚本”

推荐结构：

```python
def phase_launch(zbot): ...
def phase_navigate(zbot): ...
def phase_action(zbot): ...
def phase_verify(zbot): ...

def main(zbot, *args, **kwargs):
    phase_launch(zbot)
    phase_navigate(zbot)
    phase_action(zbot)
    phase_verify(zbot)
```

每个阶段必须输出 `[STEP]` 与 `[OK]/[FAIL]` 日志。

## 2. 定位策略分层

定位优先级建议：

1. 稳定 ID（若可用）
2. 文本 + 可见区域约束
3. 结构关系（parent/child/closest clickable）
4. 坐标点击（最后兜底）

避免只依赖单个文本定位。

## 3. 动作要可回退

对每个关键动作提供 fallback：

- click 失败：父层 click -> 坐标 click
- 页面未到达：重试导航 -> 回退 -> 重进
- 元素未出现：短等待 + 重查 + 截图保留

## 4. 明确完成判定（不要凭感觉成功）

至少定义一个可观测完成条件：

- 命中目标元素
- 页面包名/Activity 达到预期
- 关键日志关键字出现

## 5. 错误处理分层

- 环境错误：设备/权限/塔斯不可达 -> 立即停止并先修环境。
- 脚本错误：语法、空对象、定位失败 -> 小步修复。
- 业务错误：页面变化、账号状态异常 -> 请求用户补充上下文。

## 6. 可复用的复杂任务模式

1. **任务链模式**：按阶段串行，阶段间有显式验证。
2. **状态机模式**：页面状态不稳定时，用状态节点驱动跳转。
3. **幂等重试模式**：允许重复执行而不产生副作用。
4. **证据驱动模式**：每个关键节点可追溯日志/截图。


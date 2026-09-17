# Maya AI Assistant 0.3.0 中文安装与升级

## 一、需要复制哪个文件

运行时只需要：

```text
plug-ins\maya_ai_assistant.py
```

复制到：

```text
%USERPROFILE%\Documents\maya\2026\plug-ins\maya_ai_assistant.py
```

如果目录不存在，可以在 Maya 的 Python 脚本编辑器运行：

```python
import os
import maya.cmds as cmds

user_dir = cmds.internalVar(userAppDir=True)
plugin_dir = os.path.join(user_dir, "2026", "plug-ins")
os.makedirs(plugin_dir, exist_ok=True)
print(plugin_dir)
os.startfile(plugin_dir)
```

## 二、第一次加载

Maya 中文版：

**窗口 → 设置/首选项 → 插件管理器**

找到：

```text
maya_ai_assistant.py
```

勾选：

- 已加载
- 自动加载（可选）

然后：

**窗口 → 常规编辑器 → 脚本编辑器 → Python**

执行：

```python
import maya.cmds as cmds
cmds.mayaAIAssistant()
```

## 三、确认 Maya 实际加载的文件

如果窗口仍然显示旧版，在 Python 脚本编辑器执行：

```python
import maya.cmds as cmds
print(cmds.pluginInfo("maya_ai_assistant.py", q=True, path=True))
```

输出路径就是 Maya 当前加载的插件位置。

## 四、升级覆盖

1. 保存 Maya 工程。
2. 关闭 Maya。
3. 用新版 `maya_ai_assistant.py` 覆盖旧文件。
4. 重新启动 Maya。
5. 打开插件管理器重新加载。
6. 检查窗口标题版本。

如果 Maya 缓存了旧插件，可以先在插件管理器取消“已加载”，关闭 Maya，再覆盖文件。

## 五、API 配置

界面最上方有「配置预设」下拉，可直接套用 DeepSeek / OpenAI / rightcode。
**预设只填「接口类型 / Base URL / Model」，不会改动 API Key。**

### DeepSeek

插件选择：

```text
OpenAI-compatible Chat Completions
```

然后填写 DeepSeek 提供给你的：

- Base URL
- Model ID
- API Key

### rightcode

插件选择：

```text
RightCode Responses
```

然后填写：

- Base URL：`https://www.rightapi.ai/codex/v1`
- Model：`gpt-5.2`
- API Key：你的 rightcode API Key

rightcode 的请求格式与 OpenAI 原生 Responses 不同（`input` 项要带 `"type": "message"`，且按 SSE 流式返回），插件已单独处理，无需手动改动任何东西。

API Key 不会写入 QSettings。

## 六、常见报错

### `Syntax error`，且报错前缀是 `// 错误:`
说明你在 MEL 标签里执行了 Python。切换到 Python 标签。

### `Scene target does not exist`
AI 计划引用了场景里不存在的名称。重新生成计划，或在提示中明确要求确定性命名。

### `不适合选定的多个对象`
通常是 Maya Polygon 组件命令跨多个网格执行。当前版本已尽量按网格拆分，但复杂组件操作仍建议逐个网格处理。

### Arnold 无法加载
确认 Maya 安装包含 MtoA，并在插件管理器中可加载 `mtoa`。

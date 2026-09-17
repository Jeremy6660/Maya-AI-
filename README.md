# Maya AI Assistant 0.3.0 — Complete Package

面向 **Autodesk Maya 2026 / Maya 2026.3** 的自然语言 AI 助手。

核心流程：

**中文/自然语言 + 图片/文件参考 → AI 生成受控 JSON 计划 → Maya 白名单执行器 → 建模/材质/灯光/动画/动力学/渲染**

插件不会执行模型返回的 Python、MEL、Shell 或 PowerShell 代码。

## 项目文件

```text
MayaAIAssistant_0.3.0_COMPLETE/
├─ plug-ins/
│  └─ maya_ai_assistant.py      # 必需：插件本体，运行时唯一必需文件
├─ README.md                     # 项目说明
├─ INSTALL_CN.md                 # 中文安装/升级说明
├─ EXAMPLE_PROMPTS.md            # 示例自然语言指令
├─ QUICK_TEST.py                 # Maya Python Script Editor 自检脚本
├─ PROVIDER_CONFIGS.md           # API Provider 配置示例
├─ PROJECT_FILES.md              # 文件用途和部署位置清单
└─ CLAUDE.md                     # 给 AI 协作者的项目约定（与插件运行无关）
```

**运行 Maya 插件时，真正必须复制的只有 `plug-ins/maya_ai_assistant.py`。** 其余文件是文档、配置参考和测试辅助，不需要放入 Maya 插件目录。

## 主要能力

### 自然语言 / API
- OpenAI Responses API
- OpenAI-compatible Chat Completions
- RightCode Responses（独立请求路径，兼容 SSE 流式返回）
- DeepSeek 等兼容 Chat Completions 的服务
- 「配置预设」下拉，一键套用 rightcode / DeepSeek / OpenAI，不改动 API Key
- API Key 默认只存在内存中，不通过 QSettings 持久化
- 支持 `DEEPSEEK_API_KEY` / `OPENAI_API_KEY` 环境变量
- API 请求在线程中执行，避免阻塞 Maya UI

### 图片与文件附件
- 图片：PNG / JPG / JPEG / GIF / WebP
- 文本：TXT / MD / JSON / CSV / XML / YAML / PY / MEL / OBJ / MTL / MA / USDA 等
- 本地资产：FBX / ABC / USD / USDC / USDZ / MB / HDR / EXR / TX
- `.py` / `.mel` 附件只作为文本上下文，不执行
- 二进制资产不会把文件内容直接上传给模型；只向模型提供文件名/本地路径上下文，实际导入由 Maya 本地执行

### Polygon 建模
- Cube / Sphere / Cylinder / Cone / Torus / Plane
- Transform / Duplicate / Rename / Delete / Group / Parent
- Bevel / Smooth / Face Extrude / Combine
- Boolean Union / Difference / Intersection
- Merge Vertices / Triangulate / Quadrangulate
- Automatic / Planar / Cylindrical / Spherical UV
- 专用标准足球生成器：12 个五边形 + 20 个六边形

### NURBS 建模
- NURBS Sphere / Cylinder / Cone / Plane / Circle
- Curve from control points
- Loft
- Revolve
- Curve-on-path Extrude

### 材质与贴图
- Lambert
- `standardSurface` PBR（不可用时回退 Lambert）
- Base Color / Roughness / Metalness
- Base Color Texture
- Roughness Texture
- Metalness Texture
- Normal/Bump Texture

### 摄影机与灯光
- Camera + Focal Length
- Directional / Point / Spot / Area Light
- 颜色 / Intensity / Exposure
- Spot Cone / Penumbra
- Arnold SkyDome + HDRI

### 动画
- Translate / Rotate / Scale Keyframes
- Numeric Attribute Keyframes
- Auto / Linear / Step Tangents
- Playback Range / FPS

### 粒子与动力学
- nParticle
- Omni / Directional Emitter
- Rate / Speed / Speed Random / Lifespan / Radius
- Gravity / Turbulence / Vortex
- Dynamic field connection
- Maya Classic Rigid Body Active / Passive

### Arnold 渲染
- 自动尝试加载 `mtoa`
- Resolution
- AA / Diffuse / Specular / Transmission / SSS / Volume Samples
- Output Prefix
- Render Current Frame

## Windows 安装

把：

```text
plug-ins\maya_ai_assistant.py
```

复制到：

```text
%USERPROFILE%\Documents\maya\2026\plug-ins\maya_ai_assistant.py
```

然后在 Maya 中文版：

1. **窗口 → 设置/首选项 → 插件管理器**
2. 找到 `maya_ai_assistant.py`
3. 勾选 **已加载**；需要时勾选 **自动加载**
4. 打开 **窗口 → 常规编辑器 → 脚本编辑器**
5. 切换到 **Python**
6. 执行：

```python
import maya.cmds as cmds
cmds.mayaAIAssistant()
```

窗口标题应显示：

```text
Maya AI Assistant  0.3.0
```

## DeepSeek 示例

在插件界面填写：

```text
接口类型：OpenAI-compatible Chat Completions
Base URL：https://api.deepseek.com
Model：填写你账号当前可用的 DeepSeek 模型 ID
API Key：你的 DeepSeek API Key
```

不要在截图、群聊或公开仓库中暴露 API Key。

## RightCode 示例

在插件界面填写：

```text
接口类型：RightCode Responses
Base URL：https://www.rightapi.ai/codex/v1
Model：gpt-5.2
API Key：你的 RightCode API Key
```

RightCode 的 `/responses` 请求体与返回格式都和 OpenAI 原生不同（`input` 项需带 `"type": "message"`，且按 SSE 流式返回），插件已单独走一条请求路径处理，不需要手动改任何东西。详细说明见 `PROVIDER_CONFIGS.md`。

## 安全设计

插件只执行固定白名单操作。AI 返回内容必须是：

```json
{
  "summary": "...",
  "operations": [
    {"op": "primitive", "primitive": "cube", "name": "Box"}
  ]
}
```

不允许模型返回并执行：

- Python
- MEL
- Shell / PowerShell
- 任意系统命令
- `eval()` / `exec()`

执行计划使用 Maya Undo Chunk；发生异常时插件会尝试整批回滚。

## 依赖

不需要额外 `pip install`。

插件使用 Maya 2026 自带：

- Python 3
- `maya.cmds`
- Maya Python API 2.0
- PySide6
- shiboken6

可选功能依赖本机 Maya 安装：

- Arnold / MtoA：Arnold 高质量渲染、SkyDome
- MayaUSD：USD 导入
- AbcImport：Alembic 导入
- FBX 插件：FBX 导入

## 当前限制

这是扩展型 MVP，不是完整 Maya 全自动 Agent。当前尚未完整覆盖：

- nCloth
- Bullet
- Bifrost
- XGen
- MASH
- 完整 Rigging / Skinning / Retopology
- 所有 Arnold 节点及 AOV 管线

复杂生产场景仍应先检查“计划预览”再执行，并保存工程版本。

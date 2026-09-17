# 当前项目全部文件说明

| 文件 | 是否运行时必需 | 用途 | 应放位置 |
|---|---|---|---|
| `plug-ins/maya_ai_assistant.py` | **是** | Maya 插件本体，包含 UI、API Client、附件读取、计划验证、41 个白名单执行器 | `%USERPROFILE%\Documents\maya\2026\plug-ins\` |
| `README.md` | 否 | 项目总说明 | 任意位置 |
| `INSTALL_CN.md` | 否 | 中文安装与升级步骤 | 任意位置 |
| `EXAMPLE_PROMPTS.md` | 否 | 建模/材质/灯光/动画/粒子等示例 Prompt | 任意位置 |
| `PROVIDER_CONFIGS.md` | 否 | 配置预设表 + DeepSeek / OpenAI-compatible / Responses / RightCode 配置参考 | 任意位置 |
| `QUICK_TEST.py` | 否 | Maya 内快速加载、打开窗口、检查插件路径 | Script Editor 中运行或任意位置保存 |
| `CLAUDE.md` | 否 | 给 AI 协作者的项目约定与红线（与插件运行无关） | 仓库根目录 |

## 外部 Python 包

**无。** 不需要 `requirements.txt`，也不需要 `pip install`。

运行依赖全部由 Maya 2026 提供：

- `maya.cmds`
- `maya.api.OpenMaya`
- `maya.OpenMayaUI`
- `PySide6`
- `shiboken6`
- Python 标准库

## 可选 Maya 插件

某些功能只有本机装有相应 Maya 模块时可用：

- `mtoa`：Arnold
- `AbcImport`：Alembic
- MayaUSD：USD
- FBX：FBX 导入

这些不是本项目分发文件，不要复制到本项目目录。

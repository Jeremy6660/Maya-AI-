# -*- coding: utf-8 -*-
"""在 Maya 2026 Script Editor 的 Python 标签执行。"""

import maya.cmds as cmds

PLUGIN = "maya_ai_assistant.py"

if not cmds.pluginInfo(PLUGIN, q=True, loaded=True):
    cmds.loadPlugin(PLUGIN)

print("Loaded:", cmds.pluginInfo(PLUGIN, q=True, loaded=True))
print("Path:", cmds.pluginInfo(PLUGIN, q=True, path=True))

if cmds.commandInfo("mayaAIAssistant", exists=True):
    cmds.mayaAIAssistant()
    print("Maya AI Assistant window opened.")
else:
    raise RuntimeError("mayaAIAssistant command was not registered.")

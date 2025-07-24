# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
@File    :  ui_node.py
@Time    :  2025-07-24 17:11:15
@Author  :  Alfred Clark
@Contact :  alfredclark@163.com
@Desc    :  
"""
from comfy.comfy_types import IO
from .base_node import *


class UINode(BaseNode):
    """
    UI节点
    """
    NODE_NAME = "UINode"
    DISPLAY_NAME = "UI Node"

    DESCRIPTION = "UI Node Template"
    CATEGORY = DEFAULT_CATEGORY
    FUNCTION = "run"

    @classmethod
    def INPUT_TYPES(cls) -> dict:
        return {
            "required": {
                "ui_input": (IO.STRING, {"multiline": True}),
            }
        }

    RETURN_TYPES = (IO.STRING,)

    @classmethod
    def run(cls, ui_input, **kwargs):
        return (f'{ui_input}',)

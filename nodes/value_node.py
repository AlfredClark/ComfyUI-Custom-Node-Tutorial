# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
@File    :  value_node.py
@Time    :  2025-07-24 12:41:39
@Author  :  Alfred Clark
@Contact :  alfredclark@163.com
@Desc    :  
"""
from .base_node import *
from comfy.comfy_types import IO


class ValueNode(BaseNode):
    """
    数值相关功能节点
    """
    NODE_NAME = "Value Node"
    DISPLAY_NAME = "Value Node"

    CATEGORY = DEFAULT_CATEGORY

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "input_int": (IO.INT, {
                    "default": 50,  # 默认值
                    "min": 0,  # 最小值
                    "max": 100,  # 最大值
                    "step": 5,  # 步进数
                    "round": True,  # 数值取整
                    "display": "number",  # 数值输入框
                    "lazy": False  # 延迟求值
                }),  # 整数输入
                "input_float": (IO.FLOAT, {
                    "default": 0.0,
                    "min": 0,
                    "max": 100,
                    "step": 0.01,
                    "round": False,
                    "display": "slider",  # 滑块输入框
                    "lazy": False
                }),  # 浮点数输入
                "input_string": (IO.STRING, {
                    "default": "default",  # 默认值
                }),  # 字符串输入
                "input_text": (IO.STRING, {
                    "default": "DEFAULT",
                    "multiline": True,  # 多行文本
                    "dynamicPrompts": True,  # 动态提示
                    "tooltip": "input_text tooltip text",  # 工具提示
                }),  # 多行文本输入
            },  # 必须的输入节点
            "optional": {
                "input_number": (IO.NUMBER,),  # 数值输入
                "input_optional": (IO.STRING,)  # 文本输入
            },  # 可选的输入节点
            "hidden": {
                "unique_id": "UNIQUE_ID",  # 节点的唯一标识符
                "prompt": "PROMPT",  # 客户端发送到服务器的完整提示
                "extra_pnginfo": "EXTRA_PNGINFO",  # 额外PNG信息
                "dynprompt": "DYNPROMPT"  # 动态Prompt
            },  # 隐藏的输入节点
        }

    RETURN_TYPES = (IO.INT, IO.FLOAT, IO.NUMBER, IO.STRING, IO.STRING, IO.STRING,)
    RETURN_NAMES = ("output_int", "output_float", "output_number", "output_string", "output_text", "output_optional",)

    @classmethod
    def run(cls, input_int, input_float, input_string, input_text, input_number=75, input_optional="Optional",
            **kwargs):
        """
        可选输入需要设置默认值，其余隐藏输入可以使用**kwargs接收
        """
        for key, value in kwargs.items():
            print(f"{key}: {value}")
        return input_int, input_float, input_string, input_text, input_number, input_optional

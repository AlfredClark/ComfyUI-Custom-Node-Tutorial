# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
@File    :  locale_node.py
@Time    :  2025-07-25 10:24:07
@Author  :  Alfred Clark
@Contact :  alfredclark@163.com
@Desc    :  
"""
from .base_node import *
from comfy.comfy_types import IO


class LocaleNode(BaseNode):
    NODE_NAME = "LocaleNode"
    DISPLAY_NAME = {
        "en": "Locale Node",
        "zh": "本地化节点",
    }
    DESCRIPTION = "Locale Node Template"

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
            },  # 必须的输入节点
            "optional": {
                "input_number": (IO.NUMBER,),  # 数值输入
                "input_optional": (IO.IMAGE,)  # 文本输入
            },  # 可选的输入节点
            "hidden": {
                "locale_name": LOCALE_TYPE  # 传出本地化类型
            }
        }

    RETURN_TYPES = (IO.INT, IO.FLOAT, IO.STRING, IO.NUMBER, IO.IMAGE,)
    RETURN_NAMES = ("output_int", "output_float", "output_string", "output_number", "output_image",)

    @classmethod
    def run(cls, input_int, input_float, input_string, input_number=75, input_optional="Optional", **kwargs):
        """
        可选输入需要设置默认值，其余隐藏输入可以使用**kwargs接收
        """
        for key, value in kwargs.items():
            print(f"{key}: {value}")
        return input_int, input_float, input_string, input_number, input_optional

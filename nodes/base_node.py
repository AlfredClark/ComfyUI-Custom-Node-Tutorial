# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
@File    :  base_node.py
@Time    :  2025-07-24 07:09:16
@Author  :  Alfred Clark
@Contact :  alfredclark@163.com
@Desc    :  基础节点
"""
from .config import *


class BaseNode:
    """
    基础节点类：继承该类的节点会自动被扫描并加载到映射字典中
    """
    # 自定义添加的类参数
    NODE_NAME = None  # 节点名称：用于节点注册，全局唯一
    DISPLAY_NAME = {
        DEFAULT_LOCALE_TYPE: NODE_NAME,
    }  # 展示名称：支持本地化字典类型，也可以直接使用字符串，不设置则使用NODE_NAME
    RETURN_DISPLAY_NAMES = {
        DEFAULT_LOCALE_TYPE: (),
    }  # 输入输出展示名：支持本地化的字典类型，也可以直接使用元组

    # 官方使用的类参数
    CATEGORY = DEFAULT_CATEGORY  # 节点的前端显示类别
    DESCRIPTION = None  # 节点描述信息（鼠标瞄准节点时显示在预览下部的描述信息）

    RETURN_TYPES = ()  # 返回类型，必须有有效值，无返回则使用()
    RETURN_NAMES = ()  # 返回命名，与RETURN_TYPES长度相同的字符元组，不填写则使用类型小写

    FUNCTION = "run"  # 运行函数名

    OUTPUT_NODE = False  # 是否为输出节点
    EXPERIMENTAL = False  # 是否为实验性节点

    INPUT_IS_LIST = False  # 输入是否为列表，默认False

    # OUTPUT_IS_LIST = (False,)  # 与RETURN_TYPES长度相同的bool元组，需要在子类中实现

    @classmethod
    def INPUT_TYPES(cls) -> dict:
        """
        输入类型函数
        返回一个包含输入类型的字典
        """
        return {
            "required": {},  # 必须的输入节点
            "optional": {},  # 可选的输入节点
            "hidden": {
                "unique_id": "UNIQUE_ID",  # 节点的唯一标识符
                "prompt": "PROMPT",  # 客户端发送到服务器的完整提示
                "extra_pnginfo": "EXTRA_PNGINFO",  # 额外PNG信息
                "dynprompt": "DYNPROMPT"  # 动态Prompt
            },  # 隐藏的输入节点
        }

    @classmethod
    def VALIDATE_INPUTS(cls, **kwargs) -> bool | str:
        """
        校验输入值
        返回True表示校验通过，返回str表示错误提示
        """
        return True

    @classmethod
    def IS_CHANGED(cls, **kwargs) -> any:
        """
        是否改变
        通过对比两次运行的输入决定是否跳过该节点运行
        """
        return kwargs

    @classmethod
    def run(cls, **kwargs):
        """
        运行函数
        需要与FUNCTION所定义的名称相同
        """
        return (*kwargs,)

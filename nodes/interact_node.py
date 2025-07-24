# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
@File    :  interact_node.py
@Time    :  2025-07-24 13:35:31
@Author  :  Alfred Clark
@Contact :  alfredclark@163.com
@Desc    :  
"""
import os
from aiohttp import web
from .base_node import *
from server import PromptServer
from comfy.comfy_types import IO


class InteractNode(BaseNode):
    """
    交互功能节点
    """
    NODE_NAME = "InteractNode"
    DISPLAY_NAME = "Interact Node"
    DESCRIPTION = "Interact Node Template"

    CATEGORY = DEFAULT_CATEGORY

    @classmethod
    def INPUT_TYPES(cls):
        # 获得初始化使用的列表数据
        model_type_list = os.listdir('models')
        model_name_list = os.listdir(os.path.join('models', model_type_list[0]))
        return {
            "required": {
                "model_type": (model_type_list,),  # COMBO下拉列表
                "model_name": (model_name_list,),
            },
            "hidden": {
                "unique_id": "UNIQUE_ID",  # 节点的唯一标识符
                "prompt": "PROMPT",  # 客户端发送到服务器的完整提示
                "extra_pnginfo": "EXTRA_PNGINFO",  # 额外PNG信息
                "dynprompt": "DYNPROMPT"  # 动态Prompt
            },  # 隐藏的输入节点
        }

    RETURN_TYPES = (IO.STRING,)
    RETURN_NAMES = ("model_path",)
    FUNCTION = "run"

    @classmethod
    def run(cls, model_type, model_name, **kwargs):
        """
        可选输入需要设置默认值，其余隐藏输入可以使用**kwargs接收
        """
        # 注意单值返回也需要使用元组
        return ("{}".format(os.path.join(model_type, model_name)),)


# 获得ComfyUI路由
routes = PromptServer.instance.routes


# 定义需要使用的接口
@routes.post('/interact_node')
async def interact_with_node(request):
    the_data = await request.post()  # 获得异步请求信息
    data = dict(the_data)  # 转换数据格式
    names = os.listdir(os.path.join('models', data['type']))  # 获得需要返回的数据
    return web.json_response({
        "names": names
    })  # 返回响应数据

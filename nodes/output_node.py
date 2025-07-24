# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
@File    :  output_node.py
@Time    :  2025-07-24 15:26:32
@Author  :  Alfred Clark
@Contact :  alfredclark@163.com
@Desc    :  输出节点
"""
import json
import os
import uuid

import numpy as np
from PIL import Image
from PIL.PngImagePlugin import PngInfo

from .base_node import *
from comfy.cli_args import args
from comfy.comfy_types import IO


class OutputNode(BaseNode):
    """
    输出节点，以图像保存为例
    """
    NODE_NAME = "OutputNode"
    DISPLAY_NAME = "Output Node"

    DESCRIPTION = "Output Node Template"
    CATEGORY = DEFAULT_CATEGORY
    FUNCTION = "run"

    OUTPUT_NODE = True  # 注意需要将OUTPUT_NODE设置为True

    @classmethod
    def INPUT_TYPES(cls) -> dict:
        return {
            "required": {
                "images": (IO.IMAGE, {})  # 图片张量输入
            },
            "hidden": {
                "unique_id": "UNIQUE_ID",  # 节点的唯一标识符
                "prompt": "PROMPT",  # 客户端发送到服务器的完整提示
                "extra_pnginfo": "EXTRA_PNGINFO",  # 额外PNG信息
                "dynprompt": "DYNPROMPT"  # 动态Prompt
            },  # 隐藏的输入节点
        }

    RETURN_TYPES = ()  # 输出节点返回值为空元组

    @classmethod
    def run(cls, images, **kwargs):
        results = list()
        # 遍历传入的图片张量
        for (batch_number, image) in enumerate(images):
            # 张量数据转换
            i = 255. * image.cpu().numpy()
            img = Image.fromarray(np.clip(i, 0, 255).astype(np.uint8))
            # 图片元数据
            metadata = None
            if not args.disable_metadata:
                metadata = PngInfo()
                if kwargs['prompt'] is not None:
                    metadata.add_text("prompt", json.dumps(kwargs['prompt']))
                if kwargs['extra_pnginfo'] is not None:
                    for x in kwargs['extra_pnginfo']:
                        metadata.add_text(x, json.dumps(kwargs['extra_pnginfo'][x]))
            # 图片保存路径
            file = f"{uuid.uuid4()}.png"
            save_folder = 'temp'  # 注意需要web端可以访问的路径，如: ['input', 'output', 'temp']
            subfolder = 'example'  # 子文件夹
            save_path = os.path.join(save_folder, subfolder)
            if not os.path.exists(save_path):
                os.makedirs(save_path)
            img.save(os.path.join(save_path, file), pnginfo=metadata, compress_level=4)
            # 添加返回数据
            results.append({
                "filename": file,
                "subfolder": subfolder,
                "type": save_folder
            })
        # 图像所使用的特殊返回
        return {"ui": {"images": results}}

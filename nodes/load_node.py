# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
@File    :  load_node.py
@Time    :  2025-07-24 16:29:24
@Author  :  Alfred Clark
@Contact :  alfredclark@163.com
@Desc    :  加载节点
"""
import os

import torch
import numpy as np

import folder_paths
import node_helpers
from .base_node import *
from comfy.comfy_types import IO
from PIL import Image, ImageSequence, ImageOps


class LoadNode(BaseNode):
    """
    加载节点（以图片加载为例）
    """
    NODE_NAME = "LoadNode"
    DISPLAY_NAME = "Load Node"

    DESCRIPTION = "Load Node Template"
    CATEGORY = DEFAULT_CATEGORY
    FUNCTION = "run"

    @classmethod
    def INPUT_TYPES(cls) -> dict:
        # 获得input文件夹中的图片列表
        images = [
            f for f in os.listdir(folder_paths.get_input_directory()) if f.endswith(
                (".png", ".jpg", ".jpeg", ".webp", ".bmp", ".gif", ".jpe", ".apng", ".tif", ".tiff"))
        ]
        return {
            "required": {
                "image": (images, {
                    "image_upload": True  # 上传并加载选中图片
                })
            },
            "hidden": {
                "unique_id": "UNIQUE_ID",  # 节点的唯一标识符
                "prompt": "PROMPT",  # 客户端发送到服务器的完整提示
                "extra_pnginfo": "EXTRA_PNGINFO",  # 额外PNG信息
                "dynprompt": "DYNPROMPT"  # 动态Prompt
            },  # 隐藏的输入节点

        }

    RETURN_TYPES = (IO.IMAGE,)

    @classmethod
    def run(cls, image, **kwargs):
        # 传入的image为上传后返回的文件名
        image_path = folder_paths.get_annotated_filepath(image)
        # 加载图片
        img = node_helpers.pillow(Image.open, image_path)
        output_images = []
        w, h = None, None
        excluded_formats = ['MPO']
        # 处理图像张量
        for i in ImageSequence.Iterator(img):
            i = node_helpers.pillow(ImageOps.exif_transpose, i)
            if i.mode == 'I':
                i = i.point(lambda i: i * (1 / 255))
            image = i.convert("RGB")
            if len(output_images) == 0:
                w = image.size[0]
                h = image.size[1]
            if image.size[0] != w or image.size[1] != h:
                continue
            image = np.array(image).astype(np.float32) / 255.0
            image = torch.from_numpy(image)[None,]
            output_images.append(image)
        if len(output_images) > 1 and img.format not in excluded_formats:
            output_image = torch.cat(output_images, dim=0)
        else:
            output_image = output_images[0]
        # 返回图像张量
        return (output_image,)

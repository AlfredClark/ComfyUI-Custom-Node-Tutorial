# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
@File    :  __init__.py
@Time    :  2025-07-24 05:25:19
@Author  :  Alfred Clark
@Contact :  alfredclark@163.com
@Desc    :  入口文件
"""
from .nodes import *

# 获得用户管理程序及本地化设置
try:
    from app.user_manager import UserManager

    user_manage = UserManager()  # 获取用户管理器
    locale_type = user_manage.settings.get_settings(None).get('Comfy.Locale')  # 获得本地化设置
except Exception as e:
    locale_type = DEFAULT_LOCALE_TYPE  # 默认本地化
    del e

# 节点名称类型映射（包含要导出的所有节点及其名称的字典，注意名称需要全局唯一）
NODE_CLASS_MAPPINGS = {}
for node in nodes_class_list:
    NODE_CLASS_MAPPINGS[node.NODE_NAME] = node

# 节点展示名称映射（包含节点的展示标题名称的字典）
NODE_DISPLAY_NAME_MAPPINGS = {}
for node in nodes_class_list:
    if isinstance(node.DISPLAY_NAME, dict):
        # 支持本地化的多语言展示名
        NODE_DISPLAY_NAME_MAPPINGS[node.NODE_NAME] = locale_select(node.DISPLAY_NAME, node.NODE_NAME)
    elif isinstance(node.DISPLAY_NAME, str):
        # 直接定义的展示名
        NODE_DISPLAY_NAME_MAPPINGS[node.NODE_NAME] = node.DISPLAY_NAME
    else:
        # 默认使用节点名
        NODE_DISPLAY_NAME_MAPPINGS[node.NODE_NAME] = node.NODE_NAME

# 设置 Web 目录，该目录中的任何.js文件都会被前端作为前端扩展脚本加载
WEB_DIRECTORY = "web"

# 自定义节点元数据信息
__version__ = "1.0.0"  # 版本信息
__author__ = "Alfred Clark"  # 作者信息
__doc__ = "Custom Nodes Template"  # 文本信息

# 需要导出的映射与目录（根据具体已添加的信息选择是否导出）
# __all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS"]
__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS", "WEB_DIRECTORY"]

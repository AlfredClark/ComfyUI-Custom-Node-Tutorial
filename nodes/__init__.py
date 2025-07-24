# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
@File    :  __init__.py.py
@Time    :  2025-07-24 06:30:05
@Author  :  Alfred Clark
@Contact :  alfredclark@163.com
@Desc    :  节点包入口文件
"""
from .value_node import ValueNode
from .interact_node import InteractNode

# nodes_class_list = BaseNode.__subclasses__()  # 获得所有BaseNode的子类
nodes_class_list = [ValueNode, InteractNode]
nodes_class_list = [
    nodes_class for nodes_class in nodes_class_list if nodes_class.NODE_NAME is not None
]  # 去除没有定义节点名称的子类

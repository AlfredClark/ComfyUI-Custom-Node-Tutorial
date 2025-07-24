# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
@File    :  config.py
@Time    :  2025-07-24 10:36:52
@Author  :  Alfred Clark
@Contact :  alfredclark@163.com
@Desc    :  节点相关默认设置
"""
# 默认本地化语言（缺省设置）
DEFAULT_LOCALE_TYPE = "en"
# 默认前端显示类别
DEFAULT_CATEGORY = "Example"

# 获得用户管理程序及本地化设置
try:
    from app.user_manager import UserManager

    user_manage = UserManager()  # 获取用户管理器
    locale_type = user_manage.settings.get_settings(None).get('Comfy.Locale')  # 获得本地化设置
except Exception as e:
    locale_type = DEFAULT_LOCALE_TYPE  # 默认本地化
    del e

# 本地化语言
LOCALE_TYPE = locale_type


# 本地化选择器
def locale_select(locale_dict: dict, default: any):
    if LOCALE_TYPE in locale_dict.keys():
        return locale_dict[LOCALE_TYPE]
    elif DEFAULT_LOCALE_TYPE in locale_dict.keys():
        return locale_dict[DEFAULT_LOCALE_TYPE]
    else:
        for value in locale_dict.values():
            return value
        return default

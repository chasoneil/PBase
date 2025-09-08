#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# python 中的模块本质上就是一个文件 可以从文件中导入方法 也可以导入全部
# 如果需要做细粒度更精确的区分，那么就需要加文件夹，一个文件夹就等同于Java中的一个包
# 但是这个文件夹要有__init__.py文件才会被正确识别


print('1. 普通导入')
print('1.1 基础导入:')

# 导入一个模块就可以使用一个模块中所有的方法
import support1
support1.print_info('chason', 18)
print('sup1 add:', support1.add(1, 2))

# 也可以导入单个方法  from module_name import function_name
from support2 import max
print('sup2 max:', max(3, 1))

print('1.2 不同的包导入:')

from utils.user import *

print_name('fox')
print_age(29)
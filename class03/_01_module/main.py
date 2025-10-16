#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 1. python 中的模块本质上就是一个文件 可以从文件中导入方法 也可以导入全部
# 如果需要做细粒度更精确的区分，那么就需要加文件夹，一个文件夹就等同于Java中的一个包
# 但是这个文件夹要有__init__.py文件才会被正确识别, 所以一个含有 __init__.py的文件夹其实就是一个python包

# 2. 对于导入文件的变量，如果是普通变量名 （不是以下划线开头的） 则默认可以引用
# _ 或者 __ 开头的 例如 _tmp 这种变量默认是 private 导入也是不能引用的，同理方法也是

# 如果使用 import * 则必须是module级别 不能放在方法中
from utils.user import *

# 导入一个模块就可以使用一个模块中所有的方法
import support1

# 也可以导入单个方法  from module_name import function_name
from support2 import max

def test1():
    support1.print_info('chason', 18)
    print('sup1 add:', support1.add(1, 2))

def test2():
    print('sup2 max:', max(3, 1))

def test3():
    print_name('fox')
    print_age(20)

def test4():
    pwd = support1.get_pwd()
    print(pwd)

if __name__ == '__main__':
    # test1()
    # test2()
    # test3()
    test4()
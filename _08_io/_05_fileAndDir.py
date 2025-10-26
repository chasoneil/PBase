#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 如果需要使用操作系统级别的命令 python 提供 os

import os

# 获取操作系统的各种信息
def demo1():
    # 获取操作系统的类型
    print(os.name)              # nt -> windows
    # 获取环境变量的内容
    print(os.environ)       # 环境变量获取到一个dict
    # 获取指定环境变量
    print(os.environ.get('WINDIR'))             # C:\WINDOWS 根据环境变量，每个人的结果可能不同


if __name__ == '__main__':
    demo1()
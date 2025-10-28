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

# 查看当前目录的路径
def demo2():
    path = os.path.abspath('')
    print(path)

# 拼接和拆分目录
def demo3():
    # 使用 join() 拼接目录
    path = os.path.join('/temp/chason', 'testdir')
    print(path)
    # 使用 split() 拆分目录
    file_split = os.path.split('/temp/testdir/file.txt')
    print(file_split)           # ('/temp/testdir', 'file.txt') 返回的是一个元组

# 使用os对文件进行处理
def demo4():
    os.rename('test.txt', 'test_new.txt')
    print('文件重命名成功')

# we use os.remove() to delete file
def demo5():
    os.remove("tmp.txt")
    print("删除文件成功")

# 8. create dir and delete dir
# we use os.mkdir() to create dir
def demo6():
    os.mkdir("temp/")
    print("创建文件夹成功")

# delete empty dir
def demo7():
    os.rmdir("temp/")  # if dir is not empty, program will throw error
    print("删除文件夹成功")

import shutil
def demo8():
    shutil.rmtree("temp/d1") # delete dir and all files inside
    print("删除文件夹下的子文件夹成功")

# 列出当前文件夹下的所有内容
# splitext可以获取文件的扩展名
def demo9():
    file_list = os.listdir('')
    print(file_list)
    for f in file_list:
        if os.path.splitext(f)[1] == '.py':
            print(f)

if __name__ == '__main__':
    # demo1()
    # demo2()
    # demo3()
    demo9()
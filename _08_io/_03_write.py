#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

# 写文件 主要使用write()
# w 模式文件会直接覆盖
def demo1():
    with open('py.txt', 'w') as f:
        f.write('good morning')
        f.write('早上好')              # 直接写中文会乱码  且没有换行
        f.close()

# 追加写入文件的方式 aw
def demo2():
    with open('py.txt', 'w', encoding='utf-8') as f:
        f.write("Hello python\n")
        f.close()

    # 以追加的方式写入
    with open('py.txt', 'a') as f:
        f.write("Nice to meet you\n")
        f.close()

# 使用os对文件进行处理
def demo3():
    os.rename('test.txt', 'test_new.txt')
    print('文件重命名成功')

# we use os.remove() to delete file
def demo4():
    os.remove("tmp.txt")
    print("删除文件成功")

# 8. create dir and delete dir
# we use os.mkdir() to create dir
def demo5():
    os.mkdir("temp/")
    print("创建文件夹成功")

# delete empty dir
def demo6():
    os.rmdir("temp/")  # if dir is not empty, program will throw error
    print("删除文件夹成功")

import shutil
def demo7():
    shutil.rmtree("temp/d1") # delete dir and all files inside
    print("删除文件夹下的子文件夹成功")

if __name__ == '__main__':
    # demo1()
    # demo2()
    # demo3()
    # demo4()
    # demo5()
    # demo6()
    demo7()

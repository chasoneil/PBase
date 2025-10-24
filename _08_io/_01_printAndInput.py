#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 控制台输入输出

# 1. print console output
def demo1():
    print("Hello, Python")
    # 使用 , 输出拼接的字符串
    name = 'zhangsan'
    print('My name is', name)
    # 输出中可以包含运算
    print('1 + 2 =', 1+2)

# 2. we use input(); raw_input() [python2] to get input from user
def demo2():
    content = input("Please input:")
    print("Your input:", content)
    # in python2 we could use like this:
    # content = raw_input("请输入:")

# 如果不需要提示词，也可以直接使用input()
def demo3():
    name = input()
    print('Your name:', name)



# 4. we use write() to write something to file
def demo4():
    f = open("D:/temp/py1.txt", "w")  # create file
    f.write("Hello, Python. \nWe use python write to write content.\n")
    print("write done")
    f.close()



# second read is after the first read,so the file pointer is important!
# demo5() # read: Hello, Pyt

def demo6():
    f = open("D:/temp/py1.txt", "r")
    content = f.read()
    print(content)
    f.close()

#demo6()

# 6. we use tell() to get file position
# we use seek to set pointer to file start
def demo7():
    f = open("D:/temp/py1.txt", "r")
    content1 = f.read(10)
    p = f.tell()
    print("position:", p)
    f.seek(0, 0)
    p = f.tell()
    print("position:", p)
    f.close()

# demo7()

# 7. rename and delete file
import os

# we use os -> rename() to rename file
def demo8():
    # src filename, new filename
    os.rename("D:/temp/py1.txt", "D:/temp/py2.txt")
    print("rename file")

# demo8()

# we use os.remove() to delete file
def demo9():
    os.remove("D:/temp/py2.txt")
    print("delete file")

# demo9()

# 8. create dir and delete dir
# we use os.mkdir() to create dir

def demo10():
    os.mkdir("D:/temp/py")
    print("create dir")

# demo10()

# delete empty dir
def demo11():
    os.rmdir("D:/temp/py") # if dir is not empty, program will throw error
    print("delete dir")

# demo11()

import shutil
def demo12():
    shutil.rmtree("D:/temp/py") # delete dir and all files inside
    print("delete dir")

if __name__ == '__main__':
    #demo1()
    #demo2()
    demo3()






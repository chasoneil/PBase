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

if __name__ == '__main__':
    #demo1()
    #demo2()
    demo3()






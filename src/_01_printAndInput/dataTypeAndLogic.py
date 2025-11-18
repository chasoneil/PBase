#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 数据类型和逻辑运算符
# python的数据类型： 整数 浮点数 字符串 布尔 空值

# 整数 浮点数
def demo1():
    x = 10  # 整数
    print('x =', x)

    pi = 3.14 # 浮点数
    print('pi = ', pi)

# 字符串
def demo2():
    # python 中使用 '' / "" / ''' '''/ 来表示字符串
    print('single str')
    print("double str")
    # 字符串分行
    print('''long
    str''')

    print('I\'m Chinese')  # 有些字符需要转义
    print(r'\\\\t1')  # 使用 r可以让转义失效

# 布尔和空值
def demo3(flag):
    # python 中的布尔值是 True False
    if flag:
        print(True)
    else:
        print(False)

    # python中使用None表示空值
    a = None
    print('a =', a)

# 2. python 中使用and or not来代表与或非
def demo4(flag):
    if True and True:
        print('double true')
    if True or False:
        print('has true')

    if not flag:
        print('flag is False')
    else:
        print('flag is True')

# 使用 & | 做逻辑运算
def demo5():
    condition = True & True
    if condition:
        print('double true')
    else:
        print('has false')

    condition = True | False
    if  condition:
        print('has true')
    else:
        print('double false')

if __name__ == '__main__':
    demo1()
    demo2()
    demo3(False)
    demo4(True)
    demo5()
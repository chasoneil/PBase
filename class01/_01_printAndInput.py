#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 1. python 的输出print()
# 2. python 的输入input()
# 3. python 的数据类型
# 4. 逻辑运算符

# 1. print()
# 正常输出
print('Hello python.')

# print 中使用逗号可以分别输出多个字符串 遇到,会补充一个空格
print('Hello', 'Python', 'Over')   # result: Hello Python Over

# 输出函数中可以包含运算
print('1 + 2 =', 1+2)

print('01----------------------\n')

# 2. input()
# 使用input获取用户输入，回车结束
name = input()
print('Hello', name)

# 也可以在input中加入提示词
name = input('Please input your name:')
print('Hello', name)

print('02----------------------\n')

# 3. 数据类型
# python的数据类型： 整数 浮点数 字符串 布尔 空值
x = 10  # 整数
print('x =', x)

pi = 3.14 # 浮点数
print('pi = ', pi)

# python 中使用 '' / "" / ''' '''/ 来表示字符串
print('single str')
print("double str")
# 字符串分行
print('''long
str''')

print('I\'m Chinese')  # 有些字符需要转义
print(r'\\\\t1')  # 使用 r可以让转义失效

# python 中的布尔值是 True False
if True:
    print(True)
else:
    print(False)

# python中使用None表示空值
a = None
print('a =', a)

print('03----------------------\n')

# 4. python 中使用and or not来代表与或非
print('使用and or not 做逻辑运算:')
if True and True:
    print('double true')

if True or False:
    print('has true')

if not True:
    print('not true')
else:
    print('not false')

print('使用非关键字的方式做逻辑运算:')
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
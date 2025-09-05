#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# python 中的函数
# 1. 基础的函数定义和使用
# 2. 函数的参数

# 1. 系统函数，函数怎么使用
print('1. 系统函数:')
print('绝对值:', abs(-10))
print('最大值:', max(1, 2, 3, -4))     # 可变参数列表
print('1000的16进制:', hex(1000))

print('2. 函数参数化:')
# python 中函数名可以给变量 这点和JS类似
a = abs
print('绝对值:', a(-10))

# 定义函数: 使用def fun_name(param list) :
print('3. 定义函数:')
def get_max(a, b):
    return max(a, b)

print('get_max:',get_max(3, 4))

# 没有return的结果，返回的就是None
print('4. 如果函数没有return，那默认返回None')
def no_ret():
    print('no_ret 执行')

print('no_ret:', no_ret())

# 如果函数什么都不做，可以使用空函数 pass
print('5. 空函数 pass')
def do_nothing():
    pass

do_nothing()

# python 可以返回多个值
print('6. 返回多个值:')
def get_point(x, y, move_x, move_y):
    return x + move_x, y + move_y       # 返回多个结果,中间通过,隔开

x1, y1 = get_point(0, 0, 1, 1)
print('新的坐标:', x1, y1)

# 如果只用一个参数去接收多个返回结果
r = get_point(0, 0, 2, 2)
print('单个参数表示坐标:', r)       # (2, 2)  返回的其实是一个tuple

print('01 ----------------------\n')

# 2. 函数的参数

# 1. 给函数的参数设置默认值
print('1. 参数设置默认值:')
def power(x, n=2):      # 当没有给n的值，那么默认就是2次方, 必选参数必须在前
    res = 1
    while n > 0:
        res = res * x
        n -= 1
    return res

print('默认求平方:', power(2))
print('求多次方:', power(2, 4))

# 函数的默认值参数的其他用法
print('2. 指定特定参数的默认值:')
def print_student_msg(name, age, gender='M', addr='Shanghai'):
    print('name:', name)
    print('age:', age)
    print('gender:', gender)
    print('addr:', addr)
    print('----end----')

# print_student_msg('ceshi') 报错，因为没有给默认参数的就是必须参数
print_student_msg('zhangsan', 18)   # 非必要参数可以不传
print_student_msg('lisi', 20, 'F', 'Beijing')  # 传入所有非必要参数
print_student_msg('wangwu', 21, addr='Guangzhou')   # 也可以只传入对应的非必要参数

# 参数也可以是list tuple 等特殊类型
print('3. 参数是list:')
def print_list(l):
    print(l)

list1 = [1, 2, 3]
print_list(list1)

# 注意： 如果将参数的默认值设置为可变的，可能会出问题
print('4. 参数是默认值可能发生问题:')
def add_end(l=[]):  # 默认参数是list, 可变
    l.append('END')
    return l

print(add_end())    # ['END']
print(add_end())    # ['END', 'END']       每次调用改变了 list的默认值

# 解决上述问题的方法
def add_end1(l=None):
    if l is None:
        l = []
    l.append('end')
    return l

print(add_end1())
print(add_end1())

# python 支持可变参数
# 例: 求 任意 n个数的和 a + b + c + d...
# 可以通过传入list 或者 tuple的形式
print('5. 可变参数:')
def get_sum1(numbers):
    sum = 0
    for n in numbers:
        sum += n
    return sum

print('get_sum1:', get_sum1([1, 2, 3, 4]))
print('get_sum1:', get_sum1((2, 3, 4, 5)))

# 可以通过可变参数的形式

def get_sum2(*numbers):         # 函数本质上接收了一个tuple
    sum = 0
    for n in numbers:
        sum += n
    return sum

print('get_sum2:', get_sum2(1, 2, 3, 4))

# 允许在list和tuple前 加上一个 * 让list和tuple变成可变参数

list1 = [1, 2, 3]
print('as params:', get_sum2(*list1))

print('07 ----------------------')

# 关键字参数 提供一组可变长度的带参数名的参数列表
# 关键字参数使用 ** 的方法 接收的是dict
def print_param(name, age, **kw):
    print('name:', name)
    print('age:', age)
    print('other:', kw)

print_param('abc', 19)
print_param('abc', 19, sex='f')

print('08 ----------------------')
# 命名关键字函数，关键字函数的一种
# 传入的函数的关键字被指定为必须，如果没有这些关键字函数，会报错

def param_name(p1, p2, *, need1, need2):    # 必须要有 need1 和 need2
    print(p1, p2)
    print(need1, need2)

param_name('a', 'b', need1='c', need2='d')

print('09 ----------------------')

# 递归函数
# 求 1- n的阶乘

def fac(n):
    if n == 1:
        return 1
    else:
        return n * fac(n-1)

print('3的阶乘:', fac(3))
print('5的阶乘:', fac(5))
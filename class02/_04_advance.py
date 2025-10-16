#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 高级特性
# 1. 切片： 主要是针对可变长度的对象 List tuple string 直接通过下标的方式获取对应的元素
#   list的切片
#   tuple的切片
#   string的切片
# 2. 迭代
#   如何判断是否可以迭代
# 3. 列表生成式 python 内部用来生成列表的
# 4. 生成器 todo
# 5. 迭代器 todo

print('1. 切片:')
print('1.1 正常切片:')
arr = [1, 2, 3, 4, 5, 6]
tup = (1, 2, 3, 4, 5, 6)
str = '123456'

print('list前三个元素:', arr[0:3])  # arr[0:3] == arr[:3]  如若是从头开始的话0可以省略
print('tuple前三个元素:', tup[0:3])
print('str前三个元素:', str[0:3])

print('list指定下标区间(1-4):', arr[1:4])
print('tuple指定下标区间(1-4):', tup[1:4])
print('string指定下标区间(1-4):', str[1:4])

print('1.2 倒数切片:')
print('list后三个元素:', arr[-3:])       # arr[-3: -1]  -1是指倒数第二个元素，因为0已经是被正向的用了，所以这里要想涉及最后一个元素，就只能不写
print('tuple后三个元素:', tup[-3:])
print('string后三个元素:', str[-3:])

print('1.3 间隔切片:')
print('list0-4,每隔2个数切片:', arr[:4:2]) # [1, 3]
print('tuple0-4,每隔2个数切片:', tup[:4:2]) # (1, 3)
print('string0-4,每隔2个数切片:', str[:4:2]) # 13

# [a:b:c]  a:从什么下标开始  b到什么下标结束 c间隔多少个数取一个

print('01 ----------------------\n')

# python 中的迭代 Iteration 抽象程度高于其他语言
# 只要是可以迭代的对象，都可以进行迭代

print('1. 判断是否可以迭代:')
from collections.abc import Iterable

print('string是否可以迭代:', isinstance('abc', Iterable))
print('list是否可以迭代:', isinstance([], Iterable))
print('tuple是否可以迭代:', isinstance((), Iterable))
print('dict是否可以迭代:', isinstance({}, Iterable))

# python 中通过enumerate函数可以获取下标
print('2. 获取下标index')
tuple1 = ('a', 'b', 'c', 'd')
for index, val in enumerate(tuple1):
    print(index, ':', val)

# 单次迭代多个元素
print('3. 单次迭代多个元素:')
for x, y in [(1, 2), (2, 4), (4, 8)]:
    print(x, y)

print('--------------01--------------')

# 列表生成式
# 使用 list() 配合 range 快速生成列表

tmp_list1 = list(range(5))  # 生成 [0, 5) 的列表
print(tmp_list1)        # [0, 1, 2, 3, 4]

# 正式的列表生成式 使用 []
# 例子: 生成 [1*1, 2*2, 3*3, ... 10 *10] 的列表，方法一使用循环
tmp_list2 = []
for i in range(11):
    tmp_list2.append(i*i)
print(tmp_list2)

# 方法二：使用列表生成式
tmp_list3 = [x * x for x in range(0,11)]
print(tmp_list3)

# 列表生成式中可以有多个循环
tmp_list4 = [m + n for m in 'ABC' for n in 'XYZ']
print(tmp_list4)       # ['AX', 'AY', 'AZ', 'BX', 'BY', 'BZ', 'CX', 'CY', 'CZ']

# 使用列表生成式迭代一个 dict
d = {'a': 'A', 'b': 'B', 'c': 'C'}
tmp_list5 = [k + '=' + v for k, v in d.items()]     # 注意 k v都是String 才能使用 +
print(tmp_list5)                    # ['a=A', 'b=B', 'c=C']

# 列表生成式中还可以加判断
tmp_list6 = [x for x in range(11) if x % 2 == 0]
print(tmp_list6)        # [0, 2, 4, 6, 8, 10]





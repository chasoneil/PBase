#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 1. dict 字典 python中的字典 等同于 HashMap 或者 Hashtable
# 使用 key-value 形式存储数据，key 必须是不可变对象，value 可以是任意对象
# 2. Set 是一组key的集合

# 创建字典
print('1. 创建字典:')
dict1 = {}
print(dict1)

# 字典可以对象存储
print('2. 字典的值:')
dict2 = {"name":"chason", "age": 20, 1: 20} # key 必须是不可变对象 字符串数字等都是不可变对象
print(dict2)

print("dict2 length:", len(dict2))  # 字典长度是一个键值对算一个

# 通过key获取value
print('通过key获取value')
print('name:', dict2['name'])

print('3. 修改value:')
# 修改字典的value
dict2['age'] = 25
print(dict2)

print('4. 删除字典元素:')
# 删除字典的元素
del dict2[1]
print(dict2)

# 也可以通过pop删除
print('5. 使用pop删除元素')
d1 = {'a': 1, 'b': 2, 'c': 3}
print('删除前:', d1)
d1.pop('b')
print('删除后:', d1)

# 使用循环获取dict元素
print('6. 使用循环获取dict key')
dict3 = {'name': 'chason', 'age': 20, 'score': 90.5}
for key in dict3:
    print(key)

print('01 ----------------------\n')

# 2. set
print('1. 创建一个set')
s1 = {1, 2, 3} # 创建一个set
print(s1)

# set会自动过滤重复元素
print('2. set自动过滤重复元素')
s2 = {1, 2, 3, 2, 1}
print(s2)  # {1, 2, 3}

# 使用 add() 和 remove() 添加或删除元素
print('3. 使用add remove添加删除元素')
s3 = {'a', 'b', 'c'}
print(s3)
s3.add('m')     # 添加元素的位置不是有序的
print(s3)
s3.remove('m')
print(s3)

# set 因为不重复元素 可以做交并补
print('4. set求交并补')
s1 = {1, 2, 3}
s2 = {2, 3, 4}

sj = s1 & s2
sb = s1 | s2

print('交集:', sj)
print('并集:', sb)

# 注意: st = {1, [2, 3]}  报错, set中必须是不可变的元素
# print(st)
tt = (1, [2, 3])    # 正常输出
print(tt)
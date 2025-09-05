#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 1. for in 循环
#    range() 创建指定的序列
# 2. while 循环

# 1. for in 循环获取list元素
print('1. 正常for in循环')
list1 = [1, 2, 3]
for ele in list1:   # 循环获取元组中的元素
    print(ele)

print('2. 案例-求和:')
sum = 0
for ele in [1, 2, 3, 4, 5]:
    sum += ele
print('1-5的和:', sum)

# python 通过 range() 生成整数序列
# 例如 range(100) 生成1 - 99的整数序列 等同于 [0, 1, 2, ... 99]
print('3. 使用range() 生成序列:')
sum = 0
for ele in range(101) :
    sum += ele
print('1-100求和:', sum)

print('4. continue的使用:')
arr = list(range(10))
for ele in arr:
    if ele % 2 == 0:
        continue
    print(ele)

















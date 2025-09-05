#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 1. list  可变列表
# 2. tuple 不可变列表

# list 是一个数组， python中使用[] 来表示一个数组
classmates = ['zhangsan', 'lisi', 'wangwu']
# list 可以直接输出
print(classmates) # print : ['zhangsan', 'lisi', 'wangwu']

# python 支持数组元素不是相同类型
my_list = ['chason', 18, 87.12, 'abc']
print(my_list)

# 使用len() 获取数组长度
print('my_list len:',len(my_list))

print("====> list 相关操作:")

# 使用下标获取数组的元素 和Java相同
print('1.使用下标获取数组元素:')
print(my_list[0])
print(my_list[1])
print(my_list[2])
print(my_list[3])

print('2.从尾部获取元素:')
# 你可以使用负数用来从尾部获取元素
print('结尾元素:', my_list[-1])
print('倒数第二个元素:',my_list[-2])

print('3.使用append向数组中添加元素:')
# 向数组的结尾添加元素 append
print('添加前:', my_list)
my_list.append('yyy')
print('添加后:', my_list)

# 在数组的指定位置插入元素 insert
print('4.在数组的指定位置插入元素:')
print('插入前:', my_list)
my_list.insert(1, 'xxx')
print('插入后:', my_list)

# 弹出末尾的元素 pop()
print('5.弹出末尾元素:')
print('弹出前:', my_list)
my_list.pop()
print('弹出后:', my_list)

# 弹出指定位置的元素 pop(i)
print('6.弹出指定位置元素:')
print('弹出前:', my_list)
my_list.pop(1)
print('弹出后:', my_list)

# 通过下标直接替换元素
print('7.通过下标直接替换元素:')
print('替换前:', my_list)
my_list[1] = 'mmd'
print('替换后:', my_list)

# list中的元素也可以是另一个list
my_list[1] = [1, 2, 3]
print('数组嵌套:', my_list)

print('my_list[1][1]:', my_list[1][1])  # 数组嵌套其实就像二维数组

print('01 ----------------------\n')

# 元组：一种不可变的数组结构，初始化的时候就要确定所有的元素，你可以查，但是不能改
# 数组的大部分查询操作元组也都支持

my_tuple = ('chason', 'fox', 'lily')  # 这三个元素已经确定了不能改
print('元组:', my_tuple)

print('元组头:', my_tuple[0])
print('元组尾:', my_tuple[-1])

# 定义一个只有一个元素的元组
my_tuple1 = (1,)  # 如果要定义一个只有一个元素的元组，那么要加一个逗号
print(my_tuple1)






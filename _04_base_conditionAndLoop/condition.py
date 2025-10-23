#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 1. condition 所有的条件判断都是if else
# 2. 输入的数据类型的转换
# 3. 装配模式 match 类似于java中的switch

print('1. 基础判断:')
age = 10
if age > 10:    # 注意格式
    print('大人啦')
else:
    print('还是孩子')

# 多个条件中 使用elif
print('2. 多个条件使用elif:')
age = 18
if age < 0:
    print('年龄错误')
elif age >=0 | age < 10:
    print('还是孩子')
else:
    print('大人啦')

print('01 ----------------------\n')

age = input('请输入年龄:')   # 默认获取的类型是字符串类型
rage = int(age) # 使用int() 做类型转换
if rage < 18:
    print('未满18岁')
else:
    print('已满18岁')

print('02 ----------------------\n')

# 装配模式 match case (类似Java中的switch case)
print('1. 装配模式的基本使用:')
score = 'b'
match score:
    case 'a':
        print('level a')
    case 'b':
        print('level b')
    case 'c':
        print('level c')
    case _:                     # 表示匹配到其他的任意值
        print('unknown level')


print('2. 复杂装配模式:')
age = 18
match age:
    case x if x < 10:       # 支持表达式
        print('小于10岁')
    case 10:
        print('10岁')
    case 11 | 12 | 13:      # python中不支持java中的多个case并行，python中是条件并行
        print('11 - 13岁')
    case _:
        print('大于13岁')

print('3. 装配模式和list:')

list1 = ['zhangsan', 'lisi', 'wangwu']
match list1:
    case ['lisi']:
        print('名单中只有lisi')
    case ['zhangsan', 'zhaoliu']:
        print('名单中有 zhangsan zhaoliu')
    case ['zhangsan', name1, *others]:
        print('名单中有zhangsan和其他人')
    case _:
        print('other')
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 1. dict 字典 python中的字典 等同于Map
# 使用 key-value 形式存储数据，key 必须是不可变对象，value 可以是任意对象
# 2. Set 是一组key的集合

# 1. 创建字典
def test1():
    dict1 = {}
    print(dict1)

# key 必须是不可变对象 字符串数字等都是不可变对象
dict2 = {"name":"chason", "age": 20, 1: 20}

# 2. 字典的键值对获取和设置
def test2():
    print(dict2)
    print("dict2 length:", len(dict2))  # 字典长度是一个键值对算一个
    # 2.1 通过key获取value 获取方式跟数组有点相似 ['xxx']
    print('name:', dict2['name'])

def test2_1():
    # 使用 [] 获取不存在的key 会报错
    try:
        print(dict2['abc'])
    except BaseException:
        print('key 不存在')

    # 使用 get() 则不会
    print(dict2.get('abc'))         # None

    # 使用get() 可以设置默认值
    print(dict2.get('abc', 'default_value'))

    # 使用对象属性的方式
    # print(dict2.abc)  发生异常，不能用这种方式调用

def test3():
    # 修改字典的value
    dict2['age'] = 25
    print(dict2)

def test4():
    # 删除字典的元素
    del dict2[1]
    print(dict2)

# 5.也可以通过pop删除
def test5():
    d1 = {'a': 1, 'b': 2, 'c': 3}
    print('删除前:', d1)
    d1.pop('b')
    print('删除后:', d1)

# 6. 使用循环获取dict元素
def test6():
    dict3 = {'name': 'chason', 'age': 20, 'score': 90.5}
    for key in dict3:
        print(key)

# set
def test7():
    s1 = {1, 2, 3} # 创建一个set
    print(s1)

# 8 set会自动过滤重复元素
def test8():
    s2 = {1, 2, 3, 2, 1}
    print(s2)  # {1, 2, 3}

# 9. 使用 add() 和 remove() 添加或删除元素
def test9():
    s3 = {'a', 'b', 'c'}
    print(s3)
    s3.add('m')     # 添加元素的位置不是有序的
    print(s3)
    s3.remove('m')
    print(s3)

# 10 set 因为不重复元素 可以做交并补
def test10():
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

if __name__ == '__main__':
    # test1()
    # test2()
    # test2_1()
    test3()
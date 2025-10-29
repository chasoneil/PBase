#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from collections import namedtuple


# collections 是python中的一个内建的集合类，包含多种数据结构

# namedtuple 用来自定义 tuple对象，可以规定元素个数，同时可以用属性而不是索引来获取数据
def demo1():
    # 第一个参数是对象名
    # 第二个参数是一个list 参数的个数以及参数名
    # namedtuple('名称', [属性list])
    point = namedtuple('point', ['x', 'y'])

    # 初始化对象
    p = point(1, 2)
    print(p.x, p.y)     # 1 2

    # 因为是源自tuple
    print(isinstance(p, point))    # True
    print(isinstance(p, tuple))    # True

from collections import deque
# deque
# 这个数据结构就是链表，为了解决数组insert 和 delete 过慢的问题
# 他的数据结构是一个双向链表
def demo2():
    q = deque(['a', 'b', 'c'])
    print(q)
    print(type(q))
    # deque 的 append 和 pop 效率较高
    q.append('x')
    q.appendleft('y')
    print(q)
    q.pop()
    q.popleft()
    print(q)

from collections import defaultdict
# defaultdict
# 使用dict 如果key 不存在 则会出现keyError
# defaultdict用来解决这个问题
def demo3():
    # 构造函数需要传入一个工厂函数指定默认值
    dd = defaultdict(lambda :'default_value')
    dd['k'] = 'v'
    print(dd['k'])
    print(dd['k1'])

# OrderedDict
# 这是一个key有序的dict
from collections import OrderedDict
def demo4():
    # 普通dict
    d = dict({3 :'a', 1:'m', 2: 'c'})
    print(d)
    # OrderedDict 的有序是指按照key的插入顺序，而不是排序
    od = OrderedDict({3 :'a', 1:'m', 2: 'c'})
    print(od)

# ChainMap      todo
# Counter       todo

if __name__ == '__main__':
    # demo1()
    # demo2()
    # demo3()
    demo4()
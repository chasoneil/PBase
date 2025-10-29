#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# python 中常见的内建模块
# datetime 模块中还有个datetime类
from datetime import datetime

def demo1():
    # 获取当前日期和时间
    now = datetime.now()
    print(now)      # 2025-10-29 14:12:10.498266
    print(type(now))

# 构建指定的日期时间对象
def demo2():
    # 参数还可以定义到毫秒
    dt = datetime(2025, 10, 30, 12, 34, 25)
    print(dt)
    print(type(dt))

# datetime 和 timestamp 的互相转换
def demo3():
    date = datetime(2025, 8, 27, 8,0, 0)
    date_ts = date.timestamp()
    print(date_ts)              # python中的时间戳的默认单位是秒
    print(type(date_ts))        # <class 'float'>

    # 时间戳转 datetime
    dt = datetime.fromtimestamp(date_ts)
    print(dt)

# 字符串和datetime的互相转化
def demo4():
    # 字符串转 datetime 注意和Java区别字符串格式化的大小写
    dt = datetime.strptime('2025-10-12 08:17:20', '%Y-%m-%d %H:%M:%S')
    print(dt)

    # datetime 转 str
    now = datetime.now()
    s = now.strftime('%Y-%m-%d %H:%M:%S')
    print(s)

# datetime 的计算
# 计算需要导入 timedelta
from datetime import timedelta

# 可以直接使用 + - 去做时间的计算
def demo5():
    now = datetime.now()

    # 10个小时之前的时间
    t1 = now - timedelta(hours=10)
    print(t1)

    # 3天之后
    t2 = now + timedelta(days=3)
    print(t2)

    # 一个半小时后
    t3 = now + timedelta(hours=1, minutes=30)
    print(t3)

# 本地时间和utc时间的转化
# utc时间表示世界标准时间 需要导入timezone

from datetime import timezone

def demo6():
    # 创建时区
    tz = timezone(timedelta(hours=8))     # UTC+8:00
    now = datetime.now()
    print(now)

# 其他timezone todo

if __name__ == '__main__':
    # demo1()
    # demo2()
    # demo3()
    # demo4()
    # demo5()
    demo6()
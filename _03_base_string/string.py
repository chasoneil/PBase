#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# String 字符串
# 1. 字符串分割  slice
# 2. 常见的字符串函数 len()
# 3. 字符串输出格式化的两种方式
# 4. 字符和unicode的转化 ord() chr()
#    搞清楚编码中 ascii unicode utf8之间的关系
# 5. 字符和字节的转换  encode() decode()


# 字符串切割
str = "0123456789"

print('从0-5:', str[0:5]) # 切割从第0个开始到第5个结束的字符串
print('可以省略最初的0:', str[:5])

print('从5-end:', str[5:]) # 切割从第5个开始到最后的字符串

print('0-end,每隔2个:', str[::2]) # 切割从第0个开始到最后的字符串，每隔2个取一个

# 切割从最后一个开始到第一个结束的字符串，步长为-1
# 步长-1表示全量保存
print('0-end,步长为-1:', str[::-1])

print('01------------------------\n')

# 常见的字符串函数
name = 'chason'
print('name length:', len(name)) # 获取字符串长度

print('02------------------------\n')

# 字符串格式化:
# 方法1：使用 % 进行指定拼接，如果有多个数据，需要用()括起来

print('%s %s' %('Hello', 'python'))
print('Hello, My name is %s, my score is: %d' % ('chason', 100))
print('My name is: %s' % 'fox')

# 对浮点类型的格式化做要求
print('%.2f' % 3.1415)  # result: 3.14

# 方法二: format()
print('Hello, My name is:{0}, my score is: {1:.2f}'.format('chason', 99.8887))

print('03------------------------\n')

# 4. 字符和 unicode之间的转化
# 使用 chr() 实现 unicode -> 字符
# 使用 ord() 实现 字符 -> 整数

a = '中'
print('\'中\'的unicode:', ord(a))

b = 'x'
print('x的unicode:', ord(b))

print('20013的字符:', chr(20013))
print('120的字符:', chr(120))

print('04------------------------\n')

# 5. 字符和字节的转化 encode() decode()
# 注意byte类型需要以b开头 b'xxxx'
str = '中文'
print('中文->bytes:', str.encode('utf-8'))
print('解码成中文:', b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))
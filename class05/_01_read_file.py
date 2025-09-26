#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 使用python读取文件
# IO操作是非常常见的操作

print('1.使用只读的方式读取一个本地文件')
print("1.1 读取文件所有内容:")

# 默认的解码方式是 gbk,中文会报错
f = open("test1", "r", encoding="utf-8")
content = f.read()
print(content)
f.close()

print("1.2 读取文件一行内容:")
f = open("test1", "r", encoding="utf-8")
# 这里不能使用原来的f, 可能是因为读取的指针已经结束了
content_line = f.readline() # 就算是readline() 编码也是要一致的
print(content_line)
f.close()

print("1.3 按行读取文件所有内容，并返回list:")
f = open("test1", "r", encoding="utf-8")
content_list = f.readlines()
print(content_list)
f.close()

print("1.4 一个正常的文件读取流程:")
try:
    f = open("test1", "r", encoding="utf-8")
    # 文件读取的其他操作
    print("读取文件内容")
finally:
    if f:
        f.close()

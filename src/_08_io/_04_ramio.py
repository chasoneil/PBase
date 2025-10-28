#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 内存

from io import StringIO
from io import BytesIO

# 常见的字符串内存IO
def demo1():
    f = StringIO()
    f.write('good morning')
    print(f.getvalue())

# 另外一种使用内存文件的方式
def demo2():
    # 无论如何都是需要先初始化
    f = StringIO("Hello\nPython")

    # 这种方式也是python读取文件的常见方式
    while True:
        l = f.readline()
        if l == '':
            break
        print(l.strip())

# 如果要操作的数据不是字符串而是二进制，则需要bytesIO
def demo3():
    f = BytesIO()
    f.write("你好".encode('utf-8'))
    print(f.getvalue())

def demo4():
    f = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
    res = f.read()
    print(res)                  # b'\xe4\xb8\xad\xe6\x96\x87'

if __name__ == '__main__':
    # demo1()
    # demo2()
    # demo3()
    demo4()
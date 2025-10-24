#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 文件io
def demo1():
    f = open("test.txt", "r")  # read only
    print(f.name)  # print file name
    print(f.mode)  # file mode
    # we use close() to close file
    f.close()

# 读取文件内容
def demo2():
    f = open("test.txt", "r")
    content = f.read(10)  # 读取前10个字符
    print("10 characters:", content)
    f.close()


# 读取文件全部内容
def demo3():
    f = open('test.txt', 'r')
    content = f.read()
    print(content)
    f.close()

# 按行读取文件
def demo4():
    f = open('test.txt', 'r')
    line = f.readline()
    while line:
        print('line:', line, end = "")
        line = f.readline()
    f.close()

# 另外一种按行读取文件的方式
# strip() : 类似于Java中的trim() 移除字符串头和尾的指定字符，默认是空格
def demo5():
    f = open('test.txt', 'r')
    for l in f:                 # 可以直接从文件中通过 for in 或去每行的数据
        l = l.strip()
        print(l)
    f.close()

# 一个正常读取文件的流程 try except finally
def demo6():
    global f
    try:
        f = open('test.txt', 'r')
        for l in f:
            l = l.strip()
            print(l)
    except FileNotFoundError as e:
        print('文件不存在:', e)
    finally:
        if f:
            f.close()

# 使用with 解决编码过于繁琐的问题
# 使用with 则不用调用 close
def demo7():
    with open('test.txt', 'r') as f:
        for l in f:
            l = l.strip()
            print(l)

# 最后一种按行读取的方法 readlines
# readlines() 是一次性读取所有内容并返回 list
def demo8():
    with open('test.txt', 'r') as f:
        for line in f.readlines():
            print(line.strip())


# 有时候读取的文件是个二进制，那么读取的模式使用 rb b表示二进制即可
def demo9():
    with open('demo.jpg', 'rb') as f:
        for l in f.readlines():
            print(l.strip())                # 读出来的都是二进制


# 读取文件，注意编码问题
def demo10():
    try:
        f = open("test1.txt", 'r')
        content = f.read()
        print(content)
    except UnicodeDecodeError as e:
        # UnicodeDecodeError: 'gbk' codec can't decode byte 0x99 in position 86: incomplete multibyte sequence
        print('发生错误:', e)
    finally:
        if f:
            f.close()

# 指定字符编码
def demo11():
    with open('test1.txt', 'r', encoding='utf-8') as f:
        print(f.read())

# 指定字符编码的时候，如果遇到异常，忽略
# 会忽略异常，但是输出中文和日语会变乱码
def demo12():
    with open('test1.txt', 'r', encoding='gbk', errors='ignore') as f:
        print(f.read())

    # UnicodeDecodeError: 'gbk' codec can't decode byte 0x99 in position 54: incomplete multibyte sequence
    with open('test1.txt', 'r', encoding='gbk') as f:
        print(f.read())

if __name__ == '__main__':
    # demo1()
    # demo2()
    # demo3()
    # demo4()
    # demo5()
    # demo6()
    # demo7()
    # demo8()
    # demo9()
    # demo10()
    # demo11()
    demo12()


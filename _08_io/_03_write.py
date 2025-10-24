#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 写文件 主要使用write()
# w 模式文件会直接覆盖
def demo1():
    with open('py.txt', 'w') as f:
        f.write('good morning')
        f.write('早上好')              # 直接写中文会乱码  且没有换行
        f.close()

# 追加写入文件的方式 aw
def demo2():
    with open('py.txt', 'w', encoding='utf-8') as f:
        f.write("Hello python\n")
        f.close()

    # 以追加的方式写入
    with open('py.txt', 'a') as f:
        f.write("Nice to meet you\n")
        f.close()

if __name__ == '__main__':
    # demo1()
    demo2()
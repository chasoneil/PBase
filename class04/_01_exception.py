#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 错误、异常和调试

import logging
logging.basicConfig(level=logging.INFO)

# 1. try-except block for specific exception
def demo1():
    try:
        x = 10/0
        print(x)
    except ZeroDivisionError:
        print("Error: division by zero")

# 2. 收集多个异常
def demo2():
    try:
        a = 10 / 0
        print(a)
    except ZeroDivisionError as e:
        print('0 不能作为除数.')
    except ValueError as e:
        print('发生 value error.')

# 收集多个异常的时候，如果直接写异常也是可以的，但是，不写 as e 就没法获取具体的异常信息
def demo2_1():
    try:
        a = 10 / 0
        print(a)
    except ZeroDivisionError:
        print('error 1')
    except ValueError:
        print('error 2')

# 3. catch all exception
def demo3():
    try:
        a = 10 / 0
        print(a)
    except BaseException as e:  # 所有的异常都来自 BaseException
        print("Error: your code caught exception")

# 4. try except finally
def demo4():
    try:
        x = 10 / 0
        print(x)
    except ZeroDivisionError as e:
        print("Error: division by zero")
    finally:
        print("finally...")

# 5. try-except-else
def demo5():
    try:
        print("do try")
    except BaseException:
        print("caught except.")
    else:
        print("no except.")

# 6. 抛出异常
# python 中使用raise 关键字抛出异常
def demo6(level):
    if level < 1:
        raise Exception("level is under 1!")
    print("level:", level)

# 7. python 内置的logging 模块可以打印错误


def foo(s):
    return 10 / int(s)

def demo07():
    try:
        foo('0')
    except Exception as e:
        logging.exception(e)

# ------------------------------------------

# 调试

# 1. 使用断言代替 print()
# 虽然断言比print也好不到哪去，但是python解释器可以通过 -O 参数去掉
def tmp1(s):
    n = int(s)
    assert n != 0, 'n is not 0'
    print('after')

# 2. logging
# 要注意当我们使用日志级别的时候，我们需要给日志配置级别
def tmp2(s):
    n = int(s)
    logging.info('n = %d' % n)
    print('after')

if __name__ == '__main__':
    # demo1()
    # demo2()
    # demo2_1()
    # demo3()
    # demo4()
    # demo5()
    # demo6(0)
    # demo07()
    # print('END')  # 还是还会被执行

    # tmp1('0')
    tmp2('0')



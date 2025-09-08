#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 错误、异常和调试
# 1. try except finally
# 2. 同时抓取多个异常
#

# 1. try-except block for specific exception
print('1.1 使用try except抓取指定异常:')
def demo1():
    try:
        x = 10/0
        print(x)
    except ZeroDivisionError:
        print("Error: division by zero")

demo1()

print('1.2 抓取多个异常:')
def demo2():
    try:
        a = 10 / 0
        print(a)
    except ZeroDivisionError as e:
        print('0 不能作为除数.')
    except ValueError as e:
        print('发生 value error.')

demo2()

print('1.3 抓取所有异常')
# 3. catch all exception
def demo3():
    try:
        a = 10 / 0
        print(a)
    except BaseException as e:  # 所有的异常都来自 BaseException
        print("Error: your code caught exception")

demo3()

print('1.4 try catch finally')
# 4. try except finally
def demo4():
    try:
        x = 10 / 0
        print(x)
    except ZeroDivisionError:
        print("Error: division by zero")
    finally:
        print("finally...")

demo4()

# 5. try-except-else
print('1.5 try except else')
def demo5():
    try:
        print("do try")
    except:
        print("caught except.")
    else:
        print("no except.")

demo5()

# 6. throw exception
# python 中使用raise 关键字抛出异常
print('1.6 抛出异常')
def demo6(level):
    if level < 1:
        raise Exception("level is under 1!")
    print("level:", level)

# demo6(0)

# 7. python 内置的logging 模块可以打印错误
print('1.7 使用logging收集异常信息')
import logging

def foo(s):
    return 10 / int(s)

def demo07():
    try:
        foo('0')
    except Exception as e:
        logging.exception(e)

demo07()
print('END') # 还是会被执行


#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 这是一个python module, 可以将方法写在里面

def print_info(name, age):
    print("name:", name, end = " ")
    print("age:", age)

def add(a, b):
    return a+b

# 以 _ 或者 __ 开头的就是不应该直接获取的变量
_name = 'chason'
_password = '123456'

# private 的方法
def _get_ori_pwd():
    return _password

def get_pwd():
    pwd = _get_ori_pwd()
    return pwd + '123'

#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# python 单元测试

# 案例： 编写一个 Dict类 这个类的作用和 dict 一样
# 通过单元测试来验证

# 为了执行测试 需要引入 unittest

import unittest

from mydict import Dict

# 创建测试案例
class test_dict(unittest.TestCase):

    def test_init(self):
        d = Dict(a=1, b='test')
        self.assertEqual(d.a, 1)    # 通过类似断言的方式
        self.assertEqual(d.b, 'test')
        self.assertTrue(isinstance(d, dict))

    def test_key(self):
        d = Dict()
        d['k'] = 'v'
        self.assertEqual(d['k'], 'v')
        self.assertEqual(d.k, 'v')          # 对象才有的获取key的方式

    def test_keyError(self):
        d = Dict()
        with self.assertRaises(KeyError):
            value = d['empty']

    def test_attrError(self):
        d = Dict()
        with self.assertRaises(AttributeError):
            value = d.empty

    # setUp() tearDown()  定义了该方法，每个测试开始和结束的时候都会执行
    # 和 junit 中的 @before @after差不多
    def setUp(self):
        print('before test...')

    def tearDown(self):
        print('after test...')


if __name__ == '__main__':
    unittest.main()


# 单元测试可以通过参数的方式只执行某个案例 或者执行某些案例



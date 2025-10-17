#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Dict(dict):
    def __init__(self, **kw):
        super().__init__(**kw)

    # 通过重写 dict 中的方法来实现我们自己的功能
    def __setattr__(self, key, value):
        self[key] = value

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError('Dict has no attribute %s' % key)
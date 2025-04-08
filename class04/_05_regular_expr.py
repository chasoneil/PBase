# python regular expression

# 1. use module 're'

import re

# use match to match same string from a string
# match(pattern, string, flag)
# pattern: regular expression
# string: all content
# flag : for other requirement
def demo01():
    print(re.match('www', 'www.baidu.com'))
    print(re.match('com', 'www.baidu.com'))

demo01()
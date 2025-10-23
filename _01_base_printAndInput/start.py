# 运行第一个python程序
# python 支持交互式编程

print("Hello python!")
print("你好，Python") # 注意中文的编码

print("01-----------------------")

# python可以在一行中写多个语句，语句之间用;隔开
print("Hello");print("Python")

print("02-----------------------")

#python是一个很讲究缩进的语言
if True:
    print("True")
else:
    print("False")
  #print("haha")  如果缩进不对，编译器会提示， 运行会弹出 IndentationError

print("03-----------------------")

#python的拼接和C类似 都是使用 \ 进行行的拼接

item_one = 1
item_two = 2
item_three = 3

total = item_one + \
        item_two + \
        item_three

print(total)
print("04-----------------------")

# python 中 单引号，双引号 三引号都可以表示字符串 ，三个双引号还能表示多行注释

'''
多行注释方法1
'''

"""
多行注释方法2
"""

word1 = 'p1'
word2 = "p2"
word3 = """p3
p4"""

print(word1)
print(word2)
print(word3)
print("05-----------------------")




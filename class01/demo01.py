# 1. 单行注释与多行注释
# 2. 变量赋值 变量不用声明，直接赋值
# 3. 使用缩进代替代码块
# 4. 多行语句代码拼接

'''
多行注释方法1
'''

"""
多行注释方法2
"""

# 变量赋值 没有数据类型，同一个变量可以赋值不同类型的数据
a = 10
b = 20
c = a + b
print(c)
print("=========================")

a = "Hello, python!"
print(a)

# 多变量赋值
x, y, z = 10, 20, "python"
print(x, y, z)


# 缩进代替代码块
if c > 10:
    print("c is greater than 10")
else:
    print("c is less than or equal to 10")


# 多行语句代码拼接
str = "This is first line;" + \
      " This is second line;" + \
      " This is third line;"
print(str)
# 1. python 的 print
# 2. python 的用户输入 input
# 3. python 的数据类型
# 4. 逻辑运算符

# print 中使用逗号可以分别输出多个字符串 遇到,会补充一个空格
print('Hello', 'Python', 'Over')   # result: Hello Python Over

print('1 + 2 =', 1+2)

print('01----------------------')

# 使用input获取用户输入，回车结束
name = input()
print('Hello', name)

# 也可以在input中加入提示词
name = input('Please input your name:')
print('Hello', name)

print('02----------------------')

# python的数据类型： 整数 浮点数 字符串 布尔 空值
x = 10  # 整数
print('x =', x)

pi = 3.14
print('pi = ', pi)

# python 中使用 '' / "" / ''' '''/ 来表示字符串
print('single str')
print("double str")
print('''long
str''')

print('I\'m Chinese')  # 有些字符需要转义

print(r'\\\\t1')  # 使用 r可以让转义失效

print('03----------------------')

# python 中的布尔值是 True False
if True:
    print(True)
else:
    print(False)

# python中使用None表示空值

print('04----------------------')

# python 中使用and or not来代表与或非

if True and True:
    print('double true')

if True or False:
    print('has true')

if not True:
    print('not true')
else:
    print('not false')
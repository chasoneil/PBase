# python 中怎么定义一个方法
# python 中使用 def 定义一个方法

# 带有return
def add(a, b):
    return a+b

# 不带return的方法
def fun(a, b):
    if a > b:
        print("a > b")
    else:
        print("a < b")

a = 10
b = 5
c = add(a, b)
print(c)
# 输出： 15

fun(a, b)
# 输出： a > b
print("------------------------------")

# ----------------------------------------

# python 中向函数传递参数
# 1. 正常传递，按照位置一一对应

def fun2(m, n, k):
    if m > n:
        if m > k:
            print("最大值是:", m)
        else:
            print("最大值是:", k)
    elif n > m:
        if n > k:
            print("最大值是:", n)
        else:
            print("最大值是:", k)

m ,n, k = 1, 2, 3
fun2(m, n , k)

# 2. 使用变量名的方式传递参数
# 这种情况下是一个改变参数的顺序的

def fun3(str, name):
    print("str:", str, end=" ")
    print("name:", name)
    return 0

fun3("abc", "fox")
fun3(str = "bca", name = "fox1")
fun3(name = "json", str = "aaa")

'''
输出:
str: abc name: fox
str: bca name: fox1
str: aaa name: json
'''

print("------------------------------")

# --------------------------------
# 3. 给函数的参数增加默认值

# 如果没有给age, 那么默认就是18
def print_info(name, age = 18):
    print("name:", name, end = " ")
    print("age:", age)

print_info("张三")
print_info("李四", 20)
print_info(name = "王五")

'''
name: 张三 age: 18
name: 李四 age: 20
name: 王五 age: 18
'''
print("------------------------------")
# --------------------------------

# 4. 不定长参数，当你不知道需要几个参数的时候可以使用
def auto_len(*args):
    print("args:")
    for arg in args:
        print(arg, "," ,end=" ")
    return

auto_len(1, 2, 3)
# 1 , 2 , 3 ,

print()
print("------------------------------")
# --------------------------------
# 5. 匿名函数 （lambda）
# 匿名函数格式一致，只能通过lambda实现
# sum 是一个变量，变量名变成了函数名
sum = lambda arg1, arg2 : arg1 + arg2
print(sum(10, 20))
# 30


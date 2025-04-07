# 1. 列表 -> [] 列表中的元素可以是不同的类型
# 2. 元组 -> () tuple 元组和列表类似，区别是元组的元素不可以更改

# -------- 列表 ---------
# python的列表可以定义不同类型的数据
mylist = ["abc", 10, 20.3, True]
print(mylist)  # 输出整个列表
print(mylist[0]) # 输出列表的第一个元素

# 列表的元素可以更改
mylist[0] = "bca"
print(mylist)

# 列表支持拼接操作
list1 = [1, 2, 3]
list2 = [4, 5, 6]
print(list1 + list2)

# 获取列表的长度 len()
length = len(list1)
print("list1 length:",length)

print("-----------------------")

# -------- 元组 ---------
mytuple = ("abc", 2, 10.6, False)
print(mytuple)
print(mytuple[0])

# 元组的定义不需要()也可以
tuple1 = 1, 2, 3
print(type(tuple1))

# 创建一个空元组
tuple2 = ()
print("tuple2 length:", len(tuple2))

# 创建一个只有一个元素的元组
tuple3 = (1,) # 注意末尾的逗号
print("tuple3 length:", len(tuple3))

# get tuple length
t_len = len(mytuple)
print("tuple length:", t_len)

# 元组的元素不能更改
mytuple[0] = "bca" # 异常
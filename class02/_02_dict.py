# 字典 python中的字典 等同于 HashMap 或者 Hashtable 
# 使用 key-value 形式存储数据，key 必须是不可变对象，value 可以是任意对象 

# 创建字典
dict1 = {}
print(dict1)

# 字典可以对象存储
dict2 = {"name":"chason", "age": 20, 1: 20} # key 必须是不可变对象 字符串数字等都是不可变对象
print(dict2)
print("dict2 length:", len(dict2))  # 字典长度是一个键值对算一个

# 通过key获取value
print(dict2['name'])

# 修改字典的value
dict2['age'] = 25
print(dict2)

# 删除字典的元素
del dict2[1]
print(dict2)

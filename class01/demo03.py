# 1. list

# list 是一个数组， python中使用[] 来表示一个数组
classmates = ['zhangsan', 'lisi', 'wangwu']
print(classmates) # print : ['zhangsan', 'lisi', 'wangwu']

# python 支持数组元素不是相同类型
my_list = ['chason', 18, 87.12, 'abc']
print(my_list)

# 使用len() 获取数组长度
print('my_list len:',len(my_list))

print('01 ----------------------')
# 使用下标获取数组的元素
print(my_list[0])
print(my_list[1])
print(my_list[2])
print(my_list[3])

print('02 ----------------------')
# 你可以使用负数用来从尾部获取元素
print(my_list[-1])
print(my_list[-2])

print('03 ----------------------')
# 向数组的结尾添加元素 append
my_list.append('yyy')
print(my_list[-1])

print('04 ----------------------')
# 在数组的指定位置插入元素 insert
my_list.insert(1, 'xxx')

print(my_list[0])
print(my_list[1])
print(my_list[2])
print(my_list[3])
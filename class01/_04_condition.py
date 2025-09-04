# 1. condition
# 所有的条件判断都是if else
# 2. 输入的数据类型的转换
# 3. 装配模式 类似于java中的switch

age = 10
if age > 10:    # 注意格式
    print('大人啦')
else:
    print('还是孩子')

# 多个条件中 使用elif

age = 18
if age < 0:
    print('年龄错误')
elif age >=0 | age < 10:
    print('还是孩子')
else:
    print('大人啦')

print('01 ----------------------')

age = input('请输入年龄:')   # 默认获取的类型是字符串类型
rage = int(age)
if rage < 18:
    print('未满18岁')
else:
    print('已满18岁')

print('02 ----------------------')

score = 'b'

match score:
    case 'a':
        print('level a')
    case 'b':
        print('level b')
    case 'c':
        print('level c')
    case _:                     # 表示匹配到其他的任意值
        print('unknown level')

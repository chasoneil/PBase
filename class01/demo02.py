# 1. String 字符串

# 字符串切割
str = "0123456789"
print(str[0:5]) # 切割从第0个开始到第5个结束的字符串
print(str[5:]) # 切割从第5个开始到最后的字符串
print(str[:5]) # 切割从第0个开始到第5个结束的字符串
print(str[::2]) # 切割从第0个开始到最后的字符串，每隔2个取一个
print(str[::-1]) # 切割从最后一个开始到第一个结束的字符串，步长为-1

print('01------------------------')

# 常见的字符串函数
name = 'chason'
print('name length:', len(name)) # 获取字符串长度

print('02------------------------')

# 字符串格式化: 使用 % 进行指定拼接，如果有多个数据，需要用()括起来
print('Hello, My name is %s, my score is: %d' % ('chason', 100))

print('My name is: %s' % 'fox')

print('%.2f' % 3.1415)  # result: 3.14

print('03------------------------')

# 字符串的第二种的格式化 format

print('Hello, My name is:{0}, my score is: {1:.2f}'.format('chason', 99.8887))
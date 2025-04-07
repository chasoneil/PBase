# 1. String 字符串类型

# python中 单引号 = 双引号
str1 = 'Hello, python1'
str2 = "Hello, python2"
print(str1)
print(str2)

# \表示转义符
str3 = "Hello, \n python3"
print(str3)

# r 表示让转义符失效，例如下面的\n会直接输出
str4 = r"Hello, \n python4"
print(str4)

# 使用 + 做字符串拼接 使用 * 做重复拼接
str5 = "Hello, "
str6 = "python"
print(str5 + str6)
print(str6 * 2)

# 字符串切割
str = "0123456789"
print(str[0:5]) # 切割从第0个开始到第5个结束的字符串
print(str[5:]) # 切割从第5个开始到最后的字符串
print(str[:5]) # 切割从第0个开始到第5个结束的字符串
print(str[::2]) # 切割从第0个开始到最后的字符串，每隔2个取一个
print(str[::-1]) # 切割从最后一个开始到第一个结束的字符串，步长为-1
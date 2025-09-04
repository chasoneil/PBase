# 1. for in 循环
# 2. while 循环

list1 = [1, 2, 3]
for ele in list1:   # 循环获取元组中的元素
    print(ele)

print('01 ----------------------')
sum = 0
for ele in [1, 2, 3, 4, 5]:
    sum += ele

print('1-5的和:', sum)

print('02 ----------------------')

# python 通过 range() 生成整数序列
# 例如 range(100) 生成1 - 99的整数序列 等同于 [0, 1, 2, ... 99]

sum = 0
for ele in range(101) :
    sum += ele
print('1-100求和:', sum)
print('03 ----------------------')

sum = 0
i = 1
while i < 100:
    sum += i
    i = i+2

print('1-100以内的奇数和:', sum)
print('04 ----------------------')

# break 和 continue 的用法和java类似，不再举例













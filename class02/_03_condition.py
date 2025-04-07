# python 条件语句

# 1. 常见的条件语句
num = 18
if num < 0:
    print("年龄不能为负数")
elif num <= 18:
    print("你还未成年")
else:
    print("你已经成年了")

# 你还未成年

print("----------------------------")

# 2. python 3.10+ 支持match case 这样的写法
# 相当于 switch case

http_status = 404
match http_status:
    case 0:
        print("0")
    case 1:
        print("1")
    case _:
        print("other")

# other

print("----------------------------")


# 3. if statement multiple conditions

num = 10

if num >= 0 and num <= 100: # use 'and' connect the statement
    print("good number!")
else:
    print("bad number!")

# if you have only one statement, you can write it in one line.

if num > 5: print("number is upper 5")

# good number!
# number is upper 5
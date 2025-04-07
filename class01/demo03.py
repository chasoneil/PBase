# 1. 等待用户输入

# 先输出两个空行，然后等待用户输入

num = input("Press Enter a number.")
num = int(num)
if num > 0:
    print("number > 0")
else :
    print("number < 0")
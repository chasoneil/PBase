# python 中的循环

# Note: python apply for and while to do circle statements
# no 'do ... while' grammar

# 1. while

num = 1
while num < 10:
    num += 2
    print("num:", num)

# num: 3
# num: 5
# num: 7
# num: 9
# num: 11

print("---------------------------")

# 2. while else
num = 3
while num < 5:
    print("number < 5")
    num += 1
else:
    print("number > 5")

# number < 5
# number < 5
# number > 5

print("---------------------------")


# for
# statement for xxx in xxx

fruits = ['apple', 'banana', 'orange']
for fruit in fruits:
    print(fruit)

# apple
# banana
# orange

# range(start, end) means get from start to end
for num in range(3, 5):
    print(num)

# 3
# 4
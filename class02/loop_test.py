# python 循环测试

# range(a, b) 表示生成 [a, b) 的整数序列
# range(m) 表示生成 [0,m) 的整数

# 1. 模仿其他语言的for循环

print(range(5))         # range(0, 5)

def test_range():
    for i in range(10):     # 从 [0, 10) 等同于 (i=0; i<10; i++)
        print(i)

# 使用 python 编写一个选择排序的算法

def select_sort(list):
    if len(list) < 2:
        return

    length = len(list)
    for i in range(length):
        min_index = i
        for j in range(i, length):
            if list[j] < list[min_index]:
                min_index = j
        swap(list, i, min_index)

def swap(list, x, y):

    if x == y:
        return

    temp = list[x]
    list[x] = list[y]
    list[y] = temp


def test():

    list = [2, 1, 3, -1, 0, 6]
    select_sort(list)
    print(list)

test()

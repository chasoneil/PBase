# 1. list -> [] the element in the list are multiple
# 2. tuple -> () tuple 元组和列表类似，区别是元组的元素不可以更改

# -------- list ---------
# multiple data type
mylist = ["abc", 10, 20.3, True]
print(mylist)  # print all list elements
print(mylist[0]) # print single element

# you can modify the element in list
mylist[0] = "bca"
print(mylist)

print("----------------------------")

list1 = [1, 2, 3, 4, 5, 6]
list2 = [7, 8, 9]
# print index from start to end
print(list1[1: 5])
# list add: elements contains to one list
list3 = list1 + list2
print(list3)

print("----------------------------")

# get length -> len()
length = len(list1)
print("list1 length:",length)

print("-----------------------")

# modify list
list = []
print(list)
list.append("ele1")
list.append("ele2")
print(list)

print("-----------------------")

# delete list element
list4 = [1, 2, 3, 4]
print(list4)
del list4[2] # del 3
print(list4)

print("-----------------------")

# use loop to get every element from list

list5 = [1, 2, 3, 4, 5]
for num in list5:
    print(num)
print("-----------------------")

# ======================== tuple  ============================
# tuple support multiple elements
mytuple = ("abc", 2, 10.6, False)
print(mytuple)
print(mytuple[0])

# define tuple without ()
tuple1 = 1, 2, 3
print(type(tuple1))
print(tuple1)

print("-----------------------")

# create empty tuple
tuple2 = ()
print("tuple2 length:", len(tuple2))

# create one element tuple
tuple3 = (1,) # , is needed
print("tuple3 length:", len(tuple3))
print(tuple3)

print("-----------------------")

# get tuple length
t_len = len(mytuple)
print("tuple length:", t_len)

print("-----------------------")
tuple4 = (1, 2, 3, 4, 5)
print(tuple4[1: 3]) # print some elements like list

tuple5 = (6, 7)
print(tuple4 + tuple5)

print("-----------------------")

tuple6 = ()

try:
    tuple6.append("a") # exception
    print(tuple6)
except:
    print("tuple append caught error!")

try:
    mytuple[0] = "bca" # can not modify tuple element
except:
    print("modify tuple caught error!")

print("-----------------------")

tuple7 = (3, 2, 1)
for t in tuple7:
    print(t)

print("-----------------------")

tuple8 = (3, 2, 1)
try:
    del tuple8[1]
except TypeError:
    print("tuple delete exception!")

# 1. print 输出的换行与不换行
# 2. 模块和方法的导入


# 正常的print输出是会换行的
print("line 1")
print("line 2")

# 如果期望不换行 需要使用end=" " 
print("line 1", end=" ")
print("line 2")
print("---------------------")


# 导入一个模块使用import moduleName
import sys

sys.stdout.write("Hello, world!\n")

# 导入一个模块中的方法 from moduleName import functionName

from sys import argv,path

# 如果导入的是sys 那么这里的写法是sys.path 而不是path
print("path:", path)
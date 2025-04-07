# 这是python的主函数，我们可以在这里引入其他的文件

# 1. 导入一个模块
# 正常导入的模块一般放在顶端
# 这是导入一整个模块
import support1

name = "张三"
age = 18

# 使用模块名.函数名调用
# 如果引入了一个模块，那么这个模块的所有函数你都可以使用
support1.print_info(name, age)
sum = support1.add(3, 2)
print(sum)
# name: 张三 age: 18
# 5

print("------------------------------------")

# 2. 导入一个模块的其中一个函数
from support2 import max

# 这里就不需要使用module.fun,直接使用fun
m = max(3, 2)
print("max:", m)
# max: 3

print("------------------------------------")

# 3. 使用 * 导入一个模块的所有
# 这种也不需要module.fun
from support3 import *
m1 = min(3, 2)
print("min:", m1)

print("------------------------------------")
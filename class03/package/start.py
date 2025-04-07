# 这个是主方法

from pkg1.support1 import fun1
from pkg1.support1 import fun2
from pkg1.support2 import fun2

fun1()
fun2()

# 如果两个文件中出现了一样的方法名，那么上述就后导入的覆盖先导入的
# 下面这种方法在上述导入的时候，是不可以的
# support2.fun2()

# 执行初始化
# Support1 -> fun1
# Support2 -> fun2

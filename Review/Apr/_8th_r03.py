
class Father:

    def __init__(self, name):
        self.name = name
        print("Father construct")

    def toString(self):
        print("[Father Name:", self.name, "]")

    def sleep(self):
        print("Father sleep")

    def work(self):
        print("Father work")

class Son(Father):

    def __init__(self, name):
        print("son construct")

    def sleep(self):
        print("Son sleep earlier")

    def study(self):
        print("son study")

# 当子类没有写构造方法的时候，父类的构造方法被调用
# 当子类自己有构造方法的时候，他就会调用自己的构造方法
s = Son("zhangsan")
s.sleep()
s.work()
s.study()



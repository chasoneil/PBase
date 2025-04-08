# object-oriented 3 extend!

class Parent:

    attr = 0

    def __init__(self, name):
        self.name = name
        print("parent construct method has been invoked!")

    def fun1(self):
        print("parent fun1 has been invoked!")

    def fun2(self):
        print("parent fun2 has been invoked!")

    def getAttr(self):
        return Parent.attr

    def setAttr(self, a):
        Parent.attr = a

# extend
class Son(Parent):

    # if you want to use parent construct, you need add parent parameters
    # super() means use parents
    def __init__(self, age, name):
        super().__init__(name)
        self.age = age
        print("son construct method has been invoked!")

    def fun1(self):
        print("son fun1 has been invoked!")

    def get_age(self):
        print(self.age)

s = Son(18, "chason")
# print("son name:", s.name)
print("son age:", s.age)
s.fun1()

# son use parents method
s.fun2()

# use son to get and set parent's attr
print("parent attr:", s.getAttr())
s.setAttr(2)
print("parent attr:", s.getAttr())


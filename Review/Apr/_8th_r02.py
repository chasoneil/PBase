
class Student:

    def __init__(self, name, id):
        self.name = name
        self.id = id

    def toString(self):
        print("[Student Name:", self.name, "id:", self.id, "]")

    # 该方法在对象被销毁时调用
    def __del__(self):
        print("student", self.name, "destroyed!")

stu = Student("chason", "0001")
stu.toString()

print("-------------------")

name = getattr(stu, 'name')
print("name ->",name)

setattr(stu, 'age', 20)
print("age ->",stu.age)

print(hasattr(stu, 'age'))

delattr(stu, 'age')
print(hasattr(stu, 'age'))
# object-oriented 2

class Student:

    def __init__(self, name, age, id):
        self.name = name
        self.age  = age
        self.id   = id

    def intro(self):
        print("Student Id:", self.id, "Name:", self.name, "Age:", self.age)

    def __del__(self):
        print(self.name," destroyed!")

stu1 = Student("fox", 18, "00001")
stu1.intro()

# object field which we can get from object
n = stu1.name
print("stu1 name:", n)

print("---------------------------")

stu2 = Student("lily", 30, "00013")
stu2.intro()

if stu1.age > stu2.age:
    print("fox older")
else:
    print("lily older")

print("---------------------------")

# 2. use getattr() setattr() delattr() hasattr() to do some attribute operation

stu1_name = getattr(stu1, "name")
print("getattr:", stu1_name)

print("hasattr:", hasattr(stu1, 'age'))

print("setattr:", setattr(stu1, 'classroom', '3A-1')) # None
print(stu1.classroom)

print("delattr:", delattr(stu1, 'classroom'))   # None

print("---------------------------")

# 3. __del__ like java finalize()

print("stu2 id:", id(stu2))
del stu2


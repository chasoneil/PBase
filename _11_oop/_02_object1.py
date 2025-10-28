# python object-oriented

# 1. define a class

class Person:

    # like static in java
    count = 0

    # name, age belongs to Person object not class
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.count += 1

    def introduce(self):
        print("I'm a person. My name is:", self.name, "My age is:", self.age)

    def get_count(self):
        return Person.count

    def print_self(self):
        print(self)

    def print_class(self):
        print(self.__class__)

# how to create an object
p = Person("chason", 18)

p.introduce()
c = p.get_count()
print("count:", c)

print("-------------------------------")

p.print_self()
p.print_class()

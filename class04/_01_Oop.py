#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 面向对象编程，概念和Java类似，通过class定义类

# class + 类名(继承自哪个类)
class Student(object):

    # 类似Java的构造方法
    def __init__(self):
        print('Student __init__')
        pass


# 创建对象
s = Student()

print('01 ------------------------')

# 类包含属性
class Student1(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_msg(self):
        print('name:', self.name, " score:", self.score)

s1 = Student1('chason', 90)
#s2 = Student1() 和 Java 一样，有参构造不能通过午餐的方式进行初始化
s1.print_msg()

# 可以动态给对象增加属性
s1.age = 18
print(s1.age)

print('02 ------------------------')

# 访问限制
# 类似 Java 的 private 类型的变量，不能直接被外界访问，需要提供get set方法
# python 中通过 __ 双下划线的形式实现private
class Student2(object):

    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

fox = Student2('fox', 80)
# print(fox.__name) 报错，获取不到
print(fox.get_name())

print('03 ------------------------')

# 继承和多态是面向对象的三大特性之二

class Animal(object):
    def run(self):
        print('Animal is running.')

# 定义的Dog继承自Animal 和Java中的extend没啥两样
class Dog(Animal):

    def eat(self):
        print('Dog eat bones.')

    def run(self):
        print('dog run very fast!')

dog1 = Dog()
# 子类可以调用父类的方法
dog1.run()  # Animal is running.
dog1.eat()

class Cat(Animal):
    def run(self):
        print("Cat is running, but faster.")

cat1 = Cat()
# 子类可以重写父类的方法
cat1.run()

print('04 ------------------------')
# 判断数据类型

a = list()
print(isinstance(a, list))
print(isinstance(dog1, Dog))

# 子类也是父类的类型
print(isinstance(dog1, Animal))

def run_again(Animal):
    Animal.run()
    Animal.run()

# 多态的作用
run_again(dog1)
run_again(cat1)

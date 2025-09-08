#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 面向对象编程，概念和Java类似，通过class定义类

# class + 类名(继承自哪个类)
print('1. 类和对象:')
print('1.1 创建一个普通类和实例化:')
class Student(object):

    # 类似Java的构造方法
    def __init__(self):
        print('Student __init__')
        pass

# 创建对象
s = Student()
print(s)  # <__main__.Student object at 0x00000122282170E0>


# 类包含属性
print('1.2. 创建带参数的类:')
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
print('1.3. 动态给对象增加属性')
s1.age = 18
print(s1.age)

s2 = Student1('lily', 30)
# print(s2.age)  s2 并没有age属性所以报错 所以只能动态给对象增加属性

print('01 ------------------------\n')


# 访问限制
# 类似 Java 的 private 类型的变量，不能直接被外界访问，需要提供get set方法
# python 中通过 __ 双下划线的形式实现private
print('2. 访问限制:')
print('2.1 通过__来定义private:')
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

# 使用 _开头的类的变量是不推荐直接访问的变量，虽然这个变量可以被直接访问

print('02 ------------------------\n')

# 继承和多态是面向对象的三大特性之二
print('3. 继承和多态:')
print('3.1 继承:')
class Animal(object):
    def run(self):
        print('Animal is running.')

# 定义的Dog继承自Animal 和Java中的extend没啥两样
class Dog(Animal):

    # 子类可以有其他的扩展方法
    def eat(self):
        print('Dog eat bones.')

    # 子类可以重写父类的方法
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

# 判断数据类型
a = list()
print(isinstance(a, list))
print(isinstance(dog1, Dog))

# 子类也是父类的类型
print(isinstance(dog1, Animal))

# 当我们希望传入的类型是Animal， 参数首字母反而小写，方法中也是直接使用 animal
# 这个姑且先当做一种默认的规则遵守 todo
print('3.2 多态:')
def run_again(animal):
    animal.run()
    animal.run()

# 多态的作用
run_again(dog1)
run_again(cat1)

print('03 ------------------------\n')

# 判断对象类型 type()

print('4. 对象类型:')
print('4.1 判断对象类型:')

print(type(12))
print(type('abc'))

class Person(object):

    def __init__(self):
        pass

p = Person()
print(type(p)) # <class '__main__.Person'>

# isinstance()
print('4.2 判断对象是否属于某种类型:')

print(isinstance(p, Person))
print(isinstance([1, 2], (list, tuple)))    # [1, 2] 是list或者tuple

# 使用 dir()
print('4.3 获取对象的所有变量和方法')
print('p(Person)的所有变量和方法:', dir(p))

print('04 ------------------------\n')

# 类属性和对象属性
# 类属性就是属于类的属性 使用类.属性名直接获取
# 类属性可以被对象覆盖，但是类属性依旧保留

print('5. 类属性:')
class User:

    name = 'zhangsan'

    def __init__(self, age):
        self.age = age

user = User(18)
print('user name:', user.name, 'age:', user.age)
print('通过类获取name:', User.name)

user.name = 'lisi'
print('修改 user name:', user.name)
print('修改 user name, 原来类的name:', User.name)

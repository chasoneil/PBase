#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 面向对象编程，概念和Java类似，通过class定义类

# class + 类名(继承自哪个类)

# 1. 类和对象:
# 1.1 创建一个普通类和实例化:
class Student:
    # 类似Java的构造方法
    def __init__(self):
        print('Student __init__')
        pass

# 没有构造方法也是可以的，但是没啥意义
class Person:
    pass

def test1():
    # 创建对象
    s = Student()
    print(s)  # <__main__.Student object at 0x00000122282170E0>

def test1_1():
    p = Person()
    print(p)

# 1.2. 创建带参数的类:
class Student1:
    # 构造方法的第一个参数始终是self
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_msg(self):
        print('name:', self.name, " score:", self.score)

def test2():
    s1 = Student1('chason', 90) # 和 Java 一样，有参构造不能通过无参的方式进行初始化
    s1.print_msg()

    # 可以动态给对象增加属性
    s1.age = 18
    print(s1.age)

    s2 = Student1('lily', 30)
    # print(s2.age)  s2 并没有age属性所以报错 所以只能动态给对象增加属性


# 2. 访问限制
# 类似 Java 的 private 类型的变量，不能直接被外界访问，需要提供get set方法
# python 中通过 __ 双下划线的形式实现private
class Student2:
    def __init__(self, name, score, id):
        self.__name = name          # __ 开头意味这个属性不能直接访问
        self.score = score
        self._id = id

    def get_name(self):
        return self.__name

def test3():
    fox = Student2('fox', 80, '0001')
    # print(fox.__name) 报错，获取不到
    print(fox.get_name())
    # 使用 _开头的类的变量是不推荐直接访问的变量，虽然这个变量可以被直接访问
    print(fox._id)

# 3. 继承和多态是面向对象的三大特性之二
class Animal:
    def run(self):
        print('Animal is running...')

# 定义的Dog继承自Animal 和Java中的extend没啥两样
class Dog(Animal):
    # 子类可以有其他的扩展方法
    def eat(self):
        print('Dog eat bones.')

class Cat(Animal):
    # 子类可以重写父类的方法
    def run(self):
        print('Cat is running...')

def test4():
    dog1 = Dog()
    # 子类可以调用父类的方法
    dog1.run()  # Animal is running.
    dog1.eat()

    cat1 = Cat()
    # 子类可以重写父类的方法
    cat1.run()

def test5():
    dog = Dog()
    # 判断数据类型
    a = list()
    print(isinstance(a, list))
    print(isinstance(dog, Dog))

    # 子类也是父类的类型
    print(isinstance(dog, Animal))

    # 父类不是子类的类型
    a = Animal()
    print(isinstance(a, Dog))   # False

# 多态

# 当我们希望传入的类型是Animal， 参数首字母反而小写，方法中也是直接使用 animal
def run_again(animal):  # 这个姑且先当做一种默认的规则遵守 todo
    animal.run()
    animal.run()

def test6():
    dog = Dog()
    cat = Cat()
    # 多态的作用
    run_again(dog)
    run_again(cat)

# 判断对象类型 type() ininstance
def test7():
    print(type(12))
    print(type('abc'))
    p = Person()
    print(type(p)) # <class '__main__.Person'>

    # 判断对象是否属于某种类型:
    print(isinstance(p, Person))
    print(isinstance([1, 2], (list, tuple)))  # [1, 2] 是list或者tuple

    # 使用 dir() 获取对象的所有变量和方法
    chason = Student2('chason', 80, '0007')
    print('chason(Student)的所有变量和方法:', dir(chason))

    # 使用isinstance() 判断各种类型
    print(isinstance([1, 2], (list, tuple)))        # 是list或者tuple


# 类属性和对象属性
# 类属性就是属于类的属性 使用类.属性名直接获取
# 类属性可以被对象覆盖，但是类属性依旧保留
class User:
    name = 'zhangsan'   # 类的属性 类似于Java中的static
    def __init__(self, age):
        self.age = age

def test8():
    user = User(18)
    print('user name:', user.name, 'age:', user.age)
    print('通过类获取name:', User.name)

    user.name = 'lisi'
    print('修改 user name:', user.name)
    print('修改 user name, 原来类的name:', User.name)

    # 判断是否有属性 hasattr()
    print(hasattr(user, 'age'))

    # 获取对象属性 getattr()
    print(getattr(user, 'age'))     # 18



if __name__ == '__main__':
    # test1()
    # test1_1()
    # test2()
    # test5()
    # test7()
    test8()

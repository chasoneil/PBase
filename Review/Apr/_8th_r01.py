
class Person:

    count = 0

    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex
        print("construct be invoked")

    def work(self):
        if self.sex == 'male':
            print("male work faster")
        elif self.sex == 'female':
            print("female work slower")
        else:
            print("who are you?")

    def to_string(self):
        return 'name:' + self.name + ', age:' + self.age + ', sex:' + self.sex

# 创建实例

print(Person.count)
p = Person("zhangsan", 18, 'male')
print(p) # 输出的是对象实例 <__main__.Person object at 0x1042d9a90>

print("--------------")
# print(p.to_string()) exception
p.work()




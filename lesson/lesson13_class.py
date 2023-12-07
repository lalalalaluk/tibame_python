# # 定義
# class Person:
#     pass

# # 蛇行
# white_pen = 100

# # 小駝峰
# whitePen = 100

# # 大駝峰
# WhitePen = 100


class Person:
    # 初始化
    def __init__(self, name, age=11):
        # 屬性
        self.name = name
        self.age = age

    # 比較
    def __eq__(self, that):
        return self.name == that.name and self.age == that.age

    # 呈現
    def __repr__(self):
        return f"i am {self.name}, i am {self.age} years old"

    # 方法
    def walk(self) -> str:
        # print(f"I walk, i am {self.name}, i am {self.age} years old")
        a = f"I walk, i am {self.name}, i am {self.age} years old"
        return a


p = Person("John", 18)
p.walk()
print(p.name, p.age)
print(p)

l = Person("Lisa")
l.walk()

j = Person("Jack", 15)
j.walk()

# p = Person("John", 18)
# p2 = Person("John", 18)
# print(p == p2)
# print(p.walk())


class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        print(f"{self.name} is walking")

    def run(self):
        print(f"{self.name} is running")

    def jump(self):
        print(f"{self.name} is jumping")


class Dog(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)

    def jump(self):
        print(f"{self.name} is jumping really high")

    def shake_tail(self):
        print(f"{self.name} is shaking tail")


class Cat(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def show_color(self):
        print(f"I am {self.color} cat")


# a = Animal("dog", 5)

# a.walk()
# a.jump()
# a.run()

d = Dog("lucy", 3)

# d.run()
# d.jump()
# d.walk()
# d.shake_tail()

c = Cat("Yoru", 3, "white")

# c.run()
# c.walk()
# c.jump()
# c.show_color()

print(issubclass(Person, Animal))

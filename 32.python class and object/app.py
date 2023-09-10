# python class and object
class Person:
    first_name = "Rejaul"
    last_name = "Karim"
    age = 20


obj = Person()
print(obj.first_name)
print(obj.last_name)
print(obj.age)


# class attributes
class Student:
    def __init__(self, id, name, age):
        self.id = id
        self.name = name
        self.age = age


student01 = Student("10", "Rezaul Karim", "20")
print(student01.name)


# class method
class Per:
    def __init__(self, id, name, age):
        self.id = id
        self.name = name
        self.age = age

    def greet_pre(self):
        print("Hello " + self.name + ", how are you? ")


per = Per(1256564, "kamal mia", 35)
per.greet_pre()

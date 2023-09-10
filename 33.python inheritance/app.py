class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        print(self.name + "walks")


class Dog(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)

    def sound(self):
        print(self.name + " barks")


d = Dog("puppy", 1)
d.walk()
d.sound()

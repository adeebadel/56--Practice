# challenge 1 

class Car:

    def __init__(self, brand):
        self.brand = brand

    def drive(self):
        print(self.brand + " is driving.")


car1 = Car("Toyota")
car1.drive()

#challenge 2 

class Dog:

    def __init__(self, name):
        self.name = name

    def bark(self):
        print(self.name + " says Woof!")


dog1 = Dog("Bruno")
dog1.bark()
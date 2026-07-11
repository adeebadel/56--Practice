class Person:
    
    def walk(self):
        print("waiting")
        
class Student(Person):
    pass
student = Student()
student.walk()

class Animal:
    
    def eat(self):
        print("Eating...")

class Cat(Animal):
    pass

cat = Cat()
cat.eat()

class Device():
    
    def power_on(self):
        print("Power ON")
        
class Phone(Device):
    pass
phone = Phone()
phone.power_on()
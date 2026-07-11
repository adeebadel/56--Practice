class Animal:
    
    def sound(self):
        print("Animal Sound")
        
class Dog(Animal):
    
    def sound(self):
        print("WOOF! WOOF!")
        
dog = Dog()
dog.sound()

#2
class Vehicle:
    def start(self):
        print("vehicle started..")
        
class Bike(Vehicle):
    def start(self):
        print("Bike started ...")
        
bike = Bike()
bike.start()

#3

class Employee:
    
    def work(self):
        print("Working....")
        
class Developer(Employee):
    
    def work(self):
        print("Coding in PYTHON")
        
developer = Developer()
developer.work()
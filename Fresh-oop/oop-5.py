class Phone:
    
    def __init__ (self,name):
        self.name = name
Phone1 = Phone("Samsung")
phone2 = Phone("Iphone")

print(Phone1.name)
print(phone2.name)

class Car:
    
    def __init__ (self,name,year):
        self.name = name
        self.year = year
        
car1 = Car("Toyota",2005)
car2 = Car("Mercedes",2025)

print(car1.name,car1.year)
print(car2.name,car2.year)

class Book:
    
    def __init__ (self,name,author):
        self.name = name
        self.author = author
        
Book1 = Book("Harry potter","JK rowling")
Book2 = Book("BBT","Sheldon")

print(Book1.name,Book1.author)
print(Book2.name,Book2.author)
class Calculator:
    
    @staticmethod
    def add(a,b):
        return a + b
print(Calculator.add(10,15))

class Convertor:
    
    @staticmethod
    def convert(a):
        return a * 1000
    
num = int(input("Enter a number in km : "))
print(Convertor.convert(num),"meters")

class Greeting:
    @staticmethod
    def hello(name):
        return "Hello " + name

print(Greeting.hello("Adeeb"))
print(Greeting.hello("Ronaldo"))
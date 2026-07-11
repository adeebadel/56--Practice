class Phone:
    
    def __init__ (self,name,price):
        self.name = name
        self.price = price

phone = Phone("Samsung",80000)

print(phone.name,phone.price)

phone.price = 95000

print(phone.name,phone.price)

class Player:
    
    def __init__ (self,name,score):
        self.name = name
        self.score = score
        
player = Player("Virat",150)
print(player.name,player.score)

player.score = 210

print(player.name,player.score)


# 3

class Movie:
    
    def __init__ (self,name,rating):
        self.name = name
        self.rating = rating
        
movie1 = Movie("Titanic",5.0)
movie2 = Movie("Avengers",9.9)

print(movie1.name,movie1.rating)
print(movie2.name,movie2.rating)

movie1.rating = 8.8

print(movie1.name,movie1.rating)
print(movie2.name,movie2.rating)
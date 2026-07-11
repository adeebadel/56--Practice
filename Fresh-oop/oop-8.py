class Phone:
    
    company = "Samsung"
    
    def __init__ (self,brand):
        self.brand = brand
        
phone1 = Phone("S24")
phone2 = Phone("S25")

print(phone1.brand)
print(phone1.company)
print(phone2.brand)
print(phone2.company)

#2
class Player:
    
    team = "India"
    
    def __init__(self,name):
        self.name = name
        
player1 = Player("Virat")
player2 = Player("Rohit")

print(player1.name,"plays for team",player1.team)
print(player2.name,"plays for team",player2.team)

#3
class Movie:
    
    industry = "Hollywood"
    
    def __init__ (self,title,rating):
        self.title = title
        self.rating = rating
        
movie1 = Movie("Avengers",9.9)
movie2 = Movie("Titanic",7.3)

print(movie1.title,movie1.industry,movie1.rating)
print(movie2.title,movie2.industry,movie2.rating)
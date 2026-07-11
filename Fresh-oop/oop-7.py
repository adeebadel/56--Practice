class Phone:
    
    def __init__ (self,name):
        self.name = name
        
    def ring(self):
        print(self.name , "is ringing")
        
phone = Phone("Samsung")
phone.ring()

#🎯 Challenge 2
#Create
#Player
#Attributes
#name
#score
#Method
#show_score()
#Output
#Virat has 150 runs.
#Create two players.
#Call the method for both.

class Player:
    
    def __init__ (self,name,score):
        self.name = name
        self.score = score
        
    def show_score(self):
        print(self.name , "has scored" , self.score)
        
player1 = Player("Virat",150)
player2 = Player("Ronaldo",200)

player1.show_score()
player2.show_score()

#🎯 Challenge 3
#Create
#Movie
#Attributes
#titl
#rating
#Method
#review()
#Output
#Titanic has rating 8.8
#Create two movies.
#Call the method.

class Movie:
    
    def __init__ (self,title,rating):
        self.title = title
        self.rating = rating
        
    def review(self):
        print(self.title , "has a rating of" , self.rating)
        
movie1 = Movie("Avengers",9.9)
movie2 = Movie("Avatar",7.2)

movie1.review()
movie2.review()

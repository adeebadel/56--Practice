class Phone:
    
    company = "Samsung"
    @classmethod
    def change_company(cls,name):
        cls.company = name

print(Phone.company)

Phone.change_company("Iphone")
print(Phone.company)


class Player:
    team = "india"
    @classmethod
    def change_team(cls,team):
        cls.team = team
print(Player.team)
Player.change_team("Australia")
print(Player.team)

class Movie:
    industry = "Hollywood"
    @classmethod
    def change_industry(cls,name):
        cls.industry = name
print(Movie.industry)
Movie.change_industry("Bollywood")
print(Movie.industry)
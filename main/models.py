from django.db import models

# Create your models here.

#validations
class CardManager(models.Manager):
    def basic_validator(self, post_data):
        errors= {}

        if len(post_data["brand"]) < 2:
            errors["brand"] = "Please enter a brand of at least 2 characters."

        if len(post_data["player_name"]) <2:
            errors["player_name"] = "Please enter a name of at least 2 characters."
        
        if len(post_data["sport"]) < 4:
            errors["sport"] = "Please provide a sport of at least 4 characters."
        
        if len(post_data["team_name"]) < 3:
            errors["team_name"] = "Please provide a team name of at least 3 characters."
        

        return errors








class User(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    email=models.EmailField(unique=True)
    favorite_sport=models.TextField()
    number_of_cards_owned=models.IntegerField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

class Card(models.Model):
    brand=models.CharField(max_length=50)
    player_name=models.CharField(max_length=100)
    sport=models.CharField(max_length=50)
    team_name=models.CharField(max_length=50)
    release_date=models.DateField(default="2020-04-14")
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    owner= models.ForeignKey(User, on_delete=models.CASCADE, related_name="cards")
    
    objects = CardManager()
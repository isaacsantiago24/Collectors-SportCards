from django.shortcuts import render,redirect

#validations
from django.contrib import messages

from .models import User,Card #import your models

# Create your views here.
def view_all_collectors(request): #we are just showing all the collectors
    context = {
        "users": User.objects.all()
    }

    return render(request,"users.html",context)

def new_user_page(request): #a blank form to add a new user
    return render(request,"new-user.html")

def create_new_user(request): #creating a new user
    new_user=User.objects.create( #creating a variable
        first_name=request.POST["first_name"],
        last_name=request.POST["last_name"],
        email=request.POST["email"],
        favorite_sport=request.POST["favorite_sport"],
        number_of_cards_owned=request.POST["number_of_cards_owned"]
    )

    return redirect("/collectors")

def delete_collector(request, user_id):
    user = User.objects.get(id=user_id)
    user.delete()

    return redirect("/collectors")

def show_collector_page(request, user_id):
    context={
        "user": User.objects.get(id=user_id),
        "cards": Card.objects.all()
    }

    return render(request, "show-user.html", context)

def delete_card(request, card_id,user_id):
    card=Card.objects.get(id=card_id)
    card.delete()

    return redirect(f"/collectors/{user_id}")

def create_sports_card(request, user_id):

    #validations
    errors = Card.objects.basic_validator(request.POST)

    if len(errors) > 0:

        #looping in python
        for key, err in errors.items():
            messages.error(request, err)

        return redirect(f"/collectors/{user_id}")

    Card.objects.create(
        owner= User.objects.get(id=user_id),

        brand=request.POST['brand'],
        player_name=request.POST["player_name"],
        sport=request.POST["sport"],
        team_name=request.POST["team_name"],
        release_date=request.POST["release_date"]

    )

    return redirect(f"/collectors/{user_id}")

def edit_card_page(request,card_id):
    card = Card.objects.get(id=card_id)
    card.release_date= card.release_date.strftime("%Y-%m-%d")
    #strftime

    context= {
        "card": card

    }

    return render(request, "edit-card.html", context)

def update_card(request, card_id):
    card=Card.objects.get(id=card_id)

    card.brand=request.POST["brand"]
    card.player_name=request.POST["player_name"]
    card.sport=request.POST["sport"]
    card.team_name=request.POST["team_name"]
    card.release_date=request.POST["release_date"]

    card.save()

    return redirect(f"/cards/{card_id}/edit")
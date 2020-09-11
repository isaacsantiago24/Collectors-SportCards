from django.urls import path

from .import views

urlpatterns= [
    path("collectors", views.view_all_collectors),
    path("collectors/new", views.new_user_page),
    path("users/create", views.create_new_user),
    path("collectors/<int:user_id>/delete", views.delete_collector),
    path("collectors/<int:user_id>", views. show_collector_page),

    path("collectors/<int:user_id>/cards/<int:card_id>/delete", views.delete_card),
    path("collectors/<int:user_id>/cards/create", views.create_sports_card),

    path("cards/<int:card_id>/edit", views.edit_card_page),
    path("cards/<int:card_id>/update", views.update_card)



]
from django.contrib import admin
from django.urls import path
from .views import *
from . import views

app_name = "images_app"

urlpatterns = [
    path('', views.index_view, name="index"),
    path('signup/', views.signup_view, name="signup"),
    path('login/', views.signin_view, name="login"),
    path('logout/', views.logout_view, name="logout"),
    path('add_card/', views.add_card, name="add_card"),
    path('card/<int:pk>', views.card_detail_view, name="card_page"),
    path('delete/<int:pk>', views.delete_entry, name="delete"),
]
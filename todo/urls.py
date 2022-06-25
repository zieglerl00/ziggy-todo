from django.urls import path
from . import views

app_name = "todo"

urlpatterns = [
    path('', views.index_view, name="index"),
    path('signup/', views.signup_view, name="signup"),
    path('login/', views.signin_view, name="login"),
    path('logout/', views.logout_view, name="logout"),
    path('add_todo/', views.new_todo_view, name="add_todo"),
]
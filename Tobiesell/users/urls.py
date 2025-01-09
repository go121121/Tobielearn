from django.urls import path,include  
from . import views 
from django.shortcuts import render 

urlpatterns=[
    path("register/", views.register,name="register" ), 
    path("login/", views.login, name="login"),
    path('learn_page',views.learn_page,name="learn"), 
    path('',views.home ,name="home"), 
]
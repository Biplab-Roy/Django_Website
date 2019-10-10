from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('signup/',views.signup,name='Signup_url'),
    path('signin/',views.signin,name='Signi_url'),
    path('profile/',views.profile,name='Profile_url'),
]

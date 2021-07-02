from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('', views.index, name="home"),
    path('tutorial', views.tutorial, name='tutorial'),
    path('contact', views.contact, name='contact'),
    path('gameplay', views.gameplay, name='gameplay'),
    path('about', views.about, name='about'),
    path('privacy', views.privacy, name='privacy'),
    path('terms', views.terms, name='terms'),
]

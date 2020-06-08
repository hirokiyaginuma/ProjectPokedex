from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
	path('about_me/', views.about_me, name='about_me'),
	path('Starter_Pokemon/', views.Starter_Pokemon, name='Starter_Pokemon'),
]
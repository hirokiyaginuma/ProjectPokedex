from django.shortcuts import render
from django.utils import timezone
from .models import Main


def index(request):
    return render(request, 'website/index.html', {})
	
def about_me(request):
    return render(request, 'website/about_me.html', {})
	
def Starter_Pokemon(request):
    return render(request, 'website/Starter_Pokemon.html', {})
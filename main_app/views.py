from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.db import models
from .models import Game

def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact_us(request):
    return render(request, 'contact-us.html')

def games_index(request):
    games = Game.objects.all()
    return render(request, 'games/index.html', {'played_games': games})

def games_detail(request, game_id):
    game = Game.objects.get(id=game_id)
    return render(request, 'games/detail.html', {'game': game})

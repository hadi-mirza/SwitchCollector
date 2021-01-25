from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.db import models

class Game:
  def __init__(self, name, time):
    self.name = name
    self.time = time

games = [
    Game('Legend Of Zelda: BOTW', '150 Hours'),
    Game('Stardew Valley', '500 Hours'), 
    Game('Untitled Goose Game', '10 Hours'),
    Game('Ori and the Will of the Wisp', '24 Hours'),
    Game('Lego Harry Potter', '32 Hours'),
    ]

def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact_us(request):
    return render(request, 'contact-us.html')

def games_index(request):
    return render(request, 'games/index.html', {'played_games': games})
from django.shortcuts import redirect, render

# Create your views here.

from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.db import models
from django.urls import reverse_lazy
from .models import Game
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView

def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact_us(request):
    return render(request, 'contact-us.html')

# def games_index(request):
#     games = Game.objects.all()
#     return render(request, 'games/index.html', {'played_games': games})

# def games_detail(request, game_id):
#     game = Game.objects.get(id=game_id)
#     return render(request, 'games/detail.html', {'game': game})

class GameList(ListView):
    model = Game

class GameDetail(DetailView):
    model = Game
    pk_url_kwarg = "game_id"

class GameCreate(CreateView):
    model = Game
    fields = '__all__'
    success_url = reverse_lazy('all_games')
    
class GameUpdate(UpdateView):
    model = Game
    fields = '__all__'
    pk_url_kwarg = 'game_id'
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('all_games')

class GameDelete(DeleteView):
    model = Game
    pk_url_kwarg = 'game_id'
    success_url = reverse_lazy('all_games')

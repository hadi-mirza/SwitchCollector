from django.shortcuts import redirect, render

# Create your views here.

from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.db import models
from django.urls import reverse_lazy
from .models import Game
from .models import Review
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact_us(request):
    return render(request, 'contact-us.html')

def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

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

    # def form_valid(self, form):
    # # Assign the logged in user (self.request.user)
    #     form.instance.user = self.request.user  # form.instance is the cat
    # # Let the CreateView do its job as usual
    #     return super().form_valid(form)
    
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

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('about/', views.about),
    path('contactus/', views.contact_us),
    path('games/', views.games_index),
    path('games/<int:game_id>', views.games_detail)
]

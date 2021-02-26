from django.urls import path, include
from . import views
from .views import GameList, GameDetail, GameCreate, GameUpdate, GameDelete

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contactus/', views.contact_us, name='contact'),
    # path('games/', views.games_index),
    # path('games/<int:game_id>', views.games_detail),
    path('games/all/', GameList.as_view(), name='all_games'),
    path('games/add', GameCreate.as_view(), name='game_create'),
    path('games/all/<int:game_id>', GameDetail.as_view(), name='game_detail'),
    path('games/all/<int:game_id>/update', GameUpdate.as_view(), name='game_update'),
    path('games/all/<int:game_id>/delete', GameDelete.as_view(), name='game_delete'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', views.signup, name='signup'),
]

from django.urls import path
from . import views
from .views import GameList
from .views import GameDetail
from .views import GameCreate
from .views import GameUpdate
from .views import GameDelete

urlpatterns = [
    path('', views.home),
    path('about/', views.about),
    path('contactus/', views.contact_us),
    # path('games/', views.games_index),
    # path('games/<int:game_id>', views.games_detail),
    path('games/all/', GameList.as_view(), name='all_games'),
    path('games/all/<int:game_id>', GameDetail.as_view(), name='game_detail'),
    path('games/add', GameCreate.as_view(), name='game_create'),
    path('games/all/<int:game_id>/update', GameUpdate.as_view(), name='game_update'),
    path('games/all/<int:game_id>/delete', GameDelete.as_view(), name='game_delete')
]

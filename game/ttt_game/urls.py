"""ttt_game_server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .game import start_new_game, get_game_state, player_move, is_have_active_game

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('start_new_game/', start_new_game, name='start_new_game'),
    path('get_game_state/', get_game_state, name='get_game_state'),
    path('player_move/', player_move, name='player_move'),
    path('is_have_active_game/', is_have_active_game, name='is_have_active_game'),
    
]

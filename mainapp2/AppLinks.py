from .views import loginpage
from .views import moviepage
from .views import homepage
from .views import fetch_one_player_page
from django.urls import path
from .views import fetch_all_players_page
from .views import update_one_player_page
from .views import update_one_movie_page
from .views import delete_one_player
urlpatterns=[
    path("homepage/", homepage, name="homepage"),
    path("loginpage/", loginpage, name="loginpage"),
    path("moviepage/", moviepage, name="moviepage"),
    path("fetch_one_player_page/<int:pk>", fetch_one_player_page, name="fetch_one_player_page"),
    path("update_one_player/<int:pk>", update_one_player_page, name="update_one_player"),
    path("update_one_movie/<int:pk>", update_one_movie_page, name="update_one_movie"),
    path("delete_one_player/<int:pk>", delete_one_player, name="delete_one_player"),

path("allplayspage/", fetch_all_players_page, name="allplayerspage"),
]
 
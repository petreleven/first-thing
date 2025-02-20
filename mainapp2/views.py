from django.shortcuts import render
from django.http import HttpResponse
from .models import player
from .models import Movie
# Create your views here.
def homepage(request):
    return HttpResponse("Hello from Yasser")
def loginpage(request):
    print("you did a"+request.method)
    return render(request, "login.html")
def moviepage(request):
    print("you did a"+request.method)
    if request.method=="POST":
         Movie_Name=request.POST.get("Movie name")
         Description=request.POST.get("Description")
         New_movie=Movie(name = Movie_Name, description= Description)
         New_movie.save()
    return render(request, "movie.html")

def fetch_all_players_page(request):
    all_players = player.objects.all()
    return render(request, "all_players.html", {"all_players" :all_players})

def fetch_all_movies_page(request):
    ""
def fetch_one_player_page(request, pk):
    single_player = player.objects.get(pk = pk)
    return render(request, "one_player.html", {"single_player" :single_player})

def update_one_player_page(request, pk):
    single_player = player.objects.get(pk = pk)
    if request.method == "POST":
        new_username = request.POST.get("username")
        new_password = request.POST.get("password")
        single_player.username = new_username
        single_player.password = new_password
        single_player.save()
    return render(request, "update_one_player.html", {"single_player" :single_player})

def update_one_movie_page(request, pk):
    single_movie = Movie.objects.get(pk = pk)
    return render (request, "update_one_movie.html", {"single_movie" :single_movie})
from django.shortcuts import redirect
def delete_one_player(request, pk):
    single_player = player.objects.get(pk=pk)
    single_player.delete()
    return redirect("homepage")
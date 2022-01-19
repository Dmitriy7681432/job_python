from django.shortcuts import render,get_object_or_404
from .models import Movie
# Create your views here.

def show_all_movie(request):
    movies = Movie.objects.all()
    return render(request, 'movie/all_movie.html',{
        'movies': movies

    })

def show_one_movie(request, slug_movie:str):
    movie = get_object_or_404(Movie, slug=slug_movie)
    print('slug',slug_movie)
    return render(request, 'movie/one_movie.html',{
        'movie': movie

    })
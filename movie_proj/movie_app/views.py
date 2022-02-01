from django.shortcuts import render,get_object_or_404
from django.db.models import F, Sum,Max,Min,Count,Avg
from .models import Movie
# Create your views here.

def show_all_movie(request):
    # movies = Movie.objects.order_by(F('year').asc(nulls_last=True), '-rating')
    movies = Movie.objects.filter(id=7)
    agg = movies.aggregate(Avg('budget'), Max('rating'), Min('rating'))
    return render(request, 'movie/all_movie.html',{
        'movies': movies,
        'agg': agg,
        'total': movies.count(),

    })

def show_one_movie(request, slug_movie:str):
    movie = get_object_or_404(Movie, slug=slug_movie)
    return render(request, 'movie/one_movie.html',{
        'movie': movie

    })
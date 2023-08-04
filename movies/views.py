from typing import Any, Dict
from django.shortcuts import render
from movies.models import *
from django.views.generic import ListView, View
from movies.utils import movie_filter

# Create your views here.


def home_view(request):
    return render(request, 'pages/index.html')


def type_wise_movie_view(request, slug):
    filter_string = movie_filter(request)

    movie_type = MovieType.objects.get(slug=slug)
    movies = Movie.objects.filter(movie_type=movie_type, **filter_string)
    context = {
        'movies': movies,
        'movie_type': movie_type
    }
    return render(request, 'pages/type-wise-movies.html', context)

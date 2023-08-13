import json
from django.shortcuts import render, get_object_or_404
from movies.models import *
from django.views.generic import ListView, View, DetailView
from movies.utils import movie_filter
from django.http import JsonResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.db.models import Avg

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


def actor_details(request, actor_id):
    role = request.GET.get('role')
    if role == 'actor':
        actor = get_object_or_404(Actor, id=actor_id)
    elif role == 'director':
        actor = get_object_or_404(Director, id=actor_id)
    else:
        print("Invalid role")

    context = {
        'actor': actor
    }
    return render(request, 'pages/actor-details.html', context)


class MovieDetailsView(DetailView):
    template_name = 'pages/movie-details.html'
    queryset = Movie.objects.all()
    context_object_name = "movie"

    def get_context_data(self, *args, **kwargs):
        context = super(MovieDetailsView, self).get_context_data(
            *args, **kwargs)
        context['reviews'] = Review.objects.filter(
            movie=kwargs['object']
        )
        context['avg_rating'] = context['reviews'].aggregate(Avg('rating'))[
            'rating__avg']
        return context


@login_required(login_url='/accounts/login')
def create_review(request):
    if request.method == 'POST':
        data = json.loads(request.body)

        movie_id = data.get('movie_id')
        movie = get_object_or_404(Movie, id=movie_id)
        user = request.user
        rating = data.get('rating', 1)
        message = data.get('message', '')

        review, created = Review.objects.update_or_create(
            user=user,
            movie=movie,
            defaults={
                'rating': rating,
                'message': message
            }
        )

        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    return JsonResponse({'success': False})

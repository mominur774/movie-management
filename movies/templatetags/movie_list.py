from django import template
from movies.models import Movie, Category, MovieType
from movies.utils import movie_filter

register = template.Library()


@register.filter(name="type_wise_movie")
def type_wise_movie(request, movie_type):
    filter_string = movie_filter(request)
    return Movie.objects.filter(movie_type=movie_type, **filter_string)[:6]


@register.simple_tag
def category_list():
    return Category.objects.all().prefetch_related('subcategory')


@register.simple_tag
def movie_type_list():
    return MovieType.objects.all()

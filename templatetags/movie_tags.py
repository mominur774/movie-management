from django import template
from movies.models import Movie

register = template.Library()

@register.simple_tag
def movie_list():
    return Movie.objects.all()
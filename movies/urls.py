from movies import views
from django.urls import path


urlpatterns = [
    path('', views.home_view, name='index'),
    path('movie-type/<slug:slug>/',
         views.type_wise_movie_view, name='type_wise_movie')
]

from django.urls import path
from movies import views
from movies.views import MovieDetailsView

urlpatterns = [
    path('movie/<int:movie_id>/', views.watch_movie, name='watch_movie'),
    path('movie/<slug:slug>/', MovieDetailsView.as_view(), name='movie-details'),

    path('', views.home_view, name='index'),
    path('movie/<slug:slug>/', views.MovieDetailsView.as_view(), name="movie_details"),
    path('movie/<slug:movie_slug>/episode/<int:episode_id>/', views.movie_episode, name='movie_episode'),
    path('movie-type/<slug:slug>/', views.type_wise_movie_view, name='type_wise_movie'),
    path('actor/<int:actor_id>/', views.actor_details, name='actor_details'),
    path('create-review/', views.create_review, name='create_review'),
]
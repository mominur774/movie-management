from movies import views
from django.urls import path


urlpatterns = [
    path('', views.home_view, name='index'),
    path('movie-type/<slug:slug>/',
         views.type_wise_movie_view, name='type_wise_movie'),
    path('actor/<int:actor_id>/', views.actor_details, name='actor_details'),
    path('movie/<slug:slug>/', views.MovieDetailsView.as_view(), name="movie_details"),
    path('create-review/', views.create_review, name='create_review'),
]

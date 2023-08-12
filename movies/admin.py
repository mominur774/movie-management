from django.contrib import admin
from movies.models import Actor, Director, Category, SubCategory, Movie, MovieType, Review

# Register your models here.


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "gender", "role", )


@admin.register(Director)
class DirectorAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "gender", "role", )


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "slug",)


@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "slug", "category",)


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "slug", "movie_type", "movie_url", )


@admin.register(MovieType)
class MovieTypeAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "slug",)


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("id", "rating", "movie", "user", )

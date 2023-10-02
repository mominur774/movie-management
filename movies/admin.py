from django.contrib import admin
from movies.models import Actor, Director, Category, SubCategory, Movie, MovieType, Review
from .models import Episode



@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "gender", "role",)

@admin.register(Director)
class DirectorAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "gender", "role", )

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "slug",)

@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "slug", "category", )

@admin.register(MovieType)
class MovieTypeAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "slug", )

# MovieAdmin uchun o'zgarishlar
@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "slug", "movie_type",'is_premiere', )
    fields = ('name', 'categories', 'subcategories', 'actors', 'directors', 'thumbnail', 'movie_type', 'iframe_content',  'description',"fasl","qism",'is_premiere','janr','yili','tili','kompaniya','davomiylogi','ovozberishaktorlari','rejesyor','homiy','yoshcheklovi',)

@admin.register(Episode)
class EpisodeAdmin(admin.ModelAdmin):
    list_display = ['name', 'movie']


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("id", "rating", "movie", "user")

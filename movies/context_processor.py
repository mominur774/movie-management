from movies.models import Category, MovieType


def movie_context(request):
    return {
        'categories': Category.objects.all().prefetch_related('subcategory'),
        'movie_types': MovieType.objects.all()
    }

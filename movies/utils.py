def movie_filter(request):
    filter_string = {}
    filter_mappings = {
        'category': 'categories__in',
        'subcategory': 'subcategories__in',
        'search': 'name__icontains'
    }
    for key in request.GET:
        if request.GET.get(key):
            filter_string[filter_mappings[key]] = request.GET.get(key)

    return filter_string

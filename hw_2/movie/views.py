from django.http import JsonResponse, Http404
from .models import Movie

def movies_list(request):
    movies = list(Movie.objects.values())
    return JsonResponse(movies, safe=False)

def movie_detail(request, id):
    try:
        movie = Movie.objects.get(pk=id)
    except Movie.DoesNotExist:
        raise Http404
    return JsonResponse({'title': movie.title, 'description': movie.description, 'producer': movie.producer, 'duration': movie.duration})
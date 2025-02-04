from django.http import JsonResponse, Http404
from .models import Article

def articles_list(request):
    articles = list(Article.objects.values())
    return JsonResponse(articles, safe=False)

def article_detail(request, id):
    try:
        article = Article.objects.get(pk=id)
    except Article.DoesNotExist:
        raise Http404
    return JsonResponse({'title': article.title, 'text': article.text, 'author': article.author})
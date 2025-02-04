from django.urls import path
from . import views

urlpatterns = [
    path('', views.articles_list, name='articles_list'),
    path('<int:id>/', views.article_detail, name='article_detail'),
]
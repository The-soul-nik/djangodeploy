from django.shortcuts import render
from .models import Article
# Create your views here.
def homepage(request):
    return render(request, 'ahead/home.html')


def articles(request):
    articles = Article.objects.all()
    return render(request, "ahead/articles.html", {'articles':articles})

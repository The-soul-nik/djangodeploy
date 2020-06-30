from django.urls import path
from . import views

app_name = "ahead"

urlpatterns = [
    path('', views.homepage),
    path('articles', views.articles, name="articles")
]

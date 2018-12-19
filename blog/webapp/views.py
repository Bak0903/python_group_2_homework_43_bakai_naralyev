from django.shortcuts import render
from django.views.generic import ListView, DetailView
from webapp.models import Blogger, Article, Favorite

class ArticleListView(ListView):
    model = Article
    template_name = 'article_list.html'


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article_detail.html'


class BloggerListView(ListView):
    model = Blogger
    template_name = 'blogger_list.html'


class BloggerDetailView(DetailView):
    model = Blogger
    template_name = 'blogger_detail.html'


class FavoriteListView(ListView):
    model = Favorite
    template_name = 'favorite_list.html'

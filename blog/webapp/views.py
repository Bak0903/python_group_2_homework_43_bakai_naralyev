from django.shortcuts import render,redirect, get_object_or_404
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


def favorite_articles(request, blogger_pk):
    blogger = get_object_or_404(Blogger, pk=blogger_pk)
    list = blogger.blogger_fav.all
    return render(request, 'favorite_articles.html', {'list': list})


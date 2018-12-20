from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, FormView, CreateView, UpdateView, DeleteView
from webapp.models import Blogger, Article, Comment
from webapp.forms import SearchArticleForm, ArticleForm, CommentForm
from django.urls import reverse_lazy


class ArticleListView(ListView, FormView):
    model = Article
    template_name = 'article_list.html'
    form_class = SearchArticleForm

    def get_queryset(self):
        search = self.request.GET.get('search')

        if not search:
            return Article.objects.all()
        else:
            return Article.objects.filter(title__contains=search)





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


class ArticleCreateView(CreateView):
    model = Article
    template_name = 'article_create.html'
    form_class = ArticleForm
    success_url = reverse_lazy('article_list')

class ArticleDeleteView(DeleteView):
    model = Article
    template_name = 'delete_article.html'
    success_url = reverse_lazy('article_list')


class ArticleUpdateView(UpdateView):
    model = Article
    template_name = 'article_update.html'
    form_class = ArticleForm
    success_url = reverse_lazy('article_list')


class CommentCreateView(CreateView):
    model = Comment
    template_name = 'comment_create.html'
    form_class = CommentForm
    success_url = reverse_lazy('article_list')


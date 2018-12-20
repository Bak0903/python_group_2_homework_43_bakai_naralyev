from django import forms
from webapp.models import Article, Comment


class SearchArticleForm(forms.Form):
    search = forms.CharField(max_length=50, required=False, label="Поле для поиска")


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'text', 'author']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['author', 'text', 'comment_to_article']


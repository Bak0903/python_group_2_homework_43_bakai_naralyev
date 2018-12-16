from django.db import models
from django.contrib.auth.models import User


class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='info', verbose_name='Пользователь')
    birth_date = models.DateField(verbose_name='День рождения')


class Blogger(models.Model):
    name = models.CharField(max_length=50, verbose_name="Имя")
    phone = models.CharField(max_length=20, verbose_name="Телефон")
    email = models.EmailField(max_length=50, verbose_name="Почта")

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    text = models.TextField(max_length=3000, verbose_name='Текст')
    author = models.ForeignKey(Blogger, on_delete=models.PROTECT, max_length=40,  verbose_name='Автор')

    def __str__(self):
        return self.title


class Comment(models.Model):
    comment_to_article = models.ForeignKey(Article, on_delete=models.CASCADE, null=True, blank=True, related_name='related', verbose_name="Комментарий к статье")
    comment_to_comment = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='related', verbose_name="Комментарий к комментарию")
    author = models.ForeignKey(Blogger, on_delete=models.PROTECT, max_length=40,  verbose_name='Автор')
    text = models.TextField(max_length=3000, verbose_name='Текст комментария')

    def __str__(self):
        return 'Комментарий от %s' % self.author


class Mark(models.Model):
    MARK_AWFULLY = 1
    MARK_BAD = 2
    MARK_NORMAL = 3
    MARK_GOOD = 4
    MARK_EXCELLENT = 5

    MARK_CHOICES = (
        (MARK_AWFULLY, 'ужасно'),
        (MARK_BAD, 'плохо'),
        (MARK_NORMAL, 'нормально'),
        (MARK_GOOD, 'хорошо'),
        (MARK_EXCELLENT, 'отлично')
    )

    relation = models.ForeignKey(Article, on_delete=models.PROTECT, related_name='mark',  verbose_name="Отношение")
    user = models.ForeignKey(Blogger, max_length=200, on_delete=models.PROTECT, verbose_name="Оценивающий")
    mark = models.CharField(max_length=20, choices=MARK_CHOICES, null=True, blank=True, verbose_name="Оценка")

    def __str__(self):
        return "Оценка к %s" % self.relation


class Favorite(models.Model):
    user = models.ForeignKey(Blogger, on_delete=models.PROTECT)
    favorite = models.ForeignKey(Article, on_delete=models.PROTECT)

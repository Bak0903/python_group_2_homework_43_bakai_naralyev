from django.contrib import admin
from webapp.models import UserInfo, Article, Comment, Mark, Favorite, Blogger

admin.site.register(UserInfo)
admin.site.register(Blogger)
admin.site.register(Article)
admin.site.register(Comment)
admin.site.register(Mark)
admin.site.register(Favorite)

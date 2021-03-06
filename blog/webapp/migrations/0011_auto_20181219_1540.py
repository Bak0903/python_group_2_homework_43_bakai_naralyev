# Generated by Django 2.1.4 on 2018-12-19 15:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0010_auto_20181219_1456'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='author',
            field=models.ForeignKey(max_length=40, on_delete=django.db.models.deletion.PROTECT, related_name='blogger_comm', to='webapp.Blogger', verbose_name='Автор'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='comment_to_article',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='article_comm', to='webapp.Article', verbose_name='Комментарий к статье'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='comment_to_comment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comment', to='webapp.Comment', verbose_name='Комментарий к комментарию'),
        ),
        migrations.AlterField(
            model_name='favorite',
            name='article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='article_fav', to='webapp.Article'),
        ),
        migrations.AlterField(
            model_name='favorite',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='blogger_fav', to='webapp.Blogger'),
        ),
        migrations.AlterField(
            model_name='mark',
            name='relation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='article_mark', to='webapp.Article', verbose_name='Отношение'),
        ),
        migrations.AlterField(
            model_name='mark',
            name='user',
            field=models.ForeignKey(max_length=200, on_delete=django.db.models.deletion.PROTECT, related_name='blogger_mark', to='webapp.Blogger', verbose_name='Оценивающий'),
        ),
    ]

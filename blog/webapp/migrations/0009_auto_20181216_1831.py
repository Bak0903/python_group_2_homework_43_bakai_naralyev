# Generated by Django 2.1.4 on 2018-12-16 18:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0008_auto_20181216_1830'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='author',
            field=models.ForeignKey(max_length=40, on_delete=django.db.models.deletion.PROTECT, to='webapp.Blogger', verbose_name='Автор'),
        ),
    ]

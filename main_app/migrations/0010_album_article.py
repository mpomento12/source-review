# Generated by Django 4.0.2 on 2023-08-16 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0009_remove_album_article_alter_review_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='article',
            field=models.TextField(default='', max_length=10000),
        ),
    ]
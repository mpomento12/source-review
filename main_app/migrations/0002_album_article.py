# Generated by Django 4.0.2 on 2023-08-15 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='article',
            field=models.TextField(default='string', max_length=2000),
        ),
    ]

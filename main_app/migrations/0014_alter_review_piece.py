# Generated by Django 4.0.2 on 2023-08-17 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0013_alter_review_piece'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='piece',
            field=models.CharField(choices=[('C', 'Classic'), ('O', 'Okay '), ('B', 'Bad')], default='C', max_length=1),
        ),
    ]
# Generated by Django 4.0.2 on 2023-08-17 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0016_alter_review_piece'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='piece',
            field=models.CharField(choices=[(0, 'Zero'), (1, 'One'), (2, 'Two'), (3, 'Three'), (4, 'Four'), (5, 'Five')], default=0, max_length=1),
        ),
    ]

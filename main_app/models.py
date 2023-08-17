from django.db import models
from django.urls import reverse
from datetime import date


REVIEWS = (
    ('C', 'Classic'),
    ('O', 'Okay '),
    ('B', 'Bad')
)

class Format(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('formats_detail', kwargs={'pk': self.id})


class Album(models.Model):
    name = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    article = models.TextField(max_length=10000, default="")
    year = models.IntegerField()
    formats = models.ManyToManyField(Format)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'album_id': self.id})
    
class Review(models.Model):
    date = models.DateField('Reading Date')
    piece = models.CharField(
        max_length=1,
            choices=REVIEWS,
            default=REVIEWS[0][0]
        )
    
    album = models.ForeignKey(Album, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.get_piece_display()} on {self.date}'
    
    class Meta:
        ordering = ['-date']
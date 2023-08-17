from django.db import models
from django.urls import reverse


REVIEWS = (
    ('C', 'Classic'),
    ('O', 'Okay '),
    ('B', 'Bad')
)


# Create your models here.

class Album(models.Model):
    name = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    article = models.TextField(max_length=10000, default="")
    year = models.IntegerField()

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
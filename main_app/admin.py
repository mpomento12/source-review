from django.contrib import admin
from .models import Album, Review, Photo

# Register your models here.
admin.site.register(Album)
admin.site.register(Review)
admin.site.register(Photo)
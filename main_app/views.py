from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Album
from .forms import ReviewForm


# Create your views here.

def home(request):
    return render (request, 'home.html')

def about(request):
    return render(request, 'about.html')

def albums_index(request):
    albums = Album.objects.all()
    return render(request, 'albums/index.html', { 'albums': albums })

def albums_detail(request, album_id):
    album = Album.objects.get(id=album_id)
    review_form = ReviewForm()
    return render(request, 'albums/detail.html', {'album':album, 'review_form' : review_form})

def add_review(request, album_id):
    form = ReviewForm(request.POST)
    print(form)
    if form.is_valid():
        new_review = form.save(commit=False)
        new_review.album_id = album_id
        new_review.save()
    return redirect('detail', album_id=album_id)

class AlbumCreate(CreateView):
    model =  Album
    fields = '__all__'
    # success_url = '/albums/'

class AlbumUpdate(UpdateView):
    model = Album
    fields = ['name','artist','article']

class AlbumDelete(DeleteView):
    model = Album
    success_url = '/albums/'
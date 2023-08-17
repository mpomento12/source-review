from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Album, Format
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
    id_list = album.formats.all().values_list('id')
    formats_album_doesnt_have = Format.objects.exclude(id__in=id_list)
    review_form = ReviewForm()
    return render(request, 'albums/detail.html', {
       'album':album, 
       'review_form' : review_form,
       'formats': formats_album_doesnt_have})

def add_review(request, album_id):
    form = ReviewForm(request.POST)
    if form.is_valid():
        new_review = form.save(commit=False)
        new_review.album_id = album_id
        new_review.save()
    return redirect('detail', album_id=album_id)

def assoc_format(request, album_id, format_id):
   Album.objects.get(id=album_id).formats.add(format_id)
   return redirect('detail', album_id=album_id)

class AlbumCreate(CreateView):
    model =  Album
    fields = ['name','artist','company', 'article', 'year']
    # success_url = '/albums/'

class AlbumUpdate(UpdateView):
    model = Album
    fields = ['name','artist','article']

class AlbumDelete(DeleteView):
    model = Album
    success_url = '/albums/'

class FormatList(ListView):
  model = Format

class FormatDetail(DetailView):
  model = Format

class FormatCreate(CreateView):
  model = Format
  fields = '__all__'

class FormatUpdate(UpdateView):
  model = Format
  fields = ['name']

class FormatDelete(DeleteView):
  model = Format
  success_url = '/formats/'
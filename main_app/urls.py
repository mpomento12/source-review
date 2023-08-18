from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('albums/', views.albums_index, name='index'),
    path('albums/<int:album_id>/', views.albums_detail, name='detail'),
    path('albums/create/', views.AlbumCreate.as_view(), name='albums_create'),
    path('albums/<int:pk>/update/', views.AlbumUpdate.as_view(), name='albums_update'),
    path('albums/<int:pk>/delete/', views.AlbumDelete.as_view(), name='albums_delete'),
    path('albums/<int:album_id>/add_review/', views.add_review, name='add_review'),
    path('albums/<int:album_id>/add_photo', views.add_photo, name='add_photo'),
    path('formats/', views.FormatList.as_view(), name='formats_index'),
    path('formats/<int:pk>/', views.FormatDetail.as_view(), name='formats_detail'),
    path('formats/create/', views.FormatCreate.as_view(), name='formats_create'),
    path('formats/<int:pk>/update/', views.FormatUpdate.as_view(), name='formats_update'),
    path('formats/<int:pk>/delete/', views.FormatDelete.as_view(), name='formats_delete'),
    path('albums/<int:album_id>/assoc_format/<int:format_id>/', views.assoc_format, name='assoc_format')
]
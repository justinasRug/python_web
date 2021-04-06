from django.views import generic
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
from .models import Artist
from . import jscrapper


def input_data():
    js = jscrapper
    songs = js.return_object()
    for s in songs:
        a = Artist.objects.create(song_name=s.songName, genre=s.genre, likes=s.like, pic=s.pic)

class IndexView(generic.ListView):
    template_name =  "music/index.html"
    def get_queryset(self):
        return Artist.objects.all()


class DetailView(generic.DetailView):
    model = Artist
    template_name = "music/details.html"

class AlbumDelete(DeleteView):
    model = Artist
    success_url = reverse_lazy( "music:index")

class AlbumUpdate(UpdateView):
    model = Artist
    fields = ["song_name", "genre", "likes", "pic"]

class AlbumCreate(CreateView):
    model = Artist
    fields = ["song_name", "genre", "likes", "pic"]
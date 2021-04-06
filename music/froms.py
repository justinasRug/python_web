from django import forms
from .models import Artist

class New_artist(forms.ModelForm):
    song_name = forms.CharField()
    genre = forms.CharField()
    likes = forms.CharField()
    pic = forms.CharField()

    class Meta:
        model = Artist
        fields = ("song_name", "genre", "likes", "pic")
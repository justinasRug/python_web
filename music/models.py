from django.db import models
from django.urls import reverse

class Artist(models.Model):
    song_name = models.CharField(max_length=300)
    genre = models.CharField(max_length=300)
    likes = models.CharField(max_length=300)
    pic = models.CharField(max_length=300)

    def get_absolute_url(self):
        return reverse("music:details", kwargs={"pk":self.pk})

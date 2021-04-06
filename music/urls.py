from django.urls import path
from . import views

app_name = "music"

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("<pk>/", views.DetailView.as_view(), name="details"),
    path('album/add/', views.AlbumCreate.as_view(), name='add_album'),
    path('album/<pk>/delete/', views.AlbumDelete.as_view(), name='delete_album'),
    path('album/<pk>/', views.AlbumUpdate.as_view(), name='update_album'),

]
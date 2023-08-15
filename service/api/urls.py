from django.urls import include, path
from rest_framework import routers
from django.contrib import admin
from .models import Track, Playlist, Playlist_Track
from . import views

router = routers.DefaultRouter()
router.register(r"track", views.TrackViewSet, basename="track")
router.register(r"playlist", views.PlaylistViewSet, basename="playlist")
router.register(
    r"playlist_track", views.PlaylistTrackViewSet, basename="playlist_track"
)

admin.site.register(Track)
admin.site.register(Playlist)
admin.site.register(Playlist_Track)

urlpatterns = [
    path("", include(router.urls)),
    path("admin/", admin.site.urls),
]

from rest_framework import permissions, viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from django.core.paginator import Paginator
from . import models, serializers

import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)


class TrackViewSet(viewsets.ModelViewSet):
    queryset = models.Track.objects.all()
    serializer_class = serializers.TrackSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class PlaylistViewSet(viewsets.ViewSet):
    def list(self, request):
        try:
            playlists = models.Playlist.objects.all()
            paginator = Paginator(playlists, 3)  # Show 3 playlist per page.
            page_number = request.GET.get("page")
            page_objs = paginator.get_page(page_number)

            serializer = serializers.PlaylistSerializer(page_objs, many=True)
            return Response(serializer.data)
        except Exception as e:
            logger.error(f"error happened during listing {e}")
            return Response(
                "something wrong happens", status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    def retrieve(self, request, pk=None):
        try:
            if pk is not None:
                playlist = models.Playlist.objects.get(id=pk)
                if not playlist:
                    return Response(
                        {"message": "Playlist doesn't exsit"},
                        status=status.HTTP_404_NOT_FOUND,
                    )
                serializer = serializers.PlaylistSerializer(playlist)
                return Response(serializer.data)
        except Exception as e:
            logger.error(f"error happened during get Playlist {e}")
            return Response(
                "error happened during get Playlist",
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

    def create(self, request):
        try:
            serializer = serializers.PlaylistSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(
                    {"message": "Data created"}, status=status.HTTP_201_CREATED
                )
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            logger.error(f"error happened during create Playlist {e}")
            return Response(
                "error happened during create Playlist",
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

    def destroy(self, request, pk=None):
        try:
            if pk is not None:
                playlist = models.Playlist.objects.get(pk=id)
                playlist.delete()
                return Response({"message": "Data Deleted"})
        except Exception as e:
            logger.error(f"error happened during delete Playlist {e}")
            return Response(
                "error happened during delete Playlist",
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )


class PlaylistTrackViewSet(viewsets.ViewSet):
    def list(self, request):
        try:
            playlist_id = request.GET.get("playlist_id")
            if playlist_id is not None:
                playlist_tracks = models.Playlist_Track.objects.filter(
                    playlist_id=playlist_id
                )
                serializer = serializers.PlaylistTracksSerializer(
                    playlist_tracks, many=True
                )
                return Response(serializer.data)
            else:
                return Response([])
        except Exception as e:
            logger.error(f"error happened during list trackes Playlist {e}")
            return Response(
                "error happened during list trackes Playlist",
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

    def retreive(self, request, pk=None):
        try:
            if pk is not None:
                playlist_track = models.Playlist.objects.get(id=pk)
                serializer = serializers.PlaylistTracksSerializer(playlist_track)
                return Response(serializer.data)
        except Exception as e:
            logger.error(f"error happened during get track for the playlist {e}")
            return Response(
                "error happened during get track from Playlist",
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

    def create(self, request):
        try:
            new_playlist_track = {
                "playlist_id": request.data.get("playlist_id"),
                "track_id": request.data.get("track_id"),
            }
            playlist = models.Playlist.objects.get(
                pk=new_playlist_track.get("playlist_id")
            )
            track = models.Track.objects.get(pk=new_playlist_track.get("track_id"))

            if request.data.get("playlist_id", None) is not None:
                last_track_in_playlist = models.Playlist_Track.objects.filter(
                    playlist_id=request.data.get("playlist_id"),
                    next_playlist_track__isnull=True,
                ).first()
            else:
                return Response("list not found", status=status.HTTP_400_BAD_REQUEST)
            is_first = False
            if last_track_in_playlist is None:
                is_first = True

            object_saved = models.Playlist_Track(
                playlist_id=playlist, track_id=track, is_first=is_first
            )
            object_saved.save()
            if last_track_in_playlist is not None:
                last_track_in_playlist.next_playlist_track = object_saved
                last_track_in_playlist.save()

            return Response(
                {"message": "Track added to playlist"}, status=status.HTTP_201_CREATED
            )
        except Exception as e:
            logger.error(f"error happened during add track to the playlist {e}")
            return Response(
                "error happened during add track to  playlist",
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

    def destroy(self, request, pk=None):
        try:
            playlist_track = models.Playlist_Track.objects.get(id=pk)

            if playlist_track.next_playlist_track is not None:
                next_playlist_track_obj = models.Playlist_Track.objects.get(
                    id=playlist_track.next_playlist_track.id
                )
            else:
                next_playlist_track_obj = None

            prev_playlist_track_obj = models.Playlist_Track.objects.filter(
                playlist_id=playlist_track.playlist_id,
                next_playlist_track=pk,
            ).first()

            if prev_playlist_track_obj is not None:
                prev_playlist_track_obj.next_playlist_track = (
                    playlist_track.next_playlist_track
                )
                prev_playlist_track_obj.save()
            else:
                next_playlist_track_obj.is_first = True
                next_playlist_track_obj.save()
            playlist_track.delete()
            return Response({"message": "Track removed"})
        except Exception as e:
            logger.error(f"error happened during delet track to the playlist {e}")
            return Response(
                "error happened during delete track to  playlist",
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

    def patch(self, request, pk=None):
        try:
            new_next_playlist_track_id = request.data.get("next_playlist_track_id")
            playlist_track = models.Playlist_Track.objects.get(id=pk)
            if playlist_track.next_playlist_track is None:
                old_next_playlist_track_obj = None
            else:
                old_next_playlist_track_obj = models.Playlist_Track.objects.filter(
                    playlist_id=playlist_track.playlist_id,
                    id=playlist_track.next_playlist_track.id,
                ).first()

            prev_playlist_track_obj = models.Playlist_Track.objects.filter(
                playlist_id=playlist_track.playlist_id,
                next_playlist_track=pk,
            ).first()
            new_next_playlist_track_obj = models.Playlist_Track.objects.get(
                id=new_next_playlist_track_id
            )
            prev_of_new_next = models.Playlist_Track.objects.filter(
                playlist_id=playlist_track.playlist_id,
                next_playlist_track=new_next_playlist_track_obj.id,
            ).first()

            if prev_of_new_next is not None:
                prev_of_new_next.next_playlist_track = playlist_track
                prev_of_new_next.save()

            if playlist_track.is_first and old_next_playlist_track_obj is not None:
                old_next_playlist_track_obj.is_first = True
                old_next_playlist_track_obj.save()
                playlist_track.is_first = False
                playlist_track.save()

            if prev_playlist_track_obj is not None:
                prev_playlist_track_obj.next_playlist_track = (
                    old_next_playlist_track_obj
                )
                prev_playlist_track_obj.save()

            if new_next_playlist_track_obj is not None:
                playlist_track.next_playlist_track = new_next_playlist_track_obj
                playlist_track.save()

            return Response({"message": "Track update successfully"})
        except Exception as e:
            logger.error(f"error happened during reoder the track in the playlist {e}")
            return Response(
                "error happened during reoder the track in the playlist",
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

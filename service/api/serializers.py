from rest_framework import serializers

from . import models


class TrackSerializer(serializers.ModelSerializer):
    genres = serializers.StringRelatedField(many=True)
    moods = serializers.StringRelatedField(many=True)
    main_artists = serializers.StringRelatedField(many=True)
    featured_artists = serializers.StringRelatedField(many=True)

    class Meta:
        model = models.Track
        fields = [
            "id",
            "title",
            "length",
            "bpm",
            "genres",
            "moods",
            "main_artists",
            "featured_artists",
            "audio",
            "cover_art",
            "waveform",
            "spotify",
        ]


class PlaylistSerializer(serializers.ModelSerializer):
    genres = serializers.StringRelatedField(many=True)
    moods = serializers.StringRelatedField(many=True)

    class Meta:
        model = models.Playlist
        fields = ["id", "title", "genres", "moods", "created_at", "updated_at"]


class PlaylistTracksSerializer(serializers.ModelSerializer):
    next_playlist_track = serializers.StringRelatedField()
    track_id = serializers.StringRelatedField()
    playlist_id = serializers.StringRelatedField()

    class Meta:
        model = models.Playlist_Track
        fields = [
            "id",
            "track_id",
            "playlist_id",
            "next_playlist_track",
            "created_at",
            "updated_at",
            "is_first",
        ]

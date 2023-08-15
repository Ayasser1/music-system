# Generated by Django 4.1.5 on 2023-08-15 09:59

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_fetch_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='Playlist',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('genres', models.ManyToManyField(related_name='genres', to='api.genre')),
                ('moods', models.ManyToManyField(related_name='moods', to='api.mood')),
            ],
        ),
        migrations.CreateModel(
            name='Playlist_Track',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_first', models.BooleanField(default=False)),
                ('next_playlist_track', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='next_track', to='api.playlist_track')),
                ('playlist_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.playlist')),
                ('track_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.track')),
            ],
            options={
                'unique_together': {('track_id', 'playlist_id')},
            },
        ),
    ]
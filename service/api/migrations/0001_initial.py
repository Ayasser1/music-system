# Generated by Django 3.2 on 2021-04-25 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Mood',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('length', models.IntegerField(default=0)),
                ('bpm', models.IntegerField(default=0)),
                ('featured_artists', models.ManyToManyField(related_name='featured_artist', to='api.Artist')),
                ('genres', models.ManyToManyField(related_name='genre', to='api.Genre')),
                ('main_artists', models.ManyToManyField(related_name='main_artist', to='api.Artist')),
                ('moods', models.ManyToManyField(related_name='mood', to='api.Mood')),
            ],
        ),
    ]
from django.db import models

# Create your models here.


class Blog(models.Model):
    img = models.ImageField(upload_to='pics')
    title = models.CharField(max_length=100)
    date = models.DateField(auto_now=True)
    comment = models.TextField()
    desc = models.TextField()


class Song(models.Model):

    genreChoices = [
        ('PP', 'POP'),
        ('RK', 'ROCK'),
        ('CL', 'CLASSIC'),
        ('ML', 'METAL')
    ]
    img = models.ImageField(upload_to='pics')
    title = models.TextField(max_length=30)
    desc = models.TextField(max_length=30)
    date = models.DateField(auto_now=True)
    genres = models.CharField(max_length=2, choices=genreChoices)
    songs = models.FileField(upload_to='music/')
    artist = models.TextField(max_length=30)




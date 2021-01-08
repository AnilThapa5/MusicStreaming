from django.db import models

# Create your models here.


class Blog(models.Model):
    img = models.ImageField(upload_to='pics')
    title = models.CharField(max_length=100)
    date = models.DateField(auto_now=True)
    comment = models.TextField()
    desc = models.TextField()



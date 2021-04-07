from django.db import models


class Home(models.Model):
    name = models.CharField(max_length=100, blank=True)
    title = models.CharField(max_length=100, blank=True)
    content = models.CharField(max_length=250, blank=True)
    image   = models.ImageField(upload_to='author_image', default='photo_2019-10-25_23-16-15.jpg')

    def __str__(self):
      return self.name  

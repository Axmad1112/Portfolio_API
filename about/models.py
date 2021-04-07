from django.db import models


class About(models.Model):
    title = models.CharField(max_length=100, blank=True)
    content = models.CharField(max_length=1000, blank=True)

    def __str__(self):
        return self.title

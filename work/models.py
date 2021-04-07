from django.db import models

class Work(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=100)
    image = models.ImageField(upload_to="work_image")
    work_content = models.CharField(max_length=200)
    work_link = models.CharField(max_length = 200)

    def __str_(self):
        return self.title

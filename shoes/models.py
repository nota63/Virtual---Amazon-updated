from django.db import models
from tinymce.models import HTMLField


# Create your models here.

class Shoes(models.Model):
    image_url = models.CharField(max_length=5000)
    title = models.TextField()
    price = HTMLField()

    def __str__(self):
        return self.image_url

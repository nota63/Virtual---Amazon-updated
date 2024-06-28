from django.db import models
from tinymce.models import HTMLField


# Create your models here.

class Televisions(models.Model):
    image_url = models.TextField()
    title = models.TextField()
    price = HTMLField()

    def __str__(self):
        return self.image_url

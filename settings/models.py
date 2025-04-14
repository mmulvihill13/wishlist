# models.py
from django.db import models

class Location(models.Model):
    name = models.CharField(max_length=255)
    estimated_delivery_time = models.CharField(max_length=255)
    image_url = models.URLField(max_length=1024)  # URL of the image

    def __str__(self):
        return self.name

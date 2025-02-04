from django.db import models

# Create your models here.

from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    producer = models.CharField(max_length=255)
    duration = models.IntegerField()  # Duration in seconds

    def __str__(self):
        return self.title
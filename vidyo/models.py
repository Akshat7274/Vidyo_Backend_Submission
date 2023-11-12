from django.db import models

# Create your models here.
class ExtractAudio(models.Model):
    username = models.CharField(max_length=30)
    input = models.CharField(max_length=500)
    output = models.CharField(max_length=500)
    timestamp = models.DateTimeField(auto_now_add=True)

class Watermark(models.Model):
    username = models.CharField(max_length=30)
    video = models.CharField(max_length=500)
    image = models.CharField(max_length=500)
    output = models.CharField(max_length=500)
    size = models.CharField(max_length=15)
    position = models.CharField(max_length=15)
    timestamp = models.DateTimeField(auto_now_add=True)
from django.db import models

# Create your models here.
class Simplehireddata(models.Model):
    inputlink = models.URLField(max_length=255)
    outputcsv = models.TextField(blank=True)
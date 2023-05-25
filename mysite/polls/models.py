from django.db import models

# Create your models here.
class Linkedindata(models.Model):
    inputlink = models.URLField(max_length=255)
    outputcsv = models.TextField(blank=True)
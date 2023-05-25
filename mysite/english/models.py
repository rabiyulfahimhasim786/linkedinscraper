from django.db import models

# Create your models here.
class Spellchecker(models.Model):
    inputtext = models.TextField()
    outputtext = models.TextField()
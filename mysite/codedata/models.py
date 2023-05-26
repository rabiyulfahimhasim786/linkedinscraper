from django.db import models

# Create your models here.
class Barcodefile(models.Model):
    inputfile = models.FileField(upload_to='csv_files/')
    pdflink = models.TextField(blank=True)
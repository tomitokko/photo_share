from django.db import models

# Create your models here.
class Photo(models.Model):
    file = models.FileField(upload_to='file')
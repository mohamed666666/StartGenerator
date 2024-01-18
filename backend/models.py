from django.db import models

# Create your models here.

class MediaFile(models.Model):
    image = models.ImageField(upload_to='uploads/images/')
    mp3 = models.FileField(upload_to='uploads/mp3/')

    def __str__(self):
        return f"MediaFile {self.id}"
        
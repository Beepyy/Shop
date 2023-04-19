from django.db import models
from config import settings
#Gallery
class Gallery(models.Model):
    title=models.CharField(max_length=20)
    image=models.ImageField(upload_to=settings.MEDIA_ROOT)
    Description=models.TextField(max_length=450)
    geo=models.TextField(max_length=50)

    def __str__(self):
        return self.title

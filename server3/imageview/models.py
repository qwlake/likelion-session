from django.db import models

class Imageview(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='image/')
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.title[:100]

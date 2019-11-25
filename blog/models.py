from django.db import models


# Create your models here.
class Haber(models.Model):
    baslik = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)
    icerik = models.TextField(max_length=500)

    def __str__(self):
        return self.baslik

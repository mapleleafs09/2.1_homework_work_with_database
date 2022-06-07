from django.db import models


class Phone(models.Model):
    name = models.CharField(max_length=70)
    price = models.FloatField(max_length=20)
    image = models.ImageField()
    release = models.DateField()
    lte = models.BooleanField()
    slug = models.SlugField(unique=True)

    pass

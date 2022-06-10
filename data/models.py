from django.db import models


# Create your models here.
class list(models.Model):

    cars = models.CharField(max_length=150, default='')
    News_Paper = models.CharField(max_length=150, default='')

from django.db import models

# Create your models here.

class macroModel(models.Model):
    height = models.IntegerField(default=0)

class Food(models.Model):
    food = models.CharField(max_length=50)


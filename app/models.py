from django.db import models

# Create your models here.

class macroModel(models.Model):
    protien = models.IntegerField(default=0)
    carbohydrate = models.IntegerField(default=0)
    fat = models.IntegerField(default=0)

class Food(models.Model):
    food = models.CharField(max_length=50)


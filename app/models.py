from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(
        max_length=100
    )
    last_name = models.CharField(
        max_length=100
    )
    total_cal = models.DecimalField(
        max_digits=4, 
        decimal_places=2
        )

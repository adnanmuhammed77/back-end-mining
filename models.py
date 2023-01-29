from django.db import models

# Create your models here.
class product(models.Model):
    name=models.CharField(max_length=200)
    description=models.CharField(max_length=2000)
    price=models.FloatField()
    image=models.CharField(max_length=2500)

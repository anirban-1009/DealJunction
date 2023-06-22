from django.db import models
from users.models import User

class Item(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image_url = models.URLField(null=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name=models.CharField(max_length=255)
    # image=models.CharField(max_length=200)
    image = models.ImageField(upload_to='products/')
    price=models.FloatField()
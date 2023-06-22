from django.db import models
from users.models import User


class Product(models.Model):
    name=models.CharField(max_length=255)
    image_url=models.CharField(max_length=200, null=True)
    image = models.ImageField(upload_to='products/')
    price=models.FloatField()
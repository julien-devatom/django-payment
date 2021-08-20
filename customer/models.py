from django.db import models


# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=64)
    phone = models.CharField(max_length=64)

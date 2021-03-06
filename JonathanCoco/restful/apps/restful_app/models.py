from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Products(models.Model):
    name = models.CharField(max_length=50)
    description  = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

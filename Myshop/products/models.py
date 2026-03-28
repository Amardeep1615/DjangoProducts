from django.db import models

# Create your models here.

class Product(models.Model):
    product_id = models.CharField(max_length=50)
    product_name = models.CharField(max_length=50)
    product_desc = models.TextField(blank=True)
    product_stock = models.PositiveIntegerField(default=0)

def __str__(self):
    return self.name
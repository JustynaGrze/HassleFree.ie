from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    class Meta:
        verbose_name_plural = 'categories'
    category = models.CharField(max_length=254, default='')
    
    def __str__(self):
        return self.category


class Location(models.Model):
    location = models.CharField(max_length=254, default='')
    
    def __str__(self):
        return self.location


class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=0)
    name = models.CharField(max_length=254, default='')
    description = models.TextField()
    location = models.ForeignKey(Location, on_delete=models.CASCADE, default=0)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='images', null=True, blank=True)

    def __str__(self):
        return self.name


    
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone


# Create your models here.
class Category(models.Model):
    class Meta:
        verbose_name_plural = 'categories'
    category = models.CharField(max_length=254, default='')
    default_image = models.ImageField(upload_to='images', null=True, blank=True)
    
    def __str__(self):
        return self.category


class Location(models.Model):
    location = models.CharField(max_length=254, default='')
    
    def __str__(self):
        return self.location


class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=0)
    name = models.CharField(max_length=50, default='')
    description = models.TextField()
    quantity = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(99)])
    location = models.ForeignKey(Location, on_delete=models.CASCADE, default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0.01)])
    image = models.ImageField(upload_to='images', null=True, blank=True)
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('product-detail', kwargs={'pk': self.pk})


    
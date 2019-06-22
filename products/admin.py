from django.contrib import admin
from .models import Product, Location, Category

# Register your models here.
admin.site.register(Product)
admin.site.register(Location)
admin.site.register(Category)
from django.shortcuts import render
from .models import Product

# Create your views here.
def all_products(request):
    products = Product.objects.all()
    placeholder = "placeholder"
    return render(request, "products/products.html", {"products": products, "placeholder": placeholder})
from django.shortcuts import get_object_or_404
from products.models import Category, Location


def product_categories(request):
    
    categories = Category.objects.all()
    
    return {'product_categories': categories}
    
    
def product_locations(request):
    
    locations = Location.objects.all()
    
    return {'product_locations': locations}
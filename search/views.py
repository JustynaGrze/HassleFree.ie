import sys
from django.shortcuts import render
from django.contrib import messages
from django.core.paginator import Paginator
from django.views.generic import ListView

from products.models import Product

# Create your views here.

def do_search(request):
    
    # gather filters
    try:
        q = request.GET['q']
    except:
        q = ""
    
    try:
        cat = list(map(int, request.GET.getlist('cat')))
    except:
        cat = []
    
    try:
        loc = list(map(int, request.GET.getlist('loc')))
    except:
        loc = []
        
    try:
        sort = request.GET['sort']
    except:
        sort = '-date_posted'
    
    # initialise the full list of products
    products = Product.objects.all().exclude(quantity=0)
    
    # start sorting
    if q and cat and loc:
        products = products.filter(name__icontains=q, category__in=cat, location__in=loc)
        
    elif q and cat:
        products = products.filter(name__icontains=q, category__in=cat)
        
    elif q and loc:
        products = products.filter(name__icontains=q, location__in=loc)
        
    elif cat and loc:
        products = products.filter(category__in=cat, location__in=loc)
        
    elif q:
        products = products.filter(name__icontains=q)
        
    elif cat:
        products = products.filter(category__in=cat)
        
    elif loc:
        products = products.filter(location__in=loc)
        
    else:
        messages.info(request, 'Choose filters to perform the search')
    
    paginator = Paginator(products.order_by(sort), 10)
        
    page = request.GET.get('page')

    products_paginated = paginator.get_page(page)
    
    return render(request, "search/search.html", {"products": products_paginated, "q": q, "cat": cat, "loc": loc, "sort": sort})
 
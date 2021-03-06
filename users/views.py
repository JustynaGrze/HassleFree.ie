from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from checkout.models import Order, OrderLineItem


from products.models import Product


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,"Your account has been created! You are now able to log in!")
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})
    
    
@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    # prepare user's transactions
    transactions = Order.objects.filter(user=request.user)
    
    # prepare user's products
    products = Product.objects.filter(user=request.user)
    
    paginator = Paginator(products.order_by('-date_posted'), 9)
        
    page = request.GET.get('page')

    products_paginated = paginator.get_page(page)


    # prerape context
    context = {
        'u_form': u_form,
        'p_form': p_form,
        'transactions': transactions,
        'products': products_paginated,
    }

    return render(request, 'users/profile.html', context)

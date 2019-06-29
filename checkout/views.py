from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import MakePaymentForm, OrderForm
from .models import OrderLineItem
from django.conf import settings
from django.utils import timezone
from products.models import Product
import stripe


# Create your views here.

stripe.api_key = settings.STRIPE_SECRET


@login_required()
def checkout(request):
    if request.method=="POST":
        
        # Set your secret key: remember to change this to your live secret key in production
        # See your keys here: https://dashboard.stripe.com/account/apikeys
        stripe.api_key = settings.STRIPE_SECRET
        
        # Token is created using Checkout or Elements!
        # Get the payment token ID submitted by the form:
        token = request.POST.get('stripeToken')
        
        order_form = OrderForm(request.POST)

        if order_form.is_valid():
 
            order = order_form.save(commit=False)
            order.date = timezone.now()
            order.user = request.user
            order.save()
            
            cart = request.session.get('cart', {})
            total = 0
            for id, quantity in cart.items():
                product = get_object_or_404(Product, pk=id)
                total += quantity * product.price
                order_line_item = OrderLineItem(
                    order = order, 
                    product = product, 
                    quantity = quantity
                    )
                order_line_item.save()
                
            order.total = total
            
            order.save()
                
            try:
                charge = stripe.Charge.create(
                    amount = int(total * 100),
                    currency = "EUR",
                    description = request.user.email,
                    source=token,
                )
            except stripe.error.CardError:
                messages.error(request, "Your card was declined!")
                
            if charge.paid:
                messages.info(request, "You have successfully paid")
                
                for id, quantity in cart.items():
                    product = get_object_or_404(Product, pk=id)
                    
                    product.quantity -= quantity
                    product.save()
                
                request.session['cart'] = {}

                return redirect(reverse('home'))
            else:
                messages.error(request, "Unable to take payment")
        else:
            messages.error(request, "We were unable to take a payment with that card!")
    else:
        order_form = OrderForm()
        
    return render(request, "checkout/checkout.html", {'order_form': order_form, 'publishable': settings.STRIPE_PUBLISHABLE})
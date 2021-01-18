from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings     

from .forms import OrderForm 
from bag.contexts import bag_contents

import stripe 


def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    current_bag = bag_contents(request)
    total = current_bag['grand_total']
    stripe_total = round(total * 100)
    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY,
    )

    order_form = OrderForm()
    template = 'checkout/check_out.html'
    print(intent)
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51IAAZJGUt7s8PIBIfIAg2TDlGMMunb65jyEl7UL6g3Zn5YUK5lxA2NyijN7hxibDNbgLaevadEtJWzs2eyqQqi7200C3jX52QA',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)

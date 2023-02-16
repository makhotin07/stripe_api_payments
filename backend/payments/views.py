import stripe
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView

from payments.models import Item

from django.conf import settings


class ShopListView(ListView):
    model = Item
    template_name = 'ShopList.html'
    context_object_name = 'items'


def buy(request, id):
    YOUR_DOMAIN = 'http://127.0.0.1:8000/'
    item_obj = get_object_or_404(Item, pk=id)
    stripe.api_key = settings.STRIPE_SECRET_KEY
    checkout_session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[
            {
                'price_data': {
                    'currency': 'usd',
                    'unit_amount': int(item_obj.price * 100),
                    'product_data': {
                        'name': item_obj.name,
                    },
                },
                'quantity': 1,
            },
        ],
        metadata={
            "product_id": item_obj.id
        },
        mode='payment',
        success_url=YOUR_DOMAIN + 'success/',
        cancel_url=YOUR_DOMAIN + 'cancel/',
    )

    return JsonResponse({
        'id': checkout_session.id
    })


def item(request, id):
    item_obj = get_object_or_404(Item, pk=id)
    return render(request,
                  'item.html',
                  {'item': item_obj,
                   'stripe_public_key': settings.STRIPE_PUBLIC_KEY})

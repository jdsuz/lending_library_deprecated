from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse 
from products.models import Product
from django.contrib.auth.decorators import login_required
from cart.cart import Cart

@login_required
def cart_add(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    # return HttpResponseRedirect(reverse('products:products'))
    context = {'product': product}
    return render(request, 'products/cart.html', context)
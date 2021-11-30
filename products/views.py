from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse 
from django.contrib.auth.decorators import login_required

from .models import Product
from .forms import ProductForm

def index(request):
	"""The home page for Lending Library"""
	return render(request, 'products/index.html')

def products(request):
	"""Show all products."""
	products = Product.objects.order_by('-date_added')
	context = {'products': products}
	return render(request, 'products/products.html', context)

def product(request, product_id):
	"""Show a single product and all of its fields."""
	product = Product.objects.get(id=product_id)
	entries = product.entry_set.order_by('-date_added')
	context = {'product': product, 'entries': entries}
	return render(request, 'products/product.html', context)

@login_required
def new_product(request):
	"""Add a new product."""
	if request.method != 'POST':
		# No data submitted; create a blank form.
		form = ProductForm()
	else:
		# POST data submitted; process data.
		form = ProductForm(request.POST)
		if form.is_valid():
			new_product = form.save(commit=False)
			new_product.owner = request.user
			new_product.save()
			return HttpResponseRedirect(reverse('products:products'))

	context = {'form': form}
	return render(request, 'products/new_product.html', context)

@login_required
def my_products(request):
	"""Show all of a user's products."""
	products = Product.objects.filter(owner=request.user).order_by('date_added')
	context = {'products': products}
	return render(request, 'products/my_products.html', context)

def borrow_product(request, product_id):
	"""Borrow a product."""
	product = Product.objects.get(id=product_id)

	if request.method != 'POST':
		# Initial request; pre-fill form with the current product info.
		form = ProductForm(instance=product)
	else:
		# POST data submitted; process data.
		form = ProductForm(instance=product, data=request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('products:product', args=[product.id])) 

	context = {'product': product, 'form': form}
	return render(request, 'products/borrow_product.html', context)
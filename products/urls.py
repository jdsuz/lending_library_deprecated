"""Defines url patterns for products."""

from django.urls import path
from . import views

app_name = 'products'
urlpatterns = [
    # Home page.
    path('', views.index, name='index'),

    # Show all products.
    path('products/', views.products, name='products'),

    # Detail page for a single product.
    path('products/<int:product_id>/', views.product, name='product'),

    # Page for adding a new product
    path('products/new_product/', views.new_product, name='new_product'),

    # MyProducts
    path('myproducts/', views.my_products, name='my_products'),

    # Page for borrowing a product
    path('borrow_product/<int:product_id>/', views.borrow_product, name='borrow_product'),

]
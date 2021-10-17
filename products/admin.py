from django.contrib import admin

from products.models import Product, Entry

admin.site.register(Product)
admin.site.register(Entry)

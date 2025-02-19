from django.contrib import admin
from .models import Category, Drink, Order, OrderItem

admin.site.register(Category)
admin.site.register(Drink)
admin.site.register(Order)
admin.site.register(OrderItem)

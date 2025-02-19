from django.shortcuts import render
from .models import Drink

def menu(request):
    drinks = Drink.objects.filter(in_stock=True)
    return render(request, 'order/menu.html', {'drinks': drinks})

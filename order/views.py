from django.shortcuts import render
from .models import Drink

def menu(request):
    coldDrinks = Drink.objects.filter(in_stock=True).filter(category__name='Cold Drinks')
    hotDrinks = Drink.objects.filter(in_stock=True).filter(category__name='Hot Drinks')
    
    return render(request, 'order/menu.html',  {'hotDrinks': hotDrinks , 'coldDrinks': coldDrinks})

def detailed_menu(request, drink_name):
    return render(request, 'order/detailed_menu.html', {'drink_name': drink_name})
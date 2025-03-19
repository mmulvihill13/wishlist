from django.shortcuts import render, get_object_or_404
from .models import Drink

def menu(request):
    coldDrinks = Drink.objects.filter(in_stock=True).filter(category__name='Cold Drinks')
    hotDrinks = Drink.objects.filter(in_stock=True).filter(category__name='Hot Drinks')
    
    return render(request, 'order/menu.html',  {'hotDrinks': hotDrinks , 'coldDrinks': coldDrinks})

def detailed_menu(request, drink_name):
    drink = get_object_or_404(Drink, name=drink_name)
    customizations = {
        'sizes': drink.sizes,
        'milk_options': drink.milk_options,
        'syrup_options': drink.syrup_options,
        'extra_shots': drink.extra_shots,
    }

    return render(request, 'order/detailed_menu.html', {
        'drink': drink,
        'customizations': customizations
    })
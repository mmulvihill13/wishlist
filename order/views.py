from django.shortcuts import render
from .models import Drink
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, get_object_or_404

def menu(request):
    coldDrinks = Drink.objects.filter(in_stock=True).filter(category__name='Cold Drinks')
    hotDrinks = Drink.objects.filter(in_stock=True).filter(category__name='Hot Drinks')
    
    return render(request, 'order/menu.html',  {'hotDrinks': hotDrinks , 'coldDrinks': coldDrinks})

# def detailed_menu(request, drink_name, drink_id):
#     drink = Drink.objects.get(id=drink_id)
#     return render(request, 'order/detailed_menu.html', {'drink_name': drink_name, 'drink_id': drink_id})
def detailed_menu(request, drink_name, drink_id):
    drink = get_object_or_404(Drink, id=drink_id)  # Fetch drink object safely
    return render(request, 'order/detailed_menu.html', {'drink': drink})
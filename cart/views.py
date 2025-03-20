from django.shortcuts import render, get_object_or_404
from .cart import Cart
from order.models import Drink
from django.http import JsonResponse

def cart_view(request): 
    return render(request, "cart/cart.html", {})

def cart_add(request):
    #Get the cart
    cart = Cart(request)
    #test for POST
    if request.POST.get('action') == 'post':
            #GEt stuff
            drink_id = int(request.POST.get('drink_id'))
            #Look up product in DB
            drink = get_object_or_404(Drink, id=drink_id)
            #save to session
            cart.add(drink=drink)

            #Get cart quantity
            cart_quantity = cart.__len__()
            #Retrun response
            #response = JsonResponse({'Drink Name: ': drink.name})
            response = JsonResponse({'qty': cart_quantity})
            return response

def cart_delete(request):
    pass
def cart_update(request):
    pass
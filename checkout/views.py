from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages 
from cart.cart import Cart 

#checkout function
def checkout(request):
    cart = Cart(request)
    # print("Sessino ID: ", request.session.session_key)
    # print("Cart data:", cart)
    cart_drinks = []
    cart_price = 0

    #if there i something in the cart 
    if len(cart) >0 :
        #for each cart key and item in the cart 
        for cart_key, item in cart.cart.items():
            drink_id = cart_key.split('-')[0]

            #get the drink from the db and all of the information of this drink
            from order.models import Drink
            drink = get_object_or_404(Drink, id=drink_id)
            size = item['size']
            milk = item['milk']
            syrup = item['syrup']
            extra_shots = item['extra_shots']
            quantity = item['quantity']
            price = float(item['price']) 
            total_price = price * quantity 

            #add these drinks to the cart
            cart_drinks.append({
            'drink': drink,
            'size': size,
            'milk': milk,
            'syrup': syrup,
            'extra_shots': extra_shots,
            'quantity': quantity,
            'price': price,
            'id': drink_id,
            'total_price': total_price,
        })
        
        #add it to the total cart price
        cart_price += total_price 

    #pass the data
    context = {
        'cart_drinks': cart_drinks,
        'cart_price': cart_price
    }
    return render(request, 'checkout/checkout.html', context)

#function for where the order is going during "process"
def ordered(request):
    if request.method == 'POST':
        #if the cart is in this requested session
        if 'cart' in request.session:
            #get the cart request, and clear it
            cart = Cart(request)
            cart.clear()
        messages.success(request, 'You order has been placed successfully')
        return render(request, 'checkout/ordered.html')
    #get back to the checkout page other wise
    return redirect('checkout:checkout')


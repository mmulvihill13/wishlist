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
    
    locations = [
        {"name": "Becker", "image_url": "https://th.bing.com/th/id/R.621fed752366a5815416b0c987ab10b9?rik=bCXdKnGyi51%2fgQ&pid=ImgRaw&r=0", "estimated_delivery_time": "10 minutes"},
        {"name": "Cafe", "image_url": "https://i.pinimg.com/736x/a2/bc/9d/a2bc9d4d9afd8dd98f65e30d349bfee4.jpg", "estimated_delivery_time": "20 minutes"},
        {"name": "Library", "image_url": "https://www.travelandleisure.com/thmb/gpiEE4EBnn58CFGRqkZoVwzwS4I=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/florida-southern-university-lakeland-COLLEGECAMP0421-94a6a2c98f5e4a91b86cbe2a7ca134f6.jpg", "estimated_delivery_time": "30 minutes"},
    ]

    #pass the data
    context = {
        'cart_drinks': cart_drinks,
        'cart_price': cart_price,
        'locations': locations
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


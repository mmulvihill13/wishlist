from django.shortcuts import render, get_object_or_404
from .cart import Cart
from order.models import Drink
from django.http import JsonResponse
#function that gets the total cart price
#Function that gets all the drinks to display in the cart for the cart.html (the cart summary page)
def cart_view(request): 
    #Get the cart
    cart = Cart(request)
    quantities = cart.get_quants
    cart_price = 0
    
    cart_items = []

    for cart_key, item in cart.cart.items():
        # Extract drink information
        drink_id = cart_key.split('-')[0]  # Get the drink ID from the key
        drink = get_object_or_404(Drink, id=drink_id)
        
        # Get the customizations
        size = item['size']
        milk = item['milk']
        syrup = item['syrup']
        extra_shots = item['extra_shots']
        quantity = item['quantity']
        price = float(item['price']) 
        total_price = float(item['price']) * quantity  # Total price for this item
        # Prepare the item details
        cart_items.append({
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
        cart_price +=total_price
    # Render the cart page with the cart items
    return render(request, "cart/cart.html", {"cart_drinks": cart_items, "quantities":quantities, 'cart_price': cart_price})

#Function that adds a drink the cart 
def cart_add(request):
    cart = Cart(request)
    
    if request.method == 'POST':
        price = request.POST.get('price')
        drink_id = request.POST.get('drink_id') #gather customizations
        drink_qty = request.POST.get('drink_qty')
        size = request.POST.get('size')
        milk = request.POST.get('milk')
        syrup = request.POST.get('syrup')
        extra_shots = request.POST.get('extra_shots') == 'true'  
        
        # find the drink in the database
        drink = get_object_or_404(Drink, id=drink_id)
        
        # key for the item based on customizations 
        cart_key = f"{drink_id}-{size}-{milk}-{syrup}-{'extra' if extra_shots else 'no-extra'}"
        
        # add item to the cart with customizations
        cart.add(drink=drink, size=size, milk=milk, syrup=syrup, extra_shots=extra_shots, quantity =drink_qty, drink_id=drink_id, price=price)
        
        # get cart quantity
        cart_quantity = cart.__len__()

        # Return the updated cart quantity in the response
        return JsonResponse({'qty': cart_quantity})

#Function that deletes the drink from the cart 
def cart_delete(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        #get stuff
        drink_id = request.POST.get('drink_id') #gather customizations
        drink_qty = request.POST.get('drink_qty')
        size = request.POST.get('size')
        milk = request.POST.get('milk')
        syrup = request.POST.get('syrup')
        extra_shots = request.POST.get('extra_shots')  
        
        # find the drink in the database
        drink = get_object_or_404(Drink, id=drink_id)

        #call delete functino in cart 
        cart.delete(drink=drink, size=size, milk=milk, syrup=syrup, extra_shots=extra_shots, quantity =drink_qty, drink_id=drink_id)

        response = JsonResponse({'drink':drink_id})
        return response

#Function that updates the cart wehn the user slects a different quantity in the cart
def cart_update(request):
    # print("POST:", request.POST)
    cart = Cart(request)
    if request.method == 'POST' and request.POST.get('action') == 'post':
        drink_id = request.POST.get('drink_id')
        drink_qty = request.POST.get('drink_qty')

        #get the new sizes
        new_size = request.POST.get('new_size')
        new_milk = request.POST.get('new_milk')
        new_syrup = request.POST.get('new_syrup')
        new_extra_shots = request.POST.get('new_extra_shots')

        #get the original sizes
        size = request.POST.get('size')
        milk = request.POST.get('milk')
        syrup = request.POST.get('syrup')
        extra_shots = request.POST.get('extra_shots')  

        if not drink_id or not drink_qty:
            return JsonResponse({'error': 'Invalid data'}, status=400)

        # find the drink in the database
        drink = get_object_or_404(Drink, id=drink_id)

        #update the qty
        cart.update(
            drink=drink_id, 
            quantity=int(drink_qty),
            size=size,
            milk=milk,
            syrup=syrup,
            new_size=new_size,
            new_milk=new_milk,
            new_syrup=new_syrup,
            extra_shots=extra_shots,
            new_extra_shots = new_extra_shots
        )

        # #update the cart
        # cart.update(drink=drink, quantity=int(drink_qty),  size=size, milk=milk, syrup=syrup,new_size = new_size, new_milk=new_milk, new_syrup=new_syrup,extra_shots=extra_shots)

        #return the response
        return JsonResponse({'qty': drink_qty})

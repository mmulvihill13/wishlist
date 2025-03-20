from django.shortcuts import render, get_object_or_404
from .cart import Cart
from order.models import Drink
from django.http import JsonResponse

def cart_view(request): 
    #Get the cart
    cart = Cart(request)
    
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
        price = float(item['price']) * quantity  # Total price for this item

        # Prepare the item details
        cart_items.append({
            'drink': drink,
            'size': size,
            'milk': milk,
            'syrup': syrup,
            'extra_shots': extra_shots,
            'quantity': quantity,
            'price': price
        })
    
    # Render the cart page with the cart items
    return render(request, "cart/cart.html", {"cart_drinks": cart_items})


def cart_add(request):
    cart = Cart(request)
    
    if request.method == 'POST':
        drink_id = request.POST.get('drink_id') #gather customizations
        size = request.POST.get('size')
        milk = request.POST.get('milk')
        syrup = request.POST.get('syrup')
        extra_shots = request.POST.get('extra_shots') == 'true'  
        
        # find the drink in the database
        drink = get_object_or_404(Drink, id=drink_id)
        
        # key for the item based on customizations 
        cart_key = f"{drink_id}-{size}-{milk}-{syrup}-{'extra' if extra_shots else 'no-extra'}"
        
        # add item to the cart with customizations
        cart.add(drink=drink, size=size, milk=milk, syrup=syrup, extra_shots=extra_shots)
        
        # get cart quantity
        cart_quantity = cart.__len__()

        # Return the updated cart quantity in the response
        return JsonResponse({'qty': cart_quantity})

def cart_delete(request):
    pass
def cart_update(request):
    pass
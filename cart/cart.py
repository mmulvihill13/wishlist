from order.models import Drink
class Cart():
    def __init__(self, request):
        self.session = request.session

        #Get the current session key if it exists
        cart = self.session.get('session_key')

        #If the user is new, no session key, so make one
        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}

        #make sure cart is available on all pages of sit
        self.cart = cart
    
    #Make add function
    def add(self, drink, size, milk, syrup, extra_shots, quantity, drink_id, price):

        quantity = int(quantity)
        extra_text = 'extra' if extra_shots else 'no-extra'

        cart_key = f"{drink.id}-{size}-{milk}-{syrup}-{extra_text}"
        # Check if the drink with these customizations is already in the cart
        if cart_key in self.cart:
            self.cart[cart_key]['quantity'] += quantity
        else:
            # new entry with customizations
            self.cart[cart_key] = {
                'name': drink.name,
                'price': price,  # Convert Decimal to string for JSON compatibility
                'size': size,
                'milk': milk,
                'syrup': syrup,
                'extra_shots': extra_text,
                'quantity': quantity,
                'id': drink_id,
            }
        
        self.session.modified = True

    #number of itmes
    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())
    
    def get_drinks(self):
        # Get all the keys (customized drink entries)
        cart_keys = self.cart.keys()

        # Use the drink IDs from the keys to lookup the actual drinks in the database
        drink_ids = [key.split('-')[0] for key in cart_keys]  # Extract the drink ID from the key
        drinks = Drink.objects.filter(id__in=drink_ids)

        # Return the corresponding drinks
        return drinks
    
    #Get the quantities of the drinks
    def get_quants(self):
        quantities = self.cart
        return quantities
    
    #Get the updated cart
    def update(self, drink, quantity, size, milk, syrup, new_size, new_milk, new_syrup, extra_shots):
        quantity = int(quantity)
        #get the old and new cart ket
        cartkey = f"{drink}-{size}-{milk}-{syrup}-{extra_shots}"
        newkey = f"{drink}-{new_size}-{new_milk}-{new_syrup}-{extra_shots}"
        
        #if the cart key is the same update the quantity
        if cartkey == newkey:
            if cartkey in self.cart:
                self.cart[cartkey]['quantity'] = quantity
        #otherwise update the other feature
        else:
            #if the cart key is in the cart
            if cartkey in self.cart:
                #get the original drink
                original_drink = self.cart[cartkey]
                
                #if the new key is not in the self.cart alreadt
                if newkey not in self.cart:
                    self.cart[newkey] = {
                        'name': original_drink['name'],
                        'quantity': quantity,
                        'price': original_drink['price'],
                        'size': new_size,
                        'milk': new_milk,
                        'syrup': new_syrup,
                        'extra_shots': extra_shots,
                        'id': original_drink['id'] 
                    }
                    #delete the previous cartkey 
                    del self.cart[cartkey]
                else:
                    #if it already exists, add the quantity
                    self.cart[newkey]['quantity'] += quantity
                    #otheriwse delete the previous cartkey
                    del self.cart[cartkey]
        
        self.session.modified = True

    #Function that delets formt he cart class
    def delete(self, drink, size, milk, syrup, extra_shots, quantity, drink_id):
        extra_text = 'extra' if extra_shots else 'no-extra'
        cart_key = f"{drink.id}-{size}-{milk}-{syrup}-{extra_shots}"
        keys_to_delete = [key for key in list(self.cart.keys()) if key.startswith(cart_key)]
        for key in keys_to_delete:
            del self.cart[key]
        self.session.modified = True
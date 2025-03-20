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
    def add(self, drink):
        drink_id = str(drink.id)

        #logic
        if drink_id in self.cart:
            pass
        else:
            self.cart[drink_id] = {'price': str(drink.price)}
        
        self.session.modified = True

    #number of itmes
    def __len__(self):
        return len(self.cart)
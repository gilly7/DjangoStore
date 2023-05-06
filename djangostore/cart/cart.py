class Cart():
    def __init__(self, request):
        
        self.session = request.session
        
        #reurning user - obtain existing key session
        cart = self.session.get('session_key')
        
        #new user - generate a new session
        
        if 'session_key' not in request.session:
            
            cart = self.session['session_key']= {}
            
        self.cart = cart    

























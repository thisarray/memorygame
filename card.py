from pgzero.actor import Actor

# Card is based on an Actor (uses inheritance)
class Card(Actor):

    # Status can be 'back' (turned over) 'front' (turned up) or 'hidden' (already used)
    status = 'back'

    
    def __init__(self, name, back_image, card_image):
        Actor.__init__(self, back_image, (0,0))
        self.name = name
        self.back_image = back_image
        self.card_image = card_image
        
    def turnOver(self):
        if (self.status == 'back'):
            self.status = 'front'
            self.image = self.card_image
        elif (self.status == 'front'):
            self.status = 'back'
            self.image = self.back_image
        # Attempt to turn over a hidden card - ignore
        else:
            return
            
    # Override Actor.draw
    def draw(self):
        if (self.status == 'hidden'):
            return
        Actor.draw(self)

    def hide(self):
        self.status = 'hidden'
        
    # When unhide set it to back image
    def unhide (self):
        self.status = 'back'
        self.image = self.back_image
        
    def isHidden (self):
        if self.status == 'hidden':
            return True
        return False
        
    # Is it turned to face forward
    def isFaceUp (self):
        if self.status == 'front':
            return True
        return False

    def reset (self):
        self.unhide()
                            
    def toString(self):
        return self.name
        
    def setPosition(self, x, y):
        self.x = x
        self.y = y
        
    def equals (self, othercard):
        if self.name == othercard.toString(): 
            return True
        return False
        
    
from timer import Timer

# Status is tracked as a number, but to make the code readable constants are used
STATUS_NEW = 0                  # Game is ready to start, but not running
STATUS_PLAYER1_START = 1
STATUS_PLAYER1_CARDS_1 = 2
STATUS_PLAYER1_CARDS_2 = 3
STATUS_END = 50

# Number of seconds to display high score before allowing click to continue
TIME_DISPLAY_SCORE = 3

class GamePlay:
    
    # These are what we need to track
    score = 0
    

    
    status = STATUS_NEW
    
    # These are the cards that have been turned up. 
    # Should be a positive number which is the index in the array (-1 is not set)
    cards_selected = [-1, -1]
    
    def __init__(self, count_down):
        self.count_down = count_down
        pass
    
    # If game has not yet started
    def isNewGame(self):
        if self.status == STATUS_NEW:
            return True
        return False
        
    def isGameOver(self):
        if self.status == STATUS_END:
            return True
        return False
        
    def setGameOver(self):
        # Add short timer for game over to ensure
        # player gets to see high score
        self.count_down.start_count_down(TIME_DISPLAY_SCORE)
        self.status = STATUS_END
        
    def isGameRunning(self):
        if (self.status >= STATUS_PLAYER1_START and self.status < STATUS_END):
            return True
        return False
        
    def startGame(self):
        self.score = 0
        self.status = STATUS_PLAYER1_START
        
    def setNewGame(self):
        self.status = STATUS_NEW
        
    def isPairTurnedOver(self):
        if (self.status == STATUS_PLAYER1_CARDS_2):
            return True
        return False
        
    # Return the index position of the specified card
    def getCard(self, card_number):
        return self.cards_selected[card_number]
        
    # Point scored, so add score and update status
    def scorePoint(self):
        self.score += 1
        self.status = STATUS_PLAYER1_START
        
    def getScore(self):
        return self.score
        
    # Not a pair - just update status
    def notPair(self):
        self.status = STATUS_PLAYER1_START
        
    # If a card is clicked then update the status accordingly
    def cardClicked(self, card_index):
        if (self.status == STATUS_PLAYER1_START):
            self.cards_selected[0] = card_index
            self.status = STATUS_PLAYER1_CARDS_1
        elif (self.status == STATUS_PLAYER1_CARDS_1):
            self.cards_selected[1] = card_index
            self.status = STATUS_PLAYER1_CARDS_2
        

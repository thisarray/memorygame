# Memory Card Game - PyGame Zero
# This is licensed under GNU GENERAL PUBLIC LICENSE Version 3
# See : https://github.com/penguintutor/memorygame


# If running on a computer that doesn't include . in the Python Search Path
# Includes Raspbian on x86
import sys
sys.path.append('.')

import random
import pygame

from card import Card
from timer import Timer
from gameplay import GamePlay

# These constants are used to simplify the game
# For more flexibility these could be replaced with configurable variables 
# (eg. different number of cards for different difficulty levels)
NUM_CARDS_PER_ROW = 4
X_DISTANCE_BETWEEN_CARDS = 120
Y_DISTANCE_BETWEEN_CARDS = 120
CARD_START_X = 220
CARD_START_Y = 130
TIME_LIMIT = 60

TITLE = "Lake District Memory Game"
WIDTH = 800
HEIGHT = 600

cards_available = {
    'airafalls' : 'memorycard_airafalls',
    'ambleside' : 'memorycard_ambleside',
    'bridgehouse' : 'memorycard_bridgehouse',
    'derwentwater' : 'memorycard_derwentwater',
    'ravenglassrailway' : 'memorycard_ravenglassrailway',
    'ullswater' : 'memorycard_ullswater',
    'weatherstone' : 'memorycard_weatherstone',
    'windermere' : 'memorycard_windermere'
    }

card_back = "memorycard_back"

count_down = Timer(TIME_LIMIT)
game_status = GamePlay(count_down)


def draw():
    screen.fill((220, 220, 220))
    if (game_status.isNewGame()):
        screen.draw.text("Click mouse to start", fontsize=60, center=(WIDTH/2,HEIGHT/2), shadow=(1,1), color=(255,255,255), scolor="#202020")
    if (game_status.isGameOver()):
        screen.draw.text("Game Over\nScore: "+str(game_status.getScore()), fontsize=60, center=(WIDTH/2,HEIGHT/2), shadow=(1,1), color=(255,255,255), scolor="#202020")
    if (game_status.isGameRunning()):
        for card in all_cards:    
            card.draw()
        screen.draw.text("Time remaining: "+str(count_down.get_time_remaining()), fontsize=40, bottomleft=(50,50), color=(0,0,0))
        screen.draw.text("Score: "+str(game_status.getScore()), fontsize=40, bottomleft=(600,50), color=(0,0,0))


# Mouse clicked
def on_mouse_down(pos, button):
    # Only interested in the left button
    if (not button == mouse.LEFT):
        return
    # If new game then this click is to start the game
    if (game_status.isNewGame()):
        game_status.startGame()
        # start the timer
        count_down.start_count_down(TIME_LIMIT)
        dealcards()
        return
    # If game over then this click is to get to new game screen
    if (game_status.isGameOver()):
        # Make sure the timer has reached zero (short delay to see score)
        if (count_down.get_time_remaining()<=0):
            game_status.setNewGame()
        return
        
    ## Reach here then we are in game play

    # First check for both already clicked and this is a click to test
    if (game_status.isPairTurnedOver()):
        if (all_cards[game_status.getCard(0)].equals(all_cards[game_status.getCard(1)])):
            # Add points and hide the cards
            game_status.scorePoint()
            all_cards[game_status.getCard(0)].hide()
            all_cards[game_status.getCard(1)].hide()
            # Check if we are at the end of this level (all cards done)
            if (end_level_reached()):
                dealcards()
        # If not match then turn both around
        else:
            all_cards[game_status.getCard(0)].turnOver()
            all_cards[game_status.getCard(1)].turnOver()
            game_status.notPair()
        return
    
    ## Otherwise we just turn over the next card if clicked 
    for i in range (len(all_cards)):
        if (all_cards[i].collidepoint(pos)):
            # Ignore if card hidden, or has already been turned up
            if (all_cards[i].isHidden() or all_cards[i].isFaceUp()):
                return
            all_cards[i].turnOver()
            # Update status 
            game_status.cardClicked(i)
            
                
    
def update():
    if (game_status.isNewGame()):
        pass
    elif (game_status.isGameOver()):
        pass
    else:
        if (count_down.get_time_remaining()<=0):
            game_status.setGameOver()
        


# Shuffle the cards and update their positions
# Do not draw as this is called before the screen is properly setup
def dealcards():
    # Create a temporary list of card indexes that is then shuffled
    keys = []
    for i in range (len(all_cards)):
        keys.append(i)
    random.shuffle(keys) 
    
    # Setup card positions
    xpos = CARD_START_X
    ypos = CARD_START_Y
    cards_on_row = 0
    for key in keys:
        # Reset (ie. unhide if hidden and display back)
        all_cards[key].reset()
        all_cards[key].setPosition(xpos,ypos)
        xpos += X_DISTANCE_BETWEEN_CARDS
        
        cards_on_row += 1
        # If reached end of row - move to next
        if (cards_on_row >= NUM_CARDS_PER_ROW):
            cards_on_row = 0
            xpos = CARD_START_X
            ypos += Y_DISTANCE_BETWEEN_CARDS
            
# If reach end of level ?
def end_level_reached():
    for card in all_cards:
        if (not card.isHidden()):
            return False
    return True
            
# End of functions - start of initialization code

all_cards = []
# Create individual card objects, two per image
for key in cards_available.keys():
    # Add to list of cards
    all_cards.append(Card(key, card_back, cards_available[key]))
    # Add again (to have 2 cards for each img)
    all_cards.append(Card(key, card_back, cards_available[key]))

dealcards()

    
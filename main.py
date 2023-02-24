"""Python Game called Go Fish

    Returns:
        _type_: _description_
"""
import traceback


class Deck:
    """Deck of playing cards class
    
    """
    def __init__(self):

        self.suits = ['spades', 'hearts', 'diamonds',' clubs']
        self.numbers = ['1','2','3','4','5','6','7','8','9','10','J','Q','K']

        self.deck = []

        for suit in range(len(self.suits)):
            for number in range(len(self.numbers)):
                self.deck.append([self.suits[suit],self.numbers[number]])
              
    def pop(self):
        """returns a card 

        Returns:
            array: containing strings
        """
        try:      
            return self.deck.pop()
        except TypeError:
            return traceback.print_exc()

class Card:
    """Playing Card Class that is made up of a suit, and number
    """ 
    def __init__(self):
        pass
            
            
class Player:
    """Player class
    """
    
    
    def __init__(self):
        self.hand = []
        self.score = []

    
    
        
class GoFish:
    """ The name of the game, it is a card game.
    """
    
    def __init__(self):
        self.deck = Deck()
        self.player = Player()
        self.card = Card()
        self.game_over = False
        self.players = []
        self.starthand = 5
       
    
    def play(self, num_players):
        """ Play method that starts the game.

        Args:
            num_players (_type_): _description_
        """
        
        while self.game_over is False:
            
            
            for player in range(num_players):
                self.players.insert(player, self.player)

            for player in range(self.starthand):    
                
                self.players[player].hand.append(self.deck.pop())
            
            for player in range(num_players):
                print(self.players[player].hand)
              
                
            self.game_over = True


game1 = GoFish()

game1.play(num_players=5)


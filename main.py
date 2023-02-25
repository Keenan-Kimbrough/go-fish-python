import random
import traceback


class Card:
    """Playing Card Class that is made up of a suit, and number
    """ 
    def __init__(self, suit: str, value: str) -> None:
        self.suit = suit
        self.value = value
    
    

class Deck:
    """Deck of playing cards class
    
    """
    def __init__(self):

        suits = ['spades', 'hearts', 'diamonds',' clubs']
        values = ['1','2','3','4','5','6','7','8','9','10','J','Q','K']

        self.deck = []

        for suit in range(len(suits)):
            for value in range(len(values)):
                self.deck.append(Card(suit,value))
              
        random.shuffle(self.deck)
        
    def pop(self):
        """returns a card 

        Returns:
            array: containing strings
        """
        try:      
            card = self.deck.pop()
            return card
        except TypeError:
            return traceback.print_exc()


            
class Player:
    """Player class
    """
    
    
    def __init__(self, id: int):
        self.id = id
        self.hand = []
        self.score = []

    
    
        
class GoFish:
    """ The name of the game, it is a card game.
    """
    
    def __init__(self, num_players: int, hand_size):
        self.deck = Deck()
        self.game_over = False
        self.players = []
        self.hand_size = hand_size
        self.num_players = num_players
        for i in range(num_players):
            self.players.append(Player(i))
                
        for player in self.players:
            for card_number in range(hand_size):
                player.hand.insert(card_number, self.deck.pop())
        
    
    def play(self):
        """ Play method that starts the game.

        Args:
            num_players (_type_): _description_
        """
        
        
       
            
        while self.game_over is False:
            
    
              
                
            self.game_over = True


game1 = GoFish(5,4)

game1.play()



# go fish
# deck, mutliple players, they hands( cards), turns ( state ), game itself( function)

class Deck:
        
        def __init__(self):
    
            self.suits = ['spades', 'hearts', 'diamonds',' clubs']
            self.numbers = ['1','2','3','4','5','6','7','8','9','10','J','Q','K']
    
            self.deck = []
    
            for suit in range(len(self.suits)):
                for number in range(len(self.numbers)):
                    self.deck.append([self.suits[suit],self.numbers[number]])
                
                    
        def pop(self):
            try:
                    
                return self.deck.pop()
            except: 
                print(" No more cards available")
        

class Card:
        def __init__(self):
           pass
            
            
class Player:
    
    hand = []
    score = []
    
    def __init__(self):
        pass
    
    
        
class Go_fish:
    
    
    def __init__(self):
        self.deck = Deck()
        self.player = Player()
        self.card = Card()
        self.game_over = False
        self.players = []
       
    
    def play(self, num_players):
        
        
        while self.game_over == False:
            
            
            for x in range(num_players):
                self.players.insert(x, self.player)

                for y in range(len(self.players)):    
                
                    self.players[y].hand.append(self.deck.pop())
            
            for p in range(4):
                print(self.players[p].hand)
              
                
            self.game_over = True


game1 = Go_fish()

game1.play(num_players=5)


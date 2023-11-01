import copy as cp
import numpy as np


class Player():
    def __init__(self, id):
        self.cards = []
        self.id = id

    def add_card(self, card):
        if card != 0:
            self.cards.append(card)
        self.cards.sort()

    def play_card(self, card):
        if card in self.cards:
            card = self.cards.pop(self.cards.index(card))
            return card
        else:
            return False
    
    def __str__(self):
        self.sort_cards()
        return f"Player {self.id} deck: {', '.join(map(str, self.cards))}"
    
    def sort_cards(self):
        self.cards.sort()

    def has_card(self, card):
        if card in self.cards:
            return 1
        else:
            return 0   


class Board():
    def __init__(self):
        self.board_dic = {
            "♦2": None, "♦3": None, "♦4": None, "♦5": None, "♦6": None, "♦7": None, "♦8": None, "♦9": None,
            "♠A": None, "♣5": None, "♣4": None, "♣3": None, "♣2": None, "♥A": None, "♥K": None, "♦10": None,
            "♠K": None, "♣6": None, "♥5": None, "♥4": None, "♥3": None, "♥2": None, "♥Q": None, "♦Q": None,
            "♠Q": None, "♣7": None, "♥6": None, "♥7": None, "♥8": None, "♥9": None, "♥10": None, "♦K": None,
            "♠10": None, "♣8": None, "♣9": None, "♣10": None, "♣Q": None, "♣K": None, "♣A": None, "♦A": None,
            "♠9": None, "♠8": None, "♠7": None, "♠6": None, "♠5": None, "♠4": None, "♠3": None, "♠2": None
        }

    def __str__(self):
        output = []
        keys = list(self.board_dic.keys())
        
        # Find the maximum length of a tile (key)
        max_tile_length = max(len(key) for key in keys)
        max_status_length = max(len(self.get_tile_status(key)) for key in keys)
        
        for i in range(0, len(keys), 8):
            row = keys[i:i+8]
            
            # Format the tiles to ensure they all have the same width
            tiles = ' | '.join([f"{tile:{max_tile_length}}: {self.get_tile_status(tile):{max_status_length}}" for tile in row])
            
            output.append(tiles)
            output.append('-' * len(tiles))  # Separator line

        return '\n'.join(output)

    def get_tile_status(self, tile):
        """Returns the status of a tile based on its value in board_dic."""
        if self.board_dic[tile] == None:
            return ' - '
        elif self.board_dic[tile] == 1:
            return '(1)'
        elif self.board_dic[tile] == 2:
            return '(2)'
        else:
            return '?'

    def place_card(self, card, player):
        if self.board_dic[card] == None:
            self.board_dic[card] = player
            return 1
        else:
            return 0
        
    def is_free(self, card):
        if self.board_dic[card] == None:
            return 1
        else:
            return 0
        

    def check_for_winner(self):
        # Implement the winning logic here
        if self.board_dic["♦2"] != None:
            return 1
        elif self.board_dic["♦3"] != None:
            return 2
        else:
            return 0
            


class Deck():
    def __init__(self):
        self.cards_list = [
            "♠2", "♠3", "♠4", "♠5", "♠6", "♠7", "♠8", "♠9", "♠10", "♠J", "♠Q", "♠K", "♠A",
            "♦2", "♦3", "♦4", "♦5", "♦6", "♦7", "♦8", "♦9", "♦10", "♦J", "♦Q", "♦K", "♦A",
            "♣2", "♣3", "♣4", "♣5", "♣6", "♣7", "♣8", "♣9", "♣10", "♣J", "♣Q", "♣K", "♣A",
            "♥2", "♥3", "♥4", "♥5", "♥6", "♥7", "♥8", "♥9", "♥10", "♥J", "♥Q", "♥K", "♥A"
        ]
        self.cards_list_without_J = [
            "♠2", "♠3", "♠4", "♠5", "♠6", "♠7", "♠8", "♠9", "♠10", "♠Q", "♠K", "♠A",
            "♦2", "♦3", "♦4", "♦5", "♦6", "♦7", "♦8", "♦9", "♦10", "♦Q", "♦K", "♦A",
            "♣2", "♣3", "♣4", "♣5", "♣6", "♣7", "♣8", "♣9", "♣10", "♣Q", "♣K", "♣A",
            "♥2", "♥3", "♥4", "♥5", "♥6", "♥7", "♥8", "♥9", "♥10", "♥Q", "♥K", "♥A"
        ]
        self.deck = []
        self.reset_deck()

    def __str__(self):
        return str(self.deck)
    
    def reset_deck(self):
        self.deck = cp.deepcopy(self.cards_list_without_J)
        np.random.shuffle(self.deck)

    def draw_card_fom_deck(self):
        if len(self.deck) == 0:
            print("ERROR: Deck is empty")
            return 0
        return self.deck.pop()


class Sequense_game():
    def __init__(self):
        self.board = Board()
        self.deck = Deck()
        self.player1 = Player(1)
        self.player2 = Player(2)
        self.player = {1: self.player1, 2: self.player2}
        self.n_starting_cards = 7
        self.deal_hands(self.n_starting_cards)

    def reset_game(self):
        self.board = Board()
        self.deck = Deck()
        self.player1 = Player(1)
        self.player2 = Player(2)
        self.player = {1: self.player1, 2: self.player2}
        self.deal_hands(self.n_starting_cards)

    def deal_hands(self,n_cards):
        for i in range(0,n_cards):
            self.player1.add_card(self.deck.draw_card_fom_deck())
            self.player2.add_card(self.deck.draw_card_fom_deck())

    def play_card(self, player, card):
        if not (player == 1 or player == 2):
            print("ERROR: Player must be 1 or 2")
            return 0
        if self.player[player].has_card(card):
            if self.board.is_free(card):
                self.board.place_card(card, player)
                self.player[player].play_card(card)
                self.player[player].add_card(self.deck.draw_card_fom_deck())
                print("Player", player, "played", card)
                return 1
            else:
                print("ERROR: Cant play card. Already pin in that spot")
                return 0
        else:
            print("ERROR: Player dont have the card", card)
            return 0
        
    def check_if_won(self):
        return self.board.check_for_winner()
                

class Sequense_game_1_player(Sequense_game):
    def __init___(self):
        super().__init__()

    def bot_player_2_plays_card(self):
        card = self.player2.cards[0]
        self.play_card(2, card)

    def play_then_bot_play(self, player, card):
        out = self.play_card(player, card)
        if not self.check_if_won():
            self.bot_player_2_plays_card()
        return out


    def play_game(self):

        loop = 1
        while(loop):
            print(self.board)
            print("")
            print("Choose card to play:")
            outstr = ""
            for i, card in enumerate(self.player1.cards):
                outstr += f"{i+1}: {card}  "
            print(outstr)
            card = input("What nr card do you want to play? ")
            try:
                if self.player1.has_card(self.player1.cards[int(card)-1]):
                    if self.play_card(1, self.player1.cards[int(card)-1]):
                        if self.check_if_won():
                            break
                        self.bot_player_2_plays_card()
                        if self.check_if_won():
                            break
                    else:
                        print("ERROR: Cant play card.")
                else:
                    print("\nPlayer 1 hand is empty\n")
            except:
                print("No matching card")

        print("GAME OVER")
        print("Player", self.check_if_won(), "won!")
        

        
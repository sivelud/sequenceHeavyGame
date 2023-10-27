import copy as cp
import numpy as np


class GameTester():
    def __init__(self):
        self.judge = Judge()

        self.cards_on_hand = 7

        
        
    
    def sim(self):

        self.judge.deal_hand(self.cards_on_hand)

        cards = self.judge.return_hand("Player 1")

        

        self.judge.play_card(cards[0], "Player 1")


        

        self.judge.print_deck_to_terminal()


class Judge():
    def __init__(self):
        self.board = {
    "ruter 2": None, "ruter 3": None, "ruter 4": None, "ruter 5": None, "ruter 6": None, "ruter 7": None, "ruter 8": None, "ruter 9": None,
    "spar ess": None, "kløver 5": None, "kløver 4": None, "kløver 3": None, "kløver 2": None, "hjerter ess": None, "hjerter konge": None, "ruter 10": None,
    "spar konge": None, "kløver 6": None, "hjerter 5": None, "hjerter 4": None, "hjerter 3": None, "hjerter 2": None, "hjerter dame": None, "ruter dame": None,
    "spar dame": None, "kløver 7": None, "hjerter 6": None, "hjerter 7": None, "hjerter 8": None, "hjerter 9": None, "hjerter 10": None, "ruter konge": None,
    "spar 10": None, "kløver 8": None, "kløver 9": None, "kløver 10": None, "kløver dame": None, "kløver konge": None, "kløver ess": None, "ruter ess": None,
    "spar 9": None, "spar 8": None, "spar 7": None, "spar 6": None, "spar 5": None, "spar 4": None, "spar 3": None, "spar 2": None
}
        self.player1_hand = []
        self.player2_hand = []
        self.deck = []
        self.reset_deck()

    def return_hand(self, player):
        if player == "Player 1":
            return self.player1_hand
        elif player == "Player 2":
            return self.player2_hand
        
        return None

        
    def deal_hand(self,n_cards):
        for i in range(0,n_cards):
            card = self.deck.pop()
            self.player1_hand.append(card)
            card = self.deck.pop()
            self.player2_hand.append(card)


    def print_player_hand(self):
        print("\nPlayer 1 hand:")
        for elem in self.player1_hand:
            print(elem)

        print("\nPlayer 2 hand:")
        for elem in self.player2_hand:
            print(elem)

            

    def reset_deck(self):
        copy_board = cp.deepcopy(self.board)
        for key in copy_board.keys():
            self.deck.append(key)
        np.random.shuffle(self.deck)


    def print_deck_to_terminal(self):
        tiles = cp.deepcopy(self.board)
        i = 0
        printer = ""
        for tile in tiles:
            printer += tile + ": "
            if self.board[tile]:
                printer += "["
                printer += str(self.board[tile])
                printer += "]"
            else:
                printer += "[FREE]"
            i += 1
            if i == 8:
                print(printer)
                i = 0
                printer = ""

    # def remove_card_from_player(self, player, card):

        


    def play_card(self, card, player):
        if player == "Player 1":
            if card in self.player1_hand:
                self.player1_hand.pop(card)

        elif player == "Player 2":
            if card in self.player2_hand:
                self.player1_hand.pop(card)

        else:
            print("player", player, "cant play card: ", card)
            return
        
        
        
        self.board[card] == str(player)
        

    
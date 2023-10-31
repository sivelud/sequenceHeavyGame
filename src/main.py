from engine import Sequense_game


game = Sequense_game()
game.deal_hands(7)
print(game.player1)


card = game.player1.cards[0]

# print(game.play_card(1, card))
game.play_card(1, card)
print(game.board)
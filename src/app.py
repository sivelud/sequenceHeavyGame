


from flask import Flask, render_template, request, jsonify
from game_src.engine import Sequense_game_1_player  # Import your game logic class

import os
print("PATH:")
print(os.getcwd())

app = Flask(__name__, static_url_path='/static', static_folder='static')

# Global game instance
game = Sequense_game_1_player()

# ... [CARD_MAP remains unchanged] ...
CARD_MAP = {
    "♣2": "2_of_clubs",
    "♦2": "2_of_diamonds",
    "♥2": "2_of_hearts",
    "♠2": "2_of_spades",

    "♣3": "3_of_clubs",
    "♦3": "3_of_diamonds",
    "♥3": "3_of_hearts",
    "♠3": "3_of_spades",

    "♣4": "4_of_clubs",
    "♦4": "4_of_diamonds",
    "♥4": "4_of_hearts",
    "♠4": "4_of_spades",

    "♣5": "5_of_clubs",
    "♦5": "5_of_diamonds",
    "♥5": "5_of_hearts",
    "♠5": "5_of_spades",

    "♣6": "6_of_clubs",
    "♦6": "6_of_diamonds",
    "♥6": "6_of_hearts",
    "♠6": "6_of_spades",

    "♣7": "7_of_clubs",
    "♦7": "7_of_diamonds",
    "♥7": "7_of_hearts",
    "♠7": "7_of_spades",

    "♣8": "8_of_clubs",
    "♦8": "8_of_diamonds",
    "♥8": "8_of_hearts",
    "♠8": "8_of_spades",

    "♣9": "9_of_clubs",
    "♦9": "9_of_diamonds",
    "♥9": "9_of_hearts",
    "♠9": "9_of_spades",

    "♣10": "10_of_clubs",
    "♦10": "10_of_diamonds",
    "♥10": "10_of_hearts",
    "♠10": "10_of_spades",

    "♣J": "jack_of_clubs",
    "♦J": "jack_of_diamonds",
    "♥J": "jack_of_hearts",
    "♠J": "jack_of_spades",

    "♣Q": "queen_of_clubs",
    "♦Q": "queen_of_diamonds",
    "♥Q": "queen_of_hearts",
    "♠Q": "queen_of_spades",

    "♣K": "king_of_clubs",
    "♦K": "king_of_diamonds",
    "♥K": "king_of_hearts",
    "♠K": "king_of_spades",

    "♣A": "ace_of_clubs",
    "♦A": "ace_of_diamonds",
    "♥A": "ace_of_hearts",
    "♠A": "ace_of_spades",

    "🃏B": "black_joker",
    "🃏R": "red_joker"
}

@app.route('/')
def index():
    # Convert the game board and player cards for rendering
    board_for_display = {k: CARD_MAP[v] for k, v in game.board_dic.items()}
    player_cards_for_display = [CARD_MAP[card] for card in game.player1.cards]

    return render_template('your_template_name.html', board=board_for_display, player_cards=player_cards_for_display)

@app.route('/play_card', methods=['POST'])
def play_card():
    card = request.json['card']
    player = 1  # Assuming player 1 for singleplayer
    success = game.play_then_bot_play(player, card)
    winner = game.check_if_won()
    
    if success:
        # Return new state or any other relevant data
        updated_cards = game.player1.cards
        return jsonify({'success': True, 'board_str': game.board.__str__(), 'player_cards': updated_cards})
    else:
        return jsonify({'success': False, 'message': 'Cannot play card.'})

@app.route('/reset_game', methods=['POST'])
def reset_game_route():
    try:
        game.reset_game()
        return jsonify({'success': True, 'message': 'Game reset successfully'})
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)})

if __name__ == '__main__':
    app.run(debug=True)

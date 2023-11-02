from flask import Flask, render_template, request, jsonify


from game_src.engine import Sequense_game_1_player  # Import your game logic class


app = Flask(__name__, static_url_path='/static', static_folder='static')

# Global game instance; this is just a simplistic example.
# Ideally, you'd handle game states more efficiently, e.g., with sessions or a database.
game = Sequense_game_1_player()

@app.route('/')
def index():
    """
    Home page for the game.
    """
    return render_template('game.html', player_cards=game.player1.cards, board_str=game.board.__str__())

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


# ... other routes or API endpoints ...

if __name__ == '__main__':
    app.run(debug=True)

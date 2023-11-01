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
    return render_template('game.html', player_cards=game.player1.cards)

@app.route('/play_card', methods=['POST'])
def play_card():
    print("play_card in app.py")

    card = request.json.get('card')  # Change this line
    print("card:", card)
    player = 1  # Assuming player 1 for singleplayer
    success = game.play_card(player, card)
    
    if success:
        # Return new state or any other relevant data
        return jsonify({
            'success': True, 
            'board': game.board.board_dic,
            'player_cards': game.player1.cards  # Adding this line to return updated cards
        })
    else:
        return jsonify({'success': False, 'message': 'Cannot play card.'})



# ... other routes or API endpoints ...

if __name__ == '__main__':
    app.run(debug=True)

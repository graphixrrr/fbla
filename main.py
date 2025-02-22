from flask import Flask, render_template, request, jsonify, session
from game_engine import GameEngine

app = Flask(__name__)
app.secret_key = 'your-secret-key-123'  # Required for session

@app.route('/')
def index():
    # Renders the main game page
    return render_template('game.html')

@app.route('/start_game', methods=['POST'])
def start_game():
    # Initializes a new game by creating a GameEngine instance,
    # storing the initial game state in the session, and returning
    # the description and choices of the current scene
    game = GameEngine()
    # Store game state in session
    session['current_scene'] = game.current_scene
    session['visited_scenes'] = game.visited_scenes

    current_scene = game.get_current_scene()
    return jsonify({
        'description': current_scene['description'],
        'choices': current_scene['choices'],
        'is_end': len(current_scene['choices']) == 0 # Check if the game has ended
    })

@app.route('/make_choice', methods=['POST'])
def make_choice():
    # Processes the user's choice, updates the game state,
    # handles saving and loading, and returns the new scene's
    # description, choices, and end status
    data = request.json
    game = GameEngine()

    # Restore game state from session
    if 'current_scene' in session:
        game.current_scene = session['current_scene']
        game.visited_scenes = session['visited_scenes']

    if 'load' in data:
        # Load a saved game
        game.load_game()
    elif 'save' in data:
        # Save the current game state
        game.save_game()
        return jsonify({'message': 'Game saved successfully!'})
    else:
        # Process user choice and update the game state
        choice_num = int(data['choice'])
        game.make_choice(choice_num)

    # Update session with new game state
    session['current_scene'] = game.current_scene
    session['visited_scenes'] = game.visited_scenes

    current_scene = game.get_current_scene()
    is_end = len(current_scene['choices']) == 0

    return jsonify({
        'description': current_scene['description'],
        'choices': current_scene['choices'],
        'is_end': is_end,
        'congratulations': "Congratulations on completing your cosmic journey!" if is_end else None
    })

if __name__ == '__main__':
    # Starts the Flask application, allowing external access and enabling debugging mode
    app.run(host='0.0.0.0', port=8080, debug=True)
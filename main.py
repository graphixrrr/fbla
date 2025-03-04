
from flask import Flask, render_template, request, jsonify, session
from game_engine import GameEngine
import ascii_art

# Initialize Flask application with configuration
app = Flask(__name__, static_folder='.')
app.secret_key = 'your-secret-key-123'  # Required for session management
app.config['SESSION_TYPE'] = 'filesystem'  # Use filesystem to store session data

@app.route('/')
def index():
    """
    Route handler for the main page that renders the game interface.
    
    Returns:
        HTML template: The game.html template
    """
    # Renders the main game page
    return render_template('game.html')

@app.route('/start_game', methods=['POST'])
def start_game():
    """
    Initializes a new game session when the player starts playing.
    
    Returns:
        JSON: Initial scene data including description and choices
    """
    # Initializes a new game by creating a GameEngine instance
    game = GameEngine()
    # Store game state in session
    session['current_scene'] = game.current_scene
    session['visited_scenes'] = game.visited_scenes

    # Get the first scene data
    current_scene = game.get_current_scene()
    return jsonify({
        'description': current_scene['description'],
        'choices': current_scene['choices'],
        'is_end': len(current_scene['choices']) == 0, # Check if the game has ended
        'ascii_art': current_scene.get('ascii_art', '')  # Include ASCII art if available
    })

@app.route('/stop_game', methods=['POST'])
def stop_game():
    """
    Ends the current game session and clears session data.
    
    Returns:
        JSON: Game over message and status
    """
    # End the game and display a game over message
    session.pop('current_scene', None)  # Remove current scene from session
    session.pop('visited_scenes', None)  # Remove visited scenes from session
    
    return jsonify({
        'description': "You have ended the game. Thank you for playing Cosmic Odyssey!",
        'choices': [],  # No more choices available
        'is_end': True,  # Mark as game end
        'congratulations': "Game Ended",  # End message
        'ascii_art': ascii_art.GAME_OVER  # Show game over ASCII art
    })

@app.route('/make_choice', methods=['POST'])
def make_choice():
    """
    Processes player choices, updates game state, and handles save/load operations.
    
    Returns:
        JSON: Updated scene data or confirmation message
    """
    # Processes the user's choice, updates the game state,
    # handles saving and loading, and returns the new scene's
    # description, choices, and end status
    data = request.json  # Get JSON data from request
    game = GameEngine()  # Create a new game engine instance

    # Restore game state from session if available
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

    # Get updated scene data
    current_scene = game.get_current_scene()
    is_end = len(current_scene['choices']) == 0  # Check if this is an ending

    return jsonify({
        'description': current_scene['description'],
        'choices': current_scene['choices'],
        'is_end': is_end,
        'congratulations': "Congratulations on completing your cosmic journey!" if is_end else None,
        'ascii_art': current_scene.get('ascii_art', '')  # Include ASCII art if available
    })

if __name__ == '__main__':
    # Starts the Flask application when script is run directly
    # Allows external access (0.0.0.0) and enables debugging mode
    app.run(host='0.0.0.0', port=8080, debug=True)

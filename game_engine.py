
import json # Importing JSON module for saving and loading game state
import os  # Importing OS module to check file existence
from story_data import STORY_DATA # Importing story data containing scenes and choices
from ascii_art import SCENE_ART # Importing ASCII art for scenes

class GameEngine:
    """
    Game engine class that manages the game state, player choices,
    and handles saving/loading functionality for the Cosmic Odyssey game.
    """
    def __init__(self):
        """
        Initialize a new game with the starting scene and empty visited scenes list.
        """
        self.current_scene = "start" # The game begins at the 'start' scene
        self.visited_scenes = [] # List to track previously visited scenes

    def get_current_scene(self):
        """
        Retrieves data for the current scene and adds ASCII art if available.
        
        Returns:
            dict: Scene data including description, choices, and ASCII art
        """
        scene_data = STORY_DATA[self.current_scene].copy() # Copy scene data to avoid modifying original data
        # Add ASCII art to the scene if available in SCENE_ART dictionary
        if self.current_scene in SCENE_ART: 
            scene_data['ascii_art'] = SCENE_ART[self.current_scene]
        return scene_data # Return updated scene data

    def make_choice(self, choice_index):
        """
        Process a player's choice and update the game state accordingly.
        
        Args:
            choice_index (int): The index of the chosen option
        """
        current_scene_data = STORY_DATA[self.current_scene] # Get data for the current scene
        # Ensure the choice index is valid before proceeding
        if choice_index < len(current_scene_data["choices"]):
            next_scene = current_scene_data["choices"][choice_index]["next_scene"] # Get next scene from choice
            self.visited_scenes.append(self.current_scene)  # Track the visited scene
            self.current_scene = next_scene # Update current scene to the next one

    def is_game_over(self):
        """
        Check if the current scene is an ending (no more choices available).
        
        Returns:
            bool: True if game is over, False otherwise
        """
        return len(STORY_DATA[self.current_scene]["choices"]) == 0 # Game ends if there are no choices left

    def save_game(self):
        """
        Save the current game state to a JSON file.
        """
        save_data = {
            "current_scene": self.current_scene,  # Store the current scene
            "visited_scenes": self.visited_scenes # Store the visited scenes
        }
        with open("save_game.json", "w") as f: # Open file in write mode
            json.dump(save_data, f) # Save data in JSON format

    def load_game(self):
        """
        Load a previously saved game state from a JSON file.
        
        Returns:
            bool: True if load successful, False otherwise
        """
        try:
            if os.path.exists("save_game.json"): # Check if the save file exists
                with open("save_game.json", "r") as f: # Open file in read mode
                    save_data = json.load(f) # Load saved data
                    self.current_scene = save_data["current_scene"] # Restore current scene
                    self.visited_scenes = save_data["visited_scenes"] # Restore visited scenes
                return True # Successfully loaded game
        except:
            return False # Return False if an error occurs
        return False # Return False if the file doesn't exist

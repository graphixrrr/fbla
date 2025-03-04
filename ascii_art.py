
# ASCII art strings for the Cosmic Odyssey game
# These multiline strings provide visual representations for different game scenes

# ASCII art for the lunar lander spacecraft
LUNAR_LANDER = '''
    .-------------------.
    |  [§] ARTEMIS [§]  |
    |    .-""""""-.    |
    |   /  * ** *  \   |
    |  |  * ### *  |   |
    |   \  * ** *  /   |
    |    '-......-'    |
    |   [==========]   |
    '-------------------'
'''

# ASCII art representing the lunar surface landscape
LUNAR_SURFACE = '''
      .     .        .
    .   .      .    
   .      _    .     .
 .     .-' '-.   .
     /       \     .
   .           .
      .     .
'''

# ASCII art showing a moon cavern with detailed structure
MOON_CAVERN = '''
          /\\/\\
     ____/  \  \____
    /   /\   \   \  \\
   /___/  \___\   \  \\
   |  | () |  |    |()|
   |()|    |()|    |  |
   |  |    |  |    |  |
   |  |    |  |    |  |
'''

# ASCII art for the game over screen
GAME_OVER = '''
   _____                         ____                 
  / ____|                       / __ \\                
 | |  __  __ _ _ __ ___   ___ | |  | |_   _____ _ __ 
 | | |_ |/ _` | '_ ` _ \\ / _ \\| |  | \\ \\ / / _ \\ '__|
 | |__| | (_| | | | | | |  __/| |__| |\\ V /  __/ |   
  \\_____|\\__,_|_| |_| |_|\\___| \\____/  \\_/ \\___|_|   
'''

# Dictionary mapping scene names to their corresponding ASCII art
# This allows easy access to the appropriate art for each game scene
SCENE_ART = {
    "start": """
    .  ･ ｡ﾟ☆ ･ ｡｡･
      ･ﾟ★｡ ･ﾟ･｡
    /＼｡･ﾟ･｡･ﾟ☆
   /  \\  ･｡･ﾟ･
  /    \\ ﾟ･｡･ﾟ
 /======\\  ･
| ARTEMIS |
""",
    "computer_check": """
 ___________
|  MISSION  |
|  ■■■□□□  |
|===========|
""",
    "examine_surface": """
   .-'-.
 .'     '.
(    ^    )
 '.     .'
   '---'
""",
    "enter_cavern": MOON_CAVERN,
    "deeper_exploration": MOON_CAVERN,
    "first_steps": LUNAR_SURFACE,
    "move_to_signal": LUNAR_SURFACE,
    "game_over": GAME_OVER,
    "final_discovery": GAME_OVER,
    "report_discovery": GAME_OVER
}

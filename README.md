# Snake-Game

## How the Game Works
### Objective
The objective of the game is to control a snake and eat as many pieces of food as possible. Each time the snake eats food, it grows longer, and the player's score increases. The game ends if the snake collides with the boundaries of the game screen or itself.

### Setup
The game is set up to run on a 600x600 pixel square grid. The initial game setup is as follows:

-Game Screen: The game screen is a square grid with dimensions of 600x600 pixels. This grid serves as the play area for the snake to move around and interact with food.

-Snake Initialization: The snake starts in the center of the grid and faces the default direction, which is typically right. The snake initially consists of three segments.

-Food Generation: Food items are randomly placed on the grid. When the snake’s head collides with the food, it eats it, grows longer by one segment, and a new food item appears in a random position on the grid

### Gameplay Mechanics
**Snake Movement:**
The snake continuously moves in the direction it was last instructed to go.
The player controls the direction of the snake using the arrow keys (Up, Down, Left, Right).

**Eating Food:**
Food items are small red squares that randomly appear on the grid.
Every time the snake’s head eats a food item, it grows longer, and the player's score increases.

**Growing and Scoring:**
With each food item consumed, the snake grows by adding a new segment to its tail.
The player's score increases every time the snake eats food.

**Game Over Conditions:**
The game ends if the snake collides with the boundaries of the grid or itself.
After the game ends, players can press the R key to restart the game.

### Features
-**Color Scheme:**

    -Snake: Green
    
    -Food: Red
    
    -Background: Black
    
    -Game Over Text: White
    
-**User Interaction:**
    Arrow keys (Up, Down, Left, Right) control the snake’s movement.
    R key to restart the game after a Game Over.
    
-**Score Display:** The score increases as the snake eats food and is shown in the top-left corner.

-**Game Over Message:** When the game ends, a "GAME OVER" message appears, and the player can press R to restart.

### Future Improvements

-Increasing Difficulty: Gradually increase the snake's speed as it grows longer.

-Obstacles: Add static or moving obstacles to the grid to increase difficulty.

-Levels: Implement multiple levels with different goals or grid sizes.

-High Scores: Save and display the highest score across sessions.

# Installation

## Requirements

1 - Python 3.x (Download from Python's official website).

2 - Tkinter (pre-installed with Python in most distributions).


## Installation Steps
**-Clone the repository:**
             https://github.com/Meghanamajji/Snake-Game-Tkinter.git

**-Navigate into the project directory:**
             Snake-Game-Tkinter

**-Make sure you have Python 3.x and Tkinter installed**

             Verify Python :python --version
             
             Verify Tkinter:import tkinter
             
                            print(tkinter.TkVersion)
                       
**-Run the game:**
            snake_game.py



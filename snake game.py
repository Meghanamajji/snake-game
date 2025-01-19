import tkinter as tk
import random

class SnakeGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Snake Game by meghana")
        self.canvas = tk.Canvas(self.master, width=600, height=400, bg="black")
        self.canvas.pack()
        
        # Initial game settings
        self.snake = [(100, 100), (90, 100), (80, 100)]  # Initial snake position
        self.food = None
        self.direction = 'Right'
        self.game_over = False
        self.snake_size = 10
        
        self.create_food()
        self.update_snake()
        self.master.bind("<KeyPress>", self.change_direction)
        self.run_game()

    def run_game(self):
        if not self.game_over:
            self.move_snake()
            self.check_collisions()
            self.update_snake()
            self.check_food_collision()
            self.master.after(100, self.run_game)  # Repeat every 100ms

    def create_food(self):
        food_x = random.randint(0, 59) * self.snake_size
        food_y = random.randint(0, 39) * self.snake_size
        self.food = (food_x, food_y)
        self.canvas.create_rectangle(food_x, food_y, food_x + self.snake_size, food_y + self.snake_size, fill="red")

    def move_snake(self):
        head_x, head_y = self.snake[0]

        if self.direction == 'Right':
            head_x += self.snake_size
        elif self.direction == 'Left':
            head_x -= self.snake_size
        elif self.direction == 'Up':
            head_y -= self.snake_size
        elif self.direction == 'Down':
            head_y += self.snake_size

        # Add new head to snake body and remove the tail
        new_head = (head_x, head_y)
        self.snake = [new_head] + self.snake[:-1]

    def update_snake(self):
        self.canvas.delete("snake")  # Clear previous snake
        for segment in self.snake:
            x, y = segment
            self.canvas.create_rectangle(x, y, x + self.snake_size, y + self.snake_size, fill="green", tags="snake")

    def change_direction(self, event):
        if event.keysym == 'Right' and self.direction != 'Left':
            self.direction = 'Right'
        elif event.keysym == 'Left' and self.direction != 'Right':
            self.direction = 'Left'
        elif event.keysym == 'Up' and self.direction != 'Down':
            self.direction = 'Up'
        elif event.keysym == 'Down' and self.direction != 'Up':
            self.direction = 'Down'

    def check_collisions(self):
        head_x, head_y = self.snake[0]

        # Check for collision with walls
        if head_x >= 600 or head_x < 0 or head_y >= 400 or head_y < 0:
            self.game_over = True
            self.canvas.create_text(300, 200, text="GAME OVER", fill="white", font=("Arial", 24))

        # Check for collision with itself
        if len(self.snake) != len(set(self.snake)):
            self.game_over = True
            self.canvas.create_text(300, 200, text="GAME OVER", fill="white", font=("Arial", 24))

    def check_food_collision(self):
        head_x, head_y = self.snake[0]
        food_x, food_y = self.food

        if head_x == food_x and head_y == food_y:
            self.snake.append(self.snake[-1])  # Add a new segment to the snake
            self.canvas.delete("food")  # Remove the old food
            self.create_food()  # Create a new food

# Create the game window
root = tk.Tk()
game = SnakeGame(root)
root.mainloop()

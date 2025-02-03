# Create a function to make a blank grid (just dots)
def initial_grid(rows=10, cols=10):
    grid = [['.' for _ in range(cols)] for _ in range(rows)]
    return grid

# Include this 2nd function to visualise the blank grid
def print_grid(grid):
    for row in grid:
        print(' '.join(row))

# Want to see what the previous 2 functions did.  Plus, personalise the presentation a bit.
grid = initial_grid()
print('The Pyladies\' Slither Sisters present: ')
print_grid(grid)
print('Welcome to our version of Snake!')

# Step 3 & 4: Interactive Movement Loop

def move_snake_safe(snake, direction, grid_size=10):
    head_x, head_y = snake[-1]
    
    if direction == 'n':
        new_head = (head_x - 1, head_y)
    elif direction == 's':
        new_head = (head_x + 1, head_y)
    elif direction == 'e':
        new_head = (head_x, head_y + 1)
    elif direction == 'w':
        new_head = (head_x, head_y - 1)
    else:
        print("Invalid direction! Use 'n', 's', 'e', or 'w'.")
        return False  # Invalid direction
    
    # Check if the new position is out of bounds
    if not (0 <= new_head[0] < grid_size and 0 <= new_head[1] < grid_size):
        print("Invalid move: Out of bounds!")
        return False
    
    # Check if the new position collides with the snake itself
    if new_head in snake:
        print("Invalid move: Collision detected!")
        return False
    
    snake.append(new_head)
    snake.pop(0)  # Maintain length
    return True

def print_grid(snake, grid_size=10):
    grid = [['.' for _ in range(grid_size)] for _ in range(grid_size)]
    for x, y in snake:
        grid[x][y] = 'X'
    for row in grid:
        print(" ".join(row))

def interactive_snake_game():
    snake = [(0,0), (0,1), (0,2)]  # Initial snake position
    grid_size = 10
    
    while True:
        print_grid(snake, grid_size)
        direction = input("Enter move direction (n/s/e/w) or 'end' to stop: ")
        if direction == 'end':
            break
        
        if not move_snake_safe(snake, direction, grid_size):
            print("Try a different move.")
    
    print("Game over! Thanks for playing.")

# Run the interactive game
interactive_snake_game()

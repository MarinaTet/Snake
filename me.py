def create_grid(rows, cols):
    # Initialize the grid with dots
    grid = [['.' for _ in range(cols)] for _ in range(rows)]
    return grid

def draw_map(coordinates, rows=10, cols=10):
    # Create the grid
    grid = create_grid(rows, cols)
    
    # Place 'X' on the grid at the given coordinates
    for row, col in coordinates:
        if 0 <= row < rows and 0 <= col < cols:  # Check bounds
            grid[row][col] = 'X'
    
    return grid

# Example usage
coordinates = [(5, 5), (1, 0), (2, 2), (4, 3), (8, 9), (8, 9)]
grid = draw_map(coordinates)

# Print the grid
for row in grid:
    print(' '.join(row))

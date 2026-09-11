grid = [
    [0,0,0,0],
    [0,1,0,0],
    [0,0,1,0],
]
robot = (0,0)
for row in range(len(grid)):
    for col in range(len(grid[0])):
        
        if (row, col) == robot:
            print("R", end=" ")
        
        elif grid[row][col] == 1:
            print("#", end=" ")
        
        else:
            print(".", end=" ")
    
    print()
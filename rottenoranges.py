def orangesRotting(self, grid: List[List[int]]) -> int:

    # Initializing rows and columns of grid
    rows = len(grid)
    cols = len(grid[0])

    # Initializing counter for 2 purposes
    # 1 - as a return for how many minutes passed
    # 2 - as a way to know which oranges have been rotten per minute
    counter = 2

    # Initializing boolean to know when to exit the spread of rotten oranges
    needsChange = True

    while(needsChange):
        # Boolean will change by the end of the loop
        needsChange = False

        for i in range(rows):
            for j in range(cols):
                # If the orange is rotten, spread to all fresh oranges directionally adjacent (if possible)
                if(grid[i][j] == counter):
                    
                    
                    # Top
                    if(i > 0):
                        if(grid[i-1][j] == 1):
                            grid[i-1][j] = counter + 1
                            needsChange = True
                    # Bottom
                    if(i < rows-1):
                        if(grid[i+1][j] == 1):
                            grid[i+1][j] = counter + 1
                            needsChange = True
                    # Left
                    if(j > 0):
                        if(grid[i][j-1] == 1):
                            grid[i][j-1] = counter + 1
                            needsChange = True
                    # Right
                    if(j < cols-1):
                        if(grid[i][j+1] == 1):
                            grid[i][j+1] = counter + 1
                            needsChange = True
                    

        if(needsChange == True):
            counter += 1
        else:
            needsChange = False
    for i in range(rows):
        if(1 in grid[i]):
            return -1
    
    return counter-2
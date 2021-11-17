import numpy as np
import graphics as gp
from time import sleep, thread_time, thread_time_ns
from settings import *

#Settings: CONSTANTS
window_x, window_y = grid_x * scale, grid_y * scale
gridSize = grid_x * grid_y

#Game variables
grid = None
window = None
cellColor = gp.color_rgb(255, 255, 0)
backgroundColor = gp.color_rgb(50, 50, 50)
 
#Generate grid for game
#Grid is 2 length and width bigger for side and edge cases
def CreateGame():
    generatedGrid = np.zeros( (grid_x, grid_y))
    lives = np.random.randint(0, gridSize - 1, int(gridSize * startinglives))
    
    for i in lives:
        generatedGrid[i % grid_x][int(i / grid_x)] = 1
    
    return generatedGrid

#Apply game of life constraits to grid
#alive cells with 2 or 3 neighbours live, rest die
#dead cells with 2 or 3 neighours revive
def UpdateGame():
    grid_copy = grid.copy()
    #timeStart = thread_time()
    
    for x in range(grid_x):
        for y in range(grid_y):
            counter = 0
            
            #check bounds for current cell
            leftbound = (x - 1) >= 0
            rightbound = (x + 1) < grid_x
            topbound = (y - 1) >= 0
            bottombound = (y + 1) < grid_y
            
            #left side
            if leftbound:
                counter += grid[x - 1][y]
                
                #top left
                if topbound:
                    counter += grid[x - 1][y - 1]
                #botton left
                if bottombound:
                    counter += grid[x - 1][y + 1]
            
            #right side
            if rightbound:
                counter += grid[x + 1][y]
                
                #top right
                if topbound:
                    counter += grid[x + 1][y - 1]
                
                #bottom left
                if bottombound:
                    counter += grid[x + 1][y + 1]
                    
            #top
            if topbound:
                counter += grid[x][y - 1]
                
            #bottom
            if bottombound:
                counter += grid[x][y + 1]
            
            if grid[x][y] == 1:
                if (counter < 2) or (counter > 3):
                    grid_copy[x][y] = 0
            else:
                if counter == 3:
                    grid_copy[x][y] = 1
                    
    #print((thread_time() - timeStart) * 1000)
    
    #if timeStart < delay / 1000:
    #    sleep(delay / 1000 - timeStart)
    
    return grid_copy

#Take new grid, reset and update window
#Draw white rectangle for alive cells in grid cell
def DisplayGrid():
    timeStart = thread_time()
    for i in list(window.items):
        i.undraw()
    
    for x in range(grid_x):
        for y in range(grid_y):
            if grid[x][y] == 1:
                life = gp.Rectangle(gp.Point(x * scale,y * scale), gp.Point(x * scale + scale, y * scale + scale))
                life.setFill(cellColor)
                life.draw(window)
            
    print((thread_time() - timeStart) * 1000)
    window.update()

def ChangeCellState(mouseLocation):
    grid_copy = grid.copy()
    x = int(mouseLocation.getX() / scale)
    y = int(mouseLocation.getY() / scale)
    
    if grid_copy[x][y] == 1:
        grid_copy[x][y] = 0
    else :
        grid_copy[x][y] = 1
    
    return grid_copy

if __name__ == '__main__':
    grid = CreateGame()
    
    window = gp.GraphWin("Conway's Game of Life", window_x, window_y,autoflush = False)
    window.setBackground(backgroundColor)
    
    DisplayGrid()
    
    isClicked = None
    isKeyed = None
    stepper = False
    exit = False
    while not exit:
        isClicked = window.checkMouse()
        isKeyed = window.checkKey()
        
        if not stepper:
            grid = UpdateGame()
            DisplayGrid()
            
        if isKeyed == 'q':
            exit = True
        if isKeyed == 's':
            stepper = not stepper
        if (stepper and isKeyed == 'd'):
            grid = UpdateGame()
            DisplayGrid()
        if (stepper and isClicked):
            grid = ChangeCellState(isClicked)
            DisplayGrid()
        
    window.close()
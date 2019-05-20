# Based on code at:
# http://programarcadegames.com/python_examples/f.php?file=array_backed_grid.py

# 1 - Import library
import pygame
from pygame.locals import *

# 2 - Initialize the game
boardsize = (512, 512)
screen=pygame.display.set_mode(boardsize)
width, height, margin = 100, 100, 2

BLACK = (0, 0, 0)
WHITE = (255,255,255)
RED = (255, 0, 0)

## 2D array (list of lists)
grid=[]
for row in range(5):
    grid.append([])
    for column in range(5):
        grid[row].append(0)

pygame.init()
player=pygame.image.load('gunther.jpg').convert()
trash=pygame.image.load('trash.png').convert()
trash2=pygame.image.load('trash2.jpg').convert()
clock=pygame.time.Clock()

# 4 - set up variables
numlitter = 2
grid[3][2]=1
grid[2][4]=2
grid[0][1]=1
grid[0][0]=3 #player start

# 5 - keep looping through until condition met
while (numlitter > 0):

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      done = True
    elif event.type == pygame.MOUSEBUTTONDOWN:
      pos = pygame.mouse.get_pos()
      column = pos[0]
      row = pos[1]
      grid[row][column] = 1
      print("Click ", pos, "Grid coordinates: ", row, column)
  screen.fill(BLACK)        
      
  # Draw the grid
  for row in range(5):
      for column in range(5):
          color = WHITE             
          pygame.draw.rect(screen,color,
                           [(margin + width) * column + margin,
                            (margin + height) * row + margin,
                            width, height])
          if grid[row][column] == 1:  #trash location
              screen.blit(trash,((margin+width)*column + margin,
                                 (margin+height)*row+margin))
          if grid[row][column] == 2:  #trash2 location
              screen.blit(trash2,((margin+width)*column + margin,
                                 (margin+height)*row+margin))
          if grid[row][column] == 3:  #player location
              screen.blit(player,((margin+width)*column + margin,
                                 (margin+height)*row+margin))

  clock.tick(60)

  #redraw board
  pygame.display.flip()

pygame.quit()

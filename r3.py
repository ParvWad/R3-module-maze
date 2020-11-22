import pygame
import random
import time

WIDTH = 1200
HEIGHT = 1200
FPS = 60
WHITE = (255, 255, 255)
GREEN = (0,255,0)
BLUE = (0,0,225)
YELLOW=(255,255,0)
PURPLE = (128,0,128)

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("R3 Milestone 1 maze")
clock = pygame.time.Clock()

x = 0  #x axis storage
y = 0  #y axis
grid = []
visited = []
stack = [] #active cells
n = 30 #size of the grid
w = 20

def build_grid(x,y,w):
    for i in range(1,n+1):
        x = 20
        y = y+w            #new row
        for j in range (1,n+1):                 #drawing base grid
            pygame.draw.line(screen,WHITE,[x,y],[x+w,y])
            pygame.draw.line(screen, WHITE,[x+w,y],[x+w,y+w] )
            pygame.draw.line(screen, WHITE, [x,y+w], [x,y])
            pygame.draw.line(screen, WHITE, [x+w, y+w], [x,y+w])
            grid.append((x,y))
            x += w
def push_up(x,y):
    pygame.draw.rect(screen,BLUE, (x+1, y-w +1, w-1, 2*w-1),0)     #functions for drawing maze
    pygame.display.update()
def push_down(x,y):
    pygame.draw.rect(screen, BLUE, (x +  1, y + 1, w-1, 2*w-1), 0)
    pygame.display.update()
def push_left(x,y):
    pygame.draw.rect(screen, BLUE, (x - w +1, y +1, 2*w-1, w-1), 0)
    pygame.display.update()
def push_right(x,y):
    pygame.draw.rect(screen,BLUE, (x +1, y +1, 2*w-1, w-1), 0)
    pygame.display.update()



def backtracking_cell(x, y):
    pygame.draw.rect(screen, BLUE, (x +1, y +1, w-2, w-2), 0)        # used to re-colour the path after single_cell
    pygame.display.update()                                        # has visited cell


def carve_out_maze(x,y):
    stack.append((x,y))
    visited.append((x,y))
    while len(stack) > 0:                                          #main loop for moving
        cell = []
        if (x + w, y) not in visited and (x + w, y) in grid:       # choosing right left down or up
            cell.append("right")

        if (x - w, y) not in visited and (x - w, y) in grid:
            cell.append("left")

        if (x , y + w) not in visited and (x , y + w) in grid:
            cell.append("down")

        if (x, y - w) not in visited and (x , y - w) in grid:
            cell.append("up")

        if len(cell) > 0:
            cell_chosen = (random.choice(cell))

            if cell_chosen == "right":                    #code for moving right
                push_right(x, y)
                x = x + w
                visited.append((x, y))
                stack.append((x, y))

            elif cell_chosen == "left":                     #code doe moving left
                push_left(x, y)
                x = x - w
                visited.append((x, y))
                stack.append((x, y))

            elif cell_chosen == "down":                      #code for moving down
                push_down(x, y)
                y = y + w
                visited.append((x, y))
                stack.append((x, y))

            elif cell_chosen == "up":               #code for moving up
                push_up(x, y)
                y = y - w
                visited.append((x, y))
                stack.append((x, y))
        else:
            x, y = stack.pop()



x, y = 20, 20                     # starting position of grid
build_grid(40, 0, 20)
carve_out_maze(x,y)


done = False
while not done:         #main loop
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True


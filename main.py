import pygame
from pygame.locals import *

pygame.init()
window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Tetris")

# Game board dimensions
board_width = 10
board_height = 20
grid_size = 30
collisoin_matrix = [[0 for _ in range(board_width)] for _ in range(board_height)]

# Calculate the x and y coordinates of the top-left corner of the grid
grid_x = (window_width - board_width * grid_size) // 2
grid_y = (window_height - board_height * grid_size) // 2

blocks = {
    'I': {"shape": [[1],[1],[1],[1]], "sprite": pygame.image.load('pieces/I.png'), "rotate": True},
    'O': {"shape": [[1,1],[1,1]], "sprite": pygame.image.load('pieces/O.png')},
    'Z': {"shape": [[1,1,0],[0,1,1]], "sprite": pygame.image.load('pieces/Z.png'), "rotate": True},
}

clock = pygame.time.Clock()
fps_font = pygame.font.Font(None, 24)
fps_counter = 0

# Set up the 100-tick system
TICK_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(TICK_EVENT, 10)
tick = 0

# Game loop
running = True
y = 0
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == TICK_EVENT:
            # Move the piece down one grid square every tick
            tick += 1
            if tick % 10 == 0:
                print(clock.get_fps())
            if tick % 100 == 0:
                y += 1

    # Draw the game board and the piece
    for i in range(board_height):
        for j in range(board_width):
            pygame.draw.rect(window, (50, 50, 50), (grid_x + j * grid_size, grid_y + i * grid_size, grid_size, grid_size))
            pygame.draw.rect(window, (30, 30, 30), (grid_x + 2 + j * grid_size, grid_y + 2 + i * grid_size, 26, 26))

    window.blit(blocks['Z']["sprite"], ((window_width - len(blocks['Z']["shape"][0]) * grid_size) // 2, grid_size * y))

    pygame.display.update()

    # Limit the frame rate
    clock.tick(240)
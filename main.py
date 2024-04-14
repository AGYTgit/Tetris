import pygame
from pygame.locals import *
import sprites

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

clock = pygame.time.Clock()
fps_font = pygame.font.Font(None, 24)
fps_counter = 0

# Game loop
running = True
y = 0
while running:
    if pygame.time.get_ticks() % 500 == 0:
        y += 1
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    

    # Draw the game board and the piece
    # for i in range(board_height):
    #     for j in range(board_width):
    #         pygame.draw.rect(window, (50, 50, 50), (grid_x + j * grid_size, grid_y + i * grid_size, grid_size, grid_size))
    #         pygame.draw.rect(window, (30, 30, 30), (grid_x + 2 + j * grid_size, grid_y + 2 + i * grid_size, 26, 26))

    
    window.blit(sprites.blocks['I']["sprite"], ((window_width - 2 * grid_size) // 2, grid_size * y))
    
    pygame.display.update()
    print(clock.get_fps())

    # Limit the frame rate
    clock.tick(10000)
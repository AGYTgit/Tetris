import pygame
from pygame.locals import *
import random

import block


# Define constants for the key presses
DOWN_KEY = pygame.K_DOWN
LEFT_KEY = pygame.K_LEFT
RIGHT_KEY = pygame.K_RIGHT

pygame.init()
window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Tetris")


# Game board dimensions
board_width = 10
board_height = 20
grid_size = 30


grid_matrix = [[1 for _ in range(board_width)] for _ in range(board_height)]


spawn_area_x = (window_width / 2) - (4 // 2) * grid_size
spawn_area_y = 0


# Calculate the x and y coordinates of the top-left corner of the grid
grid_x = (window_width - board_width * grid_size) // 2
grid_y = (window_height - board_height * grid_size) // 2


clock = pygame.time.Clock()


# Set up the 100-tick system
TICK_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(TICK_EVENT, 10)
tick = 0


def draw_grid(grid_matrix):
    for i in range(board_height):
        for j in range(board_width):
            if grid_matrix[i][j] == 1:
                pygame.draw.rect(window, (50, 50, 50), (grid_x + j * grid_size, grid_y + i * grid_size, grid_size, grid_size))
                pygame.draw.rect(window, (30, 30, 30), (grid_x + 2 + j * grid_size, grid_y + 2 + i * grid_size, 26, 26))
                print(i, j)
    print("---")

    for i in range(board_height):
        for j in range(board_width):
            grid_matrix[i][j] = 0


draw_grid(grid_matrix)


def update_grid_matrix():
    for i in range(len(active_piece.shape)):
        for j in range(len(active_piece.shape[0])):
            grid_matrix[int(active_piece.pos_y_old / 30 + i)][int((active_piece.pos_x - grid_x) / 30 + j)] = 1

active_piece = block.I(spawn_area_x, spawn_area_y)

# Game loop
running = True
y = 0
move_delay = 0  # Initialize move delay counter
move_speed = 30  # Adjust this value to control the speed of horizontal movement
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == TICK_EVENT:
            # Move the piece down one grid square every tick
            tick += 1
            # if tick % 10 == 0:
            #     print(clock.get_fps())

            if tick % 500 == 0:
                random_piece = random.randint(0,2)
                # active_piece = block.I(spawn_area_x, spawn_area_y)

            if tick % 100 == 0:
                active_piece.increment_y_by(grid_size)
                update_grid_matrix()
                draw_grid(grid_matrix)


                window.blit(pygame.image.load(active_piece.sprite_path), (active_piece.pos_x, active_piece.pos_y))

                pygame.display.update()
                

    # Limit the frame rate
    clock.tick(240)

import pygame
from pygame.locals import *

import button


pygame.init()
window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Tetris")


"""board dimensions"""
board_width = 10
board_height = 20
grid_size = 30

border_thickness = 50

board_matrix = [['X' for _ in range(board_width + 2)] for _ in range(board_height + 2)]


"""draw game board and update board_matrix"""
def draw_board(draw_to=None):
    for i in range(board_height + 2):
        for j in range(board_width + 2):
            if board_matrix[i][j] == draw_to:
                if i > 0 and i < board_height + 1 and \
                    j > 0 and j < board_width + 1:
                    pygame.draw.rect(window, (50, 50, 50), ((window_width - board_width * grid_size) / 2 + (j - 1) * grid_size, (window_height - board_height * grid_size) / 2 + (i - 1) * grid_size, grid_size, grid_size))
                    pygame.draw.rect(window, (30, 30, 30), ((window_width - board_width * grid_size) / 2 + 1 + (j - 1) * grid_size, (window_height - board_height * grid_size) / 2 + 1 + (i - 1) * grid_size, grid_size - 2, grid_size - 2))

                    board_matrix[i][j] = 'B'


"""button init"""
red_button = button.Button(pygame, window, 10,10,50,50, (150,0,0))
green_button = button.Button(pygame, window, 10,70,50,50, (0,150,0))
blue_button = button.Button(pygame, window, 10,130,50,50, (0,0,150))


"""draw everything"""
def draw():
    pygame.draw.rect(window, (50,50,50), ((window_width - board_width * grid_size - border_thickness) / 2, (window_height - board_height * grid_size - border_thickness) / 2, board_width * grid_size + border_thickness, board_height * grid_size + border_thickness))
    red_button.draw()
    green_button.draw()
    blue_button.draw()
    draw_board('X')

draw()
pygame.display.update()


running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    if red_button.pressed():
        print("Red")
    elif green_button.pressed():
        print("green")
    elif blue_button.pressed():
        for i in range(board_height + 2):
            print(board_matrix[i], i)
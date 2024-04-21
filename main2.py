import pygame
from pygame.locals import *

import button
import block2


"""initialize pygame and create the screen object."""
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


"""2D list of cells on the board"""
board_matrix = [[['X','B'] for _ in range(board_width + 2)] for _ in range(board_height + 2)]


"""draw game board and update board_matrix"""
def draw_board():
    for i in range(board_height + 2):
        for j in range(board_width + 2):
            if i > 0 and i < board_height + 1 and \
                j > 0 and j < board_width + 1:
                if board_matrix[i][j][0] != board_matrix[i][j][1]:
                    if board_matrix[i][j][1] == 'B':
                        pygame.draw.rect(window, (50,50,50), ((window_width - board_width * grid_size) / 2 + (j - 1) * grid_size, (window_height - board_height * grid_size) / 2 + (i - 1) * grid_size, grid_size, grid_size))
                        pygame.draw.rect(window, (30,30,30), ((window_width - board_width * grid_size) / 2 + 1 + (j - 1) * grid_size, (window_height - board_height * grid_size) / 2 + 1 + (i - 1) * grid_size, grid_size - 2, grid_size - 2))
                    else:
                        pygame.draw.rect(window, block2.color_codes[board_matrix[i][j][1]], ((window_width - board_width * grid_size) / 2 + (j - 1) * grid_size, (window_height - board_height * grid_size) / 2 + (i - 1) * grid_size, grid_size, grid_size))
                        
                    board_matrix[i][j][0] = board_matrix[i][j][1]


"""button init"""
red_button = button.Button(pygame, window, 10,10,50,50, (150,0,0), "red")
green_button = button.Button(pygame, window, 10,70,50,50, (0,150,0), "green")
blue_button = button.Button(pygame, window, 10,130,50,50, (0,0,150), "blue")


"""draw everything"""
def draw():
    pygame.draw.rect(window, (50,50,50), ((window_width - board_width * grid_size - border_thickness) / 2, (window_height - board_height * grid_size - border_thickness) / 2, board_width * grid_size + border_thickness, board_height * grid_size + border_thickness))
    red_button.draw()
    green_button.draw()
    blue_button.draw()
    draw_board()

draw()
pygame.display.update()


"""setup 100tick system"""
TICK_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(TICK_EVENT, 10)
tick = 0


running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == TICK_EVENT:
            tick = (tick + 1) % 100

            """get called on each 100th tick (1 second)"""
            if tick % 100 == 0:
                try:
                    """remove block from board_matrix"""
                    for i in range(len(first_block.shape)):
                        for j in range(len(first_block.shape[0])):
                            if first_block.shape[i][j] == 1:
                                board_matrix[i + first_block.pos_y][j + first_block.pos_x][1] = 'B'

                    """move block"""
                    first_block.pos_y += 1

                    """add block to board_matrix"""
                    for i in range(len(first_block.shape)):
                        for j in range(len(first_block.shape[0])):
                            if first_block.shape[i][j] == 1:
                                board_matrix[i + first_block.pos_y][j + first_block.pos_x][1] = first_block.block_code
                except Exception as e:
                    print(e)


    if red_button.pressed():
        print("Red")
        # start game

    elif green_button.pressed():
        print("green")

        """init block"""
        first_block = block2.Block('I', 4, 1)

        """add block to board_matrix"""
        for i in range(len(first_block.shape)):
            for j in range(len(first_block.shape[0])):
                if first_block.shape[i][j] == 1:
                    board_matrix[i + first_block.pos_y][j + first_block.pos_x][1] = first_block.block_code

    elif blue_button.pressed():
        print("blue")
        for i in range(board_height + 2):
            print(board_matrix[i], i)


    draw_board()
    pygame.display.update()
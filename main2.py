import pygame
from pygame.locals import *

import button
import block2
import block_codes


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


# """2D list of cells on the board"""
# board_matrix = [[['X','B'] for _ in range(board_width + 2)] for _ in range(board_height + 2)]


# """draw game board and update board_matrix"""
# def draw_board():
#     for i in range(board_height + 2):
#         for j in range(board_width + 2):
#             if i > 0 and i < board_height + 1 and \
#                 j > 0 and j < board_width + 1:
#                 if board_matrix[i][j][0] != board_matrix[i][j][1]:
#                     if board_matrix[i][j][1] == 'B':
#                         pygame.draw.rect(window, (50,50,50), ((window_width - board_width * grid_size) / 2 + (j - 1) * grid_size, (window_height - board_height * grid_size) / 2 + (i - 1) * grid_size, grid_size, grid_size))
#                         pygame.draw.rect(window, (30,30,30), ((window_width - board_width * grid_size) / 2 + 1 + (j - 1) * grid_size, (window_height - board_height * grid_size) / 2 + 1 + (i - 1) * grid_size, grid_size - 2, grid_size - 2))
#                     else:
#                         pygame.draw.rect(window, block_codes.color_codes[board_matrix[i][j][1]], ((window_width - board_width * grid_size) / 2 + (j - 1) * grid_size, (window_height - board_height * grid_size) / 2 + (i - 1) * grid_size, grid_size, grid_size))
                        
#                     board_matrix[i][j][0] = board_matrix[i][j][1]


"""2D list of cells on the board"""
board_matrix = [[['X','B'] for _ in range(board_width)] for _ in range(board_height)]


"""draw game board and update board_matrix"""
def draw_board():
    for i in range(board_height):
        for j in range(board_width):
            if board_matrix[i][j][0] != board_matrix[i][j][1]:
                if board_matrix[i][j][1] == 'B':
                    pygame.draw.rect(window, (50,50,50), ((window_width - board_width * grid_size) / 2 + j * grid_size, (window_height - board_height * grid_size) / 2 + i * grid_size, grid_size, grid_size))
                    pygame.draw.rect(window, (30,30,30), ((window_width - board_width * grid_size) / 2 + 1 + j * grid_size, (window_height - board_height * grid_size) / 2 + 1 + i * grid_size, grid_size - 2, grid_size - 2))
                else:
                    pygame.draw.rect(window, block_codes.color_codes[board_matrix[i][j][1]], ((window_width - board_width * grid_size) / 2 + j * grid_size, (window_height - board_height * grid_size) / 2 + i * grid_size, grid_size, grid_size))
                    
                board_matrix[i][j][0] = board_matrix[i][j][1]


"""button init"""
red_button = button.Button(pygame, window, 10,10,50,50, (150,0,0), "red")
green_button = button.Button(pygame, window, 10,70,50,50, (0,150,0), "green")
blue_button = button.Button(pygame, window, 10,130,50,50, (0,0,150), "blue")

left_button = button.Button(pygame, window, 10,190,50,50, (100,100,100), "<")
right_button = button.Button(pygame, window, 70,190,50,50, (100,100,100), ">")


"""draw everything"""
def draw():
    """border around game board"""
    pygame.draw.rect(window, (50,50,50), ((window_width - board_width * grid_size - border_thickness) / 2, (window_height - board_height * grid_size - border_thickness) / 2, board_width * grid_size + border_thickness, board_height * grid_size + border_thickness))
    
    """buttons"""
    red_button.draw()
    green_button.draw()
    blue_button.draw()

    left_button.draw()
    right_button.draw()
    
    """game board"""
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
                    first_block.move(board_matrix, 'DOWN')
                except Exception as e:
                    print(e)


    # rotate block
    if red_button.pressed():
        print("Red")
        try:
            first_block.rotate(board_matrix)
        except Exception as e:
            print(e)

    # init block
    elif green_button.pressed():
        print("green")

        """init block"""
        first_block = block2.Block('I', 3, 0)

        """add block to board_matrix"""
        first_block.add_to_board_matrix(board_matrix)

    # print board_matrix
    elif blue_button.pressed():
        print("blue")
        for i in range(board_height):
            print(board_matrix[i], i)

    # move block left
    elif left_button.pressed():
        print("left")
        try:
            first_block.move(board_matrix, 'LEFT')
        except Exception as e:
            print(e)
        print(first_block.pos_x)

    # move block right
    elif right_button.pressed():
        print("right")
        try:
            first_block.move(board_matrix, 'RIGHT')
        except Exception as e:
            print(e)
        print(first_block.pos_x)


    draw_board()
    pygame.display.update()
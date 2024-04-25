import pygame
from pygame.locals import *

import button
import block
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
                    pygame.draw.rect(window, block_codes.color[board_matrix[i][j][1]], ((window_width - board_width * grid_size) / 2 + j * grid_size, (window_height - board_height * grid_size) / 2 + i * grid_size, grid_size, grid_size))
                    
                board_matrix[i][j][0] = board_matrix[i][j][1]


"""button init"""
red_button = button.Button(pygame, window, 10,10,50,50, (150,0,0), "red")
green_button = button.Button(pygame, window, 10,70,50,50, (0,150,0), "green")
blue_button = button.Button(pygame, window, 10,130,50,50, (0,0,150), "blue")

rotate_clockwise_button = button.Button(pygame, window, 10,190,50,50, (100,100,100), "<")
rotate_counterclockwise_button = button.Button(pygame, window, 70,190,50,50, (100,100,100), ">")

left_button = button.Button(pygame, window, 10,280,50,50, (100,100,100), "<")
right_button = button.Button(pygame, window, 130,280,50,50, (100,100,100), ">")
up_button = button.Button(pygame, window, 70,250,50,50, (100,100,100), "^")
down_button = button.Button(pygame, window, 70,310,50,50, (100,100,100), "⌄")



"""draw everything"""
def draw():
    """border around game board"""
    pygame.draw.rect(window, (50,50,50), ((window_width - board_width * grid_size - border_thickness) / 2, (window_height - board_height * grid_size - border_thickness) / 2, board_width * grid_size + border_thickness, board_height * grid_size + border_thickness))
    
    """buttons"""
    red_button.draw()
    green_button.draw()
    blue_button.draw()
    
    rotate_clockwise_button.draw()
    rotate_counterclockwise_button.draw()

    left_button.draw()
    right_button.draw()
    up_button.draw()
    down_button.draw()

    
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
                pass
                # try:
                #     first_block.move(board_matrix, 'DOWN')
                # except Exception as e:
                #     print(e)


    if red_button.pressed():
        """init block"""
        first_block = block.Block('O', 4, 0)

        """add block to board_matrix"""
        first_block.add_block_to_board_matrix(board_matrix)

    # init block
    elif green_button.pressed():
        """init block"""
        first_block = block.Block('I', 3, 0)

        """add block to board_matrix"""
        first_block.add_block_to_board_matrix(board_matrix)

    # print board_matrix
    elif blue_button.pressed():
        print("blue")
        for i in range(board_height):
            print(board_matrix[i], i)

    # rotate block CW
    elif rotate_clockwise_button.pressed():
        try:
            first_block.safe_rotate(board_matrix, "CW")
        except Exception as e:
            print(e)

    # rotate block CCW
    elif rotate_counterclockwise_button.pressed():
        try:
            first_block.safe_rotate(board_matrix, "CCW")
        except Exception as e:
            print(e)
            
    # move block left
    elif left_button.pressed():
        try:
            first_block.safe_move(board_matrix, 'LEFT')
        except Exception as e:
            print(e)

    # move block right
    elif right_button.pressed():
        try:
            first_block.safe_move(board_matrix, 'RIGHT')
        except Exception as e:
            print(e)

    # move block up
    elif up_button.pressed():
        try:
            first_block.safe_move(board_matrix, 'UP')
        except Exception as e:
            print(e)

    # move block down
    elif down_button.pressed():
        try:
            first_block.safe_move(board_matrix, 'DOWN')
        except Exception as e:
            print(e)


    draw_board()
    pygame.display.update()
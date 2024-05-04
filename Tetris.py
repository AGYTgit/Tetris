import pygame
from pygame.locals import *

import board
import button
import block

"""init/create variables/objects"""
if True:
    """init pygame and create the window object"""
    pygame.init()
    window_width = 800
    window_height = 600
    window = pygame.display.set_mode((window_width, window_height))
    pygame.display.set_caption("Tetris")

    """setup 100tick system"""
    TICK_EVENT = pygame.USEREVENT + 1
    pygame.time.set_timer(TICK_EVENT, 10)
    tick = 0

    """create boards"""
    main_board = board.Board(window, window_width, window_height)

    side_board = board.Side_Board(window, 600, 0, 120, 450)

    hold_board = board.Side_Board(window, 80, 0, 120, 60)

    """create block_list"""
    block_list = block.Block_List(main_board, 5)

    """create buttons"""
    red_button = button.Button(window, 10,10,50,50, (150,0,0), "red")
    green_button = button.Button(window, 10,70,50,50, (0,150,0), "green")
    blue_button = button.Button(window, 10,130,50,50, (0,0,150), "blue")

    rotate_clockwise_button = button.Button(window, 10,190,50,50, (100,100,100), "<")
    rotate_counterclockwise_button = button.Button(window, 130,190,50,50, (100,100,100), ">")

    drop_button = button.Button(window, 70,190,50,50, (100,100,100), "V")

    left_button = button.Button(window, 10,280,50,50, (100,100,100), "<")
    right_button = button.Button(window, 130,280,50,50, (100,100,100), ">")
    up_button = button.Button(window, 70,250,50,50, (100,100,100), "^")
    down_button = button.Button(window, 70,310,50,50, (100,100,100), "v")

    hold_button = button.Button(window, 10,370,50,50, (100,100,100), "v")

"""draw everything"""
def draw():
    """border around game board"""
    pygame.draw.rect(window, (50,50,50), ((window_width - main_board.board_width * main_board.grid_size - main_board.border_thickness) / 2, (window_height - main_board.board_height * main_board.grid_size - main_board.border_thickness) / 2, main_board.board_width * main_board.grid_size + main_board.border_thickness, main_board.board_height * main_board.grid_size + main_board.border_thickness))
    
    """buttons"""
    red_button.draw()
    green_button.draw()
    blue_button.draw()
    
    rotate_clockwise_button.draw()
    rotate_counterclockwise_button.draw()

    drop_button.draw()

    left_button.draw()
    right_button.draw()
    up_button.draw()
    down_button.draw()

    hold_button.draw()

    """game board"""
    main_board.draw_board()

clock = pygame.time.Clock()

hold_block = None

total_lines_cleared = 0
score = 0
level = 0
speed = 60

draw()
pygame.display.update()

running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == TICK_EVENT:
            # tick = (tick + 1) % 100
            tick += 1

            if tick % speed == 0:
                try:
                    active_block.safe_move(main_board.board_matrix, 'DOWN')
                except Exception as e:
                    print(e)



    if red_button.pressed():
        active_block = block_list.get_next_block()
        active_block.add_block_to_board_matrix(main_board.board_matrix)

    elif green_button.pressed():
        pass

    # print main_board.board_matrix
    elif blue_button.pressed():
        print("blue")
        for i in range(main_board.board_height):
            print(main_board.board_matrix[i], i)

    # rotate block CW
    elif rotate_clockwise_button.pressed():
        try:
            active_block.safe_rotate(main_board.board_matrix, "CW")
        except Exception as e:
            print(e)

    # rotate block CCW
    elif rotate_counterclockwise_button.pressed():
        try:
            active_block.safe_rotate(main_board.board_matrix, "CCW")
        except Exception as e:
            print(e)
            
    # drop block
    elif drop_button.pressed():
        try:
            active_block.drop(main_board.board_matrix)
        except Exception as e:
            print(e)

        active_block = block_list.get_next_block()
        lines_cleared = main_board.clear_completed_lines()
        if lines_cleared != 0:
            if lines_cleared == 1:
                score += 40 * (level + 1)
            elif lines_cleared == 2:
                score += 100 * (level + 1)
            elif lines_cleared == 3:
                score += 300 * (level + 1)
            elif lines_cleared == 4:
                score += 1200 * (level + 1)

            total_lines_cleared += lines_cleared
            if total_lines_cleared - 10 > level * 10:
                level = total_lines_cleared // 10
                speed = round(speed * .8)

            print(total_lines_cleared, level, speed, score)

        """add block to main_board.board_matrix"""
        active_block.add_block_to_board_matrix(main_board.board_matrix)

        try:
            side_board.draw_board('B', 0)
            for i in range(len(block_list.block_list)):
                side_board.draw_board(block_list.block_list[i].block_code, i)
        except Exception as e:
            print(e)

    # move block left
    elif left_button.pressed():
        try:
            active_block.safe_move(main_board.board_matrix, 'LEFT')
        except Exception as e:
            print(e)

    # move block right
    elif right_button.pressed():
        try:
            active_block.safe_move(main_board.board_matrix, 'RIGHT')
        except Exception as e:
            print(e)

    # move block up
    elif up_button.pressed():
        try:
            active_block.safe_move(main_board.board_matrix, 'UP')
        except Exception as e:
            print(e)

    # move block down
    elif down_button.pressed():
        try:
            active_block.safe_move(main_board.board_matrix, 'DOWN')
        except Exception as e:
            print(e)

    # hold block
    elif hold_button.pressed():
        try:
            active_block.remove_block_from_board_matrix(main_board.board_matrix)
            
            if hold_block is None:
                hold_block = block.Block(active_block.block_code, (main_board.board_width - len(active_block.shape[0])) // 2)
                active_block = block_list.get_next_block()
            else:
                placeholder = block.Block(hold_block.block_code, (main_board.board_width - len(hold_block.shape[0])) // 2)
                hold_block = block.Block(active_block.block_code, (main_board.board_width - len(active_block.shape[0])) // 2)
                active_block = placeholder

            hold_board.draw_board('B', 0)
            hold_board.draw_board(hold_block.block_code)

            active_block.add_block_to_board_matrix(main_board.board_matrix)

        except Exception as e:
            print(e)

    main_board.draw_board()
    pygame.display.update()
    clock.tick(60)
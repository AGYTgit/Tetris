import pygame
import block_codes


class Board:
    def __init__(self, window, window_width, window_height, centered=True, board_x_pos=0, board_y_pos=0, board_width=10, board_height=20, grid_size=30, border_thickness=50):
        self.window = window

        self.window_width = window_width
        self.window_height = window_height


        """board dimensions"""
        self.board_width = board_width
        self.board_height = board_height
        self.grid_size = grid_size

        self.border_thickness = border_thickness

        """board position"""
        if not centered:
            self.board_x_pos = board_x_pos
            self.board_y_pos = board_y_pos
        else:
            self.board_x_pos = (self.window_width - self.board_width * self.grid_size) / 2
            self.board_y_pos = (self.window_height - self.board_height * self.grid_size) / 2

        """2D list of cells on the board"""
        self.board_matrix = [[['X','B'] for _ in range(board_width)] for _ in range(board_height)]

    """draw game board and update board_matrix"""
    def draw_board(self, force=False):
        for i in range(self.board_height):
            for j in range(self.board_width):
                if self.board_matrix[i][j][0] != self.board_matrix[i][j][1] or force == True:
                    if self.board_matrix[i][j][1] == 'B':
                        pygame.draw.rect(self.window, (50,50,50), (self.board_x_pos + j * self.grid_size, self.board_y_pos + i * self.grid_size, self.grid_size, self.grid_size))
                        pygame.draw.rect(self.window, (30,30,30), (self.board_x_pos + 1 + j * self.grid_size, self.board_y_pos + 1 + i * self.grid_size, self.grid_size - 2, self.grid_size - 2))
                    elif self.board_matrix[i][j][1] == 'D':
                        pygame.draw.rect(self.window, (150,150,150), (self.board_x_pos + j * self.grid_size, self.board_y_pos + i * self.grid_size, self.grid_size, self.grid_size))
                        pygame.draw.rect(self.window, (30,30,30), (self.board_x_pos + 1 + j * self.grid_size, self.board_y_pos + 1 + i * self.grid_size, self.grid_size - 2, self.grid_size - 2))
                    else:
                        pygame.draw.rect(self.window, block_codes.color[self.board_matrix[i][j][1]], (self.board_x_pos + j * self.grid_size, self.board_y_pos + i * self.grid_size, self.grid_size, self.grid_size))
                        
                    self.board_matrix[i][j][0] = self.board_matrix[i][j][1]

    """clear a line if it is completed"""
    def clear_completed_lines(self):
        for i in range(self.board_height):
            for j in range(self.board_width):
                if self.board_matrix[i][j][1] in ['B', 'D']:
                    break
            else:
                for j in range(self.board_width):
                    self.board_matrix[i][j][1] = 'B'

                self.move_lines(i)


    def move_lines(self, height):
        if height > 0:
            for j in range(self.board_width):
                self.board_matrix[height][j][1] = self.board_matrix[height - 1][j][1]
            for j in range(self.board_width):
                if self.board_matrix[height][j][1] not in ['B', 'D']:
                    self.move_lines(height - 1)
                    break


class Side_Board:
    def __init__(self, window, board_x_pos, board_y_pos, board_width, board_height, grid_size=30, border_thickness=50):
        self.window = window

        """board dimensions"""
        self.board_width = board_width
        self.board_height = board_height
        self.grid_size = grid_size

        self.border_thickness = border_thickness

        """board position"""
        self.board_x_pos = board_x_pos
        self.board_y_pos = board_y_pos


    def draw_board(self, block_code, pos=0):
        if block_code not in block_codes.block_codes:
            pygame.draw.rect(self.window, (50,50,50), (self.board_x_pos, self.board_y_pos, self.board_width, self.board_height))
            return

        shape = block_codes.shape[block_code][0]
        for i in range(len(shape)):
            for j in range(len(shape[i])):
                if shape[i][j] == 0:
                    continue
                pygame.draw.rect(self.window, block_codes.color[block_code], (self.board_x_pos + j * self.grid_size, self.board_y_pos + i * self.grid_size + pos * self.grid_size * 3, self.grid_size, self.grid_size))

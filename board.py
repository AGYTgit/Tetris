import pygame
import block_codes


class Board:
    def __init__(self, window, window_width, window_height, centered=False, board_x_pos=0, board_y_pos=0, board_width=10, board_height=20, grid_size=30, border_thickness=50):
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
                    else:
                        pygame.draw.rect(self.window, block_codes.color[self.board_matrix[i][j][1]], (self.board_x_pos + j * self.grid_size, self.board_y_pos + i * self.grid_size, self.grid_size, self.grid_size))
                        
                    self.board_matrix[i][j][0] = self.board_matrix[i][j][1]

    """clear a line if it is completed"""
    def clear_completed_lines(self):
        """check if a line is completed and remove it if it is"""
        for i in range(self.board_height):
            for j in range(self.board_width):
                    if self.board_matrix[i][j][1] == 'B':
                        break
            else:
                    for j in range(self.board_width):
                        self.board_matrix[i][j][1] = 'B'
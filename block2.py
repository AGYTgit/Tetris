import block_codes

class Block:
      def __init__(self, block_code, pos_x, pos_y, rotation=0):
            """get block code"""
            self.block_code = block_code

            """get x/y position"""
            self.pos_x = pos_x
            self.pos_y = pos_y

            """get rotation"""
            self.rotation = rotation

            """get color and shape"""
            self.color = block_codes.color_codes[block_code]
            self.shape = block_codes.shape_codes[block_code][rotation]


      def rotate(self, board_matrix, direction="CW"):
            self.remove_from_board_matrix(board_matrix)

            """set new rotation"""
            if direction == "CW":
                  self.rotation = (self.rotation - 1 + 4) % 4
            elif direction == "CCW":
                  self.rotation = (self.rotation + 1) % 4

            """get shape with new rotation"""
            self.shape = block_codes.shape_codes[self.block_code][self.rotation]

            self.add_to_board_matrix(board_matrix)
            

      def move(self, board_matrix, direction='DOWN'):
            self.remove_from_board_matrix(board_matrix)

            """move block"""
            if  direction == "LEFT" and self.pos_x > 0 - min(self.count_zeros_until_one(_) for _ in self.shape):
                  self.pos_x -= 1
            elif  direction == "RIGHT" and self.pos_x < len(board_matrix[0]) - len(self.shape[0]):
                  self.pos_x += 1
            elif direction == "DOWN" and self.pos_y < len(board_matrix) - 1:
                  self.pos_y += 1

            self.add_to_board_matrix(board_matrix)
           
      
      def remove_from_board_matrix(self, board_matrix):
            """remove block from board_matrix"""
            for i in range(len(self.shape)):
                  for j in range(len(self.shape[i])):
                        if self.shape[i][j] == 1:
                              board_matrix[i + self.pos_y][j + self.pos_x][1] = 'B'


      def add_to_board_matrix(self, board_matrix):
            """add block to board_matrix"""
            for i in range(len(self.shape)):
                  for j in range(len(self.shape[i])):
                        if self.shape[i][j] == 1:
                              board_matrix[i + self.pos_y][j + self.pos_x][1] = self.block_code


      def count_zeros_until_one(self, lst):
            """count the number of 0s until it gets to 1"""
            count = 0
            for x in lst:
                  if x == 1:
                        break
                  count += 1
            return count
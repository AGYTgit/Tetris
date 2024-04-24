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
            self.color = block_codes.color[block_code]
            self.shape = block_codes.shape[block_code][rotation]
            self.offset = block_codes.offset[block_code][rotation]


      def rotate(self, board_matrix, direction="CW"):
            board_matrix = self.remove_from_board_matrix(board_matrix)

            """set new rotation"""
            if direction == "CW":
                  self.rotation = (self.rotation - 1 + 4) % 4
            elif direction == "CCW":
                  self.rotation = (self.rotation + 1) % 4

            """update shape's rotation"""
            self.shape = block_codes.shape[self.block_code][self.rotation]
            self.offset = block_codes.offset[self.block_code][self.rotation]

            """set new rotation if position is valid"""
            if self.validate_position(board_matrix) == True:
                  self.add_to_board_matrix(board_matrix)
            else:
                  """go back to old rotation"""
                  if direction == "CW":
                        self.rotation = (self.rotation + 1) % 4
                  elif direction == "CCW":
                        self.rotation = (self.rotation - 1 + 4) % 4

                  """update shape's rotation"""
                  self.shape = block_codes.shape[self.block_code][self.rotation]
                  self.offset = block_codes.offset[self.block_code][self.rotation]

                  self.add_to_board_matrix(board_matrix)
            

      def move(self, board_matrix, direction='DOWN'):
            self.remove_from_board_matrix(board_matrix)

            """move block"""
            if  direction == "LEFT" and self.pos_x > 0 - self.offset[0]:
                  self.pos_x -= 1
            elif  direction == "RIGHT" and self.pos_x < len(board_matrix[0]) - len(self.shape[0]) - self.offset[0]:
                  self.pos_x += 1
            elif direction == "DOWN" and self.pos_y < len(board_matrix) - 1 - self.offset[1]:
                  self.pos_y += 1
            elif direction == "UP" and self.pos_y > 0 - self.offset[1]:
                  self.pos_y -= 1

            if self.validate_position(board_matrix):
                  self.add_to_board_matrix(board_matrix)
            else:
                  """move back to old position"""
                  if  direction == "LEFT" and self.pos_x > 0 - self.offset[0]:
                        self.pos_x += 1
                  elif  direction == "RIGHT" and self.pos_x < len(board_matrix[0]) - len(self.shape[0]) - self.offset[0]:
                        self.pos_x -= 1
                  elif direction == "DOWN" and self.pos_y < len(board_matrix) - 1 - self.offset[1]:
                        self.pos_y -= 1
                  elif direction == "UP" and self.pos_y > 0 - self.offset[1]:
                        self.pos_y += 1
           
                  self.add_to_board_matrix(board_matrix)
      
      
      def remove_from_board_matrix(self, board_matrix):
            """remove block from board_matrix"""
            for i in range(len(self.shape)):
                  for j in range(len(self.shape[i])):
                        if self.shape[i][j] == 1:
                              board_matrix[i + self.pos_y + self.offset[1]][j + self.pos_x + self.offset[0]][1] = 'B'
            return board_matrix


      def add_to_board_matrix(self, board_matrix):
            """add block to board_matrix"""
            for i in range(len(self.shape)):
                  for j in range(len(self.shape[i])):
                        if self.shape[i][j] == 1:
                              board_matrix[i + self.pos_y + self.offset[1]][j + self.pos_x + self.offset[0]][1] = self.block_code
            return board_matrix


      def validate_position(self, board_matrix):
            """check if new position is valid"""
            for i in range(len(self.shape)):
                  for j in range(len(self.shape[i])):
                        """filter out where the piece is"""
                        if self.shape[i][j] == 0:
                              continue
                        """chekc if piece is inside the board"""
                        if  0 <= self.pos_y + self.offset[1] + i <= 19 and \
                              0 <= self.pos_x + self.offset[0] + j <= 9:
                              """check for collision"""
                              if board_matrix[self.pos_y + self.offset[1] + i][self.pos_x + self.offset[0] + j][1] == 'B':
                                    continue
                        return False           
            else:
                  return True
      
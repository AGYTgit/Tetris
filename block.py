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
            if self.block_code == 'I':
                  self.wall_kick_offset = block_codes.wall_kick_offset['I']
            else:
                  self.wall_kick_offset = block_codes.wall_kick_offset['other']


      def safe_rotate(self, board_matrix, direction="CW"):
            """remove block from board_matrix and store updated board_matrix"""
            board_matrix = self.remove_block_from_board_matrix(board_matrix)

            """set new rotation"""
            self.rotate(direction)

            """update block's shape, offset and wall-kick offset"""
            self.update_codes(shape=True, offset=True, wall_kick_offset=True)

            """go back to old rotation"""
            self.rotate(direction, reverse=True)

            """loop through wall-kick options"""
            for wall_kick_offset in self.wall_kick_offset[(self.rotation,direction)]:
                  """check if position is valid"""
                  validation, offset = self.validate_position(board_matrix, wall_kick_offset)
                  if validation == True:
                        print(offset)
                        """set new rotation"""
                        self.rotate(direction)

                        """apply offset"""
                        self.pos_y += offset[1]
                        self.pos_x += offset[0]

                        """add block to board_matrix"""
                        print('a')
                        self.add_block_to_board_matrix(board_matrix)
                        print('a')
                        break
            else:
                  """update shape's rotation"""
                  self.shape = block_codes.shape[self.block_code][self.rotation]
                  self.offset = block_codes.offset[self.block_code][self.rotation]

                  """add block to board_matrix"""
                  self.add_block_to_board_matrix(board_matrix)
            

      def safe_move(self, board_matrix, direction='DOWN'):
            """remove block from board_matrix and store updated board_matrix"""
            self.remove_block_from_board_matrix(board_matrix)

            """move block"""
            self.move(board_matrix, direction)

            validation, _ = self.validate_position(board_matrix)
            if validation:
                  """add block to board_matrix"""
                  self.add_block_to_board_matrix(board_matrix)
            else:
                  """move back to old position"""
                  self.move(board_matrix, direction, reverse=True)
           
                  """add block to board_matrix"""
                  self.add_block_to_board_matrix(board_matrix)
      
      
      def remove_block_from_board_matrix(self, board_matrix):
            """remove block from board_matrix"""
            for i in range(len(self.shape)):
                  for j in range(len(self.shape[i])):
                        """filter out empty parts of the block"""
                        if self.shape[i][j] == 0:
                              continue
                        """remove block part"""
                        board_matrix[i + self.pos_y + self.offset[1]][j + self.pos_x + self.offset[0]][1] = 'B'
            return board_matrix


      def add_block_to_board_matrix(self, board_matrix):
            """add block to board_matrix"""
            for i in range(len(self.shape)):
                  for j in range(len(self.shape[i])):
                        """filter out empty parts of the block"""
                        if self.shape[i][j] == 0:
                              continue
                        """add block part"""
                        board_matrix[i + self.pos_y + self.offset[1]][j + self.pos_x + self.offset[0]][1] = self.block_code
            return board_matrix


      def validate_position(self, board_matrix, wall_kick_offset=[0,0]):
            """check if new position is valid"""
            for i in range(len(self.shape)):
                  for j in range(len(self.shape[i])):
                        """filter out empty parts of the block"""
                        if self.shape[i][j] == 0:
                              continue
                        """chekc if piece is inside the board"""
                        if  0 <= self.pos_y + self.offset[1] + i + wall_kick_offset[1] <= len(board_matrix) - 1 and \
                              0 <= self.pos_x + self.offset[0] + j + wall_kick_offset[0] <= len(board_matrix[i]) - 1:
                              """check for collision"""
                              if board_matrix[self.pos_y + self.offset[1] + i + wall_kick_offset[1]][self.pos_x + self.offset[0] + j + wall_kick_offset[0]][1] == 'B':
                                    continue
                        return False, wall_kick_offset
            else:
                  return True, wall_kick_offset
      

      def move(self, board_matrix, direction, reverse=False):
            """move block"""
            if not reverse:
                  if  direction == "LEFT" and self.pos_x > 0 - self.offset[0]:
                        self.pos_x -= 1
                  elif  direction == "RIGHT" and self.pos_x < len(board_matrix[0]) - len(self.shape[0]) - self.offset[0]:
                        self.pos_x += 1
                  elif direction == "UP" and self.pos_y > 0 - self.offset[1]:
                        self.pos_y -= 1
                  elif direction == "DOWN" and self.pos_y < len(board_matrix) - 1 - self.offset[1]:
                        self.pos_y += 1
            else:
                  if  direction == "RIGHT" and self.pos_x > 0 - self.offset[0]:
                        self.pos_x -= 1
                  elif  direction == "LEFT" and self.pos_x < len(board_matrix[0]) - len(self.shape[0]) - self.offset[0]:
                        self.pos_x += 1
                  elif direction == "DOWN" and self.pos_y > 0 - self.offset[1]:
                        self.pos_y -= 1
                  elif direction == "UP" and self.pos_y < len(board_matrix) - 1 - self.offset[1]:
                        self.pos_y += 1


      def rotate(self, direction, reverse=False):
            """set new rotation"""
            if direction == "CW":
                  if not reverse:
                        self.rotation = (self.rotation - 1 + 4) % 4
                  else:
                        self.rotation = (self.rotation + 1) % 4
            elif direction == "CCW":
                  if not reverse:
                        self.rotation = (self.rotation + 1) % 4
                  else:
                        self.rotation = (self.rotation - 1 + 4) % 4
            else:
                  raise ValueError("Invalid direction argument for safe_rotate()")
      

      def update_codes(self, color=False, shape=False, offset=False, wall_kick_offset=False):
            """update block's color, shape, offset and wall-kick offset"""
            if color:
                  self.color = block_codes.color[self.block_code]
            if shape:
                  self.shape = block_codes.shape[self.block_code][self.rotation]
            if offset:
                  self.offset = block_codes.offset[self.block_code][self.rotation]
            if wall_kick_offset:
                  if self.block_code == 'I':
                        self.wall_kick_offset = block_codes.wall_kick_offset['I']
                  else:
                        self.wall_kick_offset = block_codes.wall_kick_offset['other']

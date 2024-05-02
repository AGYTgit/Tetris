import random

import block_codes


class Block:
      def __init__(self, block_code, pos_x, pos_y=0, rotation=0):
            """get block code"""
            self.block_code = block_code

            """get x/y position"""
            self.pos_x = pos_x
            self.pos_y = pos_y

            """get rotation"""
            self.rotation = rotation

            """get color and shape"""
            self.shape = block_codes.shape[block_code][rotation]
            self.offset = block_codes.offset[block_code][rotation]
            if self.block_code == 'I':
                  self.wall_kick_offset = block_codes.wall_kick_offset['I']
            else:
                  self.wall_kick_offset = block_codes.wall_kick_offset['other']

      def safe_rotate(self, board_matrix, direction="CW"):
            """remove block from board_matrix and store updated board_matrix"""
            board_matrix = self.remove_block_from_board_matrix(board_matrix)


            """remove block's telegraph"""
            board_matrix = self.remove_block_from_board_matrix(board_matrix, self.get_telegraph_y_pos(board_matrix))


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
                        """set new rotation"""
                        self.rotate(direction)

                        """apply offset"""
                        self.pos_y += offset[1]
                        self.pos_x += offset[0]


                        """add block's telegraph"""
                        self.add_block_to_board_matrix(board_matrix, 'D', self.get_telegraph_y_pos(board_matrix))


                        """add block to board_matrix"""
                        board_matrix = self.add_block_to_board_matrix(board_matrix)
                        break
            else:
                  """update shape's rotation"""
                  self.shape = block_codes.shape[self.block_code][self.rotation]
                  self.offset = block_codes.offset[self.block_code][self.rotation]


                  """add block's telegraph"""
                  self.add_block_to_board_matrix(board_matrix, 'D', self.get_telegraph_y_pos(board_matrix))


                  """add block to board_matrix"""
                  board_matrix = self.add_block_to_board_matrix(board_matrix)
            
      def safe_move(self, board_matrix, direction='DOWN'):
            """remove block from board_matrix and store updated board_matrix"""
            self.remove_block_from_board_matrix(board_matrix)

            """remove block's telegraph"""
            board_matrix = self.remove_block_from_board_matrix(board_matrix, self.get_telegraph_y_pos(board_matrix))


            """move block"""
            self.move(board_matrix, direction)

            validation, _ = self.validate_position(board_matrix)
            if validation:

                  """add block's telegraph"""
                  self.add_block_to_board_matrix(board_matrix, 'D', self.get_telegraph_y_pos(board_matrix))


                  """add block to board_matrix"""
                  self.add_block_to_board_matrix(board_matrix)
            else:
                  """move back to old position"""
                  self.move(board_matrix, direction, reverse=True)


                  """add block's telegraph"""
                  self.add_block_to_board_matrix(board_matrix, 'D', self.get_telegraph_y_pos(board_matrix))

           
                  """add block to board_matrix"""
                  self.add_block_to_board_matrix(board_matrix)

                  return False
      
      def drop(self, board_matrix):
            # """get telegraph's y position"""
            # telegraph_y_pos = self.get_telegraph_y_pos(board_matrix)

            # """remove block's telegraph"""
            # board_matrix = self.remove_block_from_board_matrix(board_matrix, telegraph_y_pos)
            for _ in range(len(board_matrix)):
                  decision = self.safe_move(board_matrix, 'DOWN')

                  if decision is False:
                        break
            
      def get_telegraph_y_pos(self, board_matrix):
            for i in range(len(board_matrix)):
                  decision, _ = self.validate_position(board_matrix, wall_kick_offset=[0,i])

                  if decision is False:
                        return self.pos_y + (i - 1)
            else:
                  return 0

      def remove_block_from_board_matrix(self, board_matrix, pos_y=None):
            """remove block from board_matrix"""
            for i in range(len(self.shape)):
                  for j in range(len(self.shape[i])):
                        """filter out empty parts of the block"""
                        if self.shape[i][j] == 0:
                              continue
                        """remove block part"""
                        if pos_y is None:
                              board_matrix[i + self.pos_y + self.offset[1]][j + self.pos_x + self.offset[0]][1] = 'B'
                        else:
                              board_matrix[i + pos_y + self.offset[1]][j + self.pos_x + self.offset[0]][1] = 'B'

            return board_matrix

      def add_block_to_board_matrix(self, board_matrix, block_code=None, pos_y=None):
            """add block to board_matrix"""
            for i in range(len(self.shape)):
                  for j in range(len(self.shape[i])):
                        """filter out empty parts of the block"""
                        if self.shape[i][j] == 0:
                              continue
                        """add block part"""
                        if block_code == None:
                              board_matrix[i + self.pos_y + self.offset[1]][j + self.pos_x + self.offset[0]][1] = self.block_code
                        else:
                              board_matrix[i + pos_y + self.offset[1]][j + self.pos_x + self.offset[0]][1] = block_code
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
                              if board_matrix[self.pos_y + self.offset[1] + i + wall_kick_offset[1]][self.pos_x + self.offset[0] + j + wall_kick_offset[0]][1] in ['B', 'D']:
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


class Block_List:
      def __init__(self, main_board, future_blocks):
            self.board = main_board

            """create list of blocks"""
            self.future_blocks = future_blocks
            self.block_code_list = [block_codes.block_codes[random.randint(0, len(block_codes.block_codes) - 1)] for _ in range(future_blocks)]
            self.block_list = [Block(self.block_code_list[i], (self.board.board_width - len(block_codes.shape[self.block_code_list[i]][0][0])) // 2) for i in range(future_blocks)]

      """get next block from the block_list[]"""
      def get_next_block(self):
            """get active block"""
            active_block = self.block_list[0]

            """move blocks to the left of the list"""
            for i in range(self.future_blocks - 1):
                  self.block_list[i] = self.block_list[i + 1]

            """add a new block at the end"""
            random_block_code = block_codes.block_codes[random.randint(0, len(block_codes.block_codes) - 1)]
            self.block_list[self.future_blocks - 1] = Block(random_block_code, (self.board.board_width - len(block_codes.shape[random_block_code][0][0])) // 2)

            return active_block

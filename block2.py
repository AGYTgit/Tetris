"""color definitions for each piece (mainly for use in board_matrix)"""
color_codes = {
    'I': (0,255,255),
    'J': (0,0,255),
    'L': (255,127,0),
    'O': (255,255,0),
    'S': (0,255,0),
    'T': (255,0,255),
    'Z': (255,0,0),
    }


"""shape definitions for each piece (mainly for use in board_matrix)"""
shape_codes = {
    'I': [[1,1,1,1]],

    'J': [[0,1],
          [0,1],
          [1,1]],

    'L': [[1,0],
          [1,0],
          [1,1]],

    'O': [[1,1],
          [1,1]],

    'S': [[0,1,1],
          [1,1,0]],

    'T': [[0,1,0],
          [1,1,1]],

    'Z': [[1,1,0],
          [0,1,1]],
    }


class Block:
    def __init__(self, block_code, pos_x, pos_y):
        """get block code"""
        self.block_code = block_code

        """get color and shape"""
        self.color = color_codes[block_code]
        self.shape = shape_codes[block_code]

        """get x/y position"""
        self.pos_x = pos_x
        self.pos_y = pos_y

class I:
    pos_x = 0
    pos_y = 0
    pos_y_old = 0
    shape = [
        [1,1,1,1]
    ]
    sprite_path = 'pieces/I.png'
    rotation = True

    def __init__(self, pos_x, pos_y):
        self.pos_x = pos_x
        self.pos_y = pos_y

    def increment_y_by(self, value):
        self.pos_y_old = self.pos_y
        self.pos_y += value


class O:
    shape = [
        [1,1],
        [1,1]
    ]
    sprite_path = 'pieces/O.png'
    rotation = False

    def __init__(self, pos_x, pos_y):
        self.pos_x = pos_x
        self.pos_y = pos_y


class Z:
    shape = [
        [1,1,0],
        [0,1,1]
    ]
    sprite_path = 'pieces/Z.png'
    rotation = True

    def __init__(self, pos_x, pos_y):
        self.pos_x = pos_x
        self.pos_y = pos_y

import pygame

blocks = {
    'I': {
        "shape": [
            [1],
            [1],
            [1],
            [1]
            ],
        "sprite": pygame.image.load('pieces/I.png'),
        "rotate": True},
    'O': {
        "shape": [
            [1,1],
            [1,1]
            ],
        "sprite": pygame.image.load('pieces/O.png')},
    'Z': {
        "shape":[
            [1,1,0],
            [0,1,1]
            ],
        "sprite": pygame.image.load('pieces/Z.png'),
        "rotate": True},
}
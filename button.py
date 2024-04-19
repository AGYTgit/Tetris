class Button:
    def __init__(self, pygame, window, x, y, width, height, color):
        self.pygame = pygame
        self.window = window
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

        self.pressed_bool = True

    def draw(self):
        """Draw the button on the screen"""
        self.pygame.draw.rect(self.window, self.color, (self.x, self.y, self.width, self.height))
        self.pygame.display.update()

    def pressed(self):
        """Returns true if mouse is clicked over button"""
        if self.pygame.mouse.get_pressed()[0] and self.pressed_bool:
            self.pressed_bool = False
            pos = self.pygame.mouse.get_pos()
            return self.x <= pos[0] <= self.x + self.width and \
                self.y <= pos[1] <= self.y + self.height
        
        elif not self.pygame.mouse.get_pressed()[0] and not self.pressed_bool:  # reset button state
            self.pressed_bool = True
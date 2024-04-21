class Button:
    def __init__(self, pygame, window, x, y, width, height, color, text, text_color=(0,0,0), font="freesansbold.ttf", font_size=20):
        """get pygame and window"""
        self.pygame = pygame
        self.window = window

        """get position and size"""
        self.x = x
        self.y = y
        self.width = width
        self.height = height

        """get color"""
        self.color = color

        """get text properties"""
        self.font = self.pygame.font.Font(font, font_size)
        self.text = self.font.render(text, False, text_color)
        self.textRect = self.text.get_rect()
        self.textRect.center = ((self.x + self.width / 2), (self.y + self.height / 2))

        """bool for button state"""
        self.pressed_bool = True


    def draw(self):
        """draw button"""
        self.pygame.draw.rect(self.window, self.color, (self.x, self.y, self.width, self.height))
        self.pygame.display.update()

        """draw text"""
        self.window.blit(self.text, self.textRect)


    def pressed(self):
        """return true when LMB is clicked over the button"""
        if self.pygame.mouse.get_pressed()[0] and self.pressed_bool:
            self.pressed_bool = False
            pos = self.pygame.mouse.get_pos()
            return self.x <= pos[0] <= self.x + self.width and \
                self.y <= pos[1] <= self.y + self.height
        
        elif not self.pygame.mouse.get_pressed()[0] and not self.pressed_bool:  # reset button state
            self.pressed_bool = True
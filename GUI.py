import pygame

class Button:
    def __init__(self, window, x, y, width, height, color, text, text_color=(0,0,0), font="freesansbold.ttf", font_size=20):
        """get pygame and window"""
        self.window = window

        """get position and size"""
        self.x = x
        self.y = y
        self.width = width
        self.height = height

        """get color"""
        self.color = color

        """get text properties"""
        self.font = pygame.font.Font(font, font_size)
        self.text = self.font.render(text, False, text_color)
        self.textRect = self.text.get_rect()
        self.textRect.center = ((self.x + self.width / 2), (self.y + self.height / 2))

        """bool for button state"""
        self.pressed_bool = True

        self.external_interrupt = False

    def draw(self):
        """draw button"""
        pygame.draw.rect(self.window, self.color, (self.x, self.y, self.width, self.height))

        """draw text"""
        self.window.blit(self.text, self.textRect)

    def pressed(self):
        if self.external_interrupt:
            self.external_interrupt = False
            return True
        
        """return true when LMB is clicked over the button"""
        if pygame.mouse.get_pressed()[0] and self.pressed_bool:
            self.pressed_bool = False
            pos = pygame.mouse.get_pos()
            
            return self.x <= pos[0] <= self.x + self.width and \
                self.y <= pos[1] <= self.y + self.height
        
        elif not pygame.mouse.get_pressed()[0] and not self.pressed_bool:  # reset button state
            self.pressed_bool = True
    
    def press(self):
        """press button"""
        self.external_interrupt = True

class Text_Field:
    def __init__(self, window, x, y, width, height, color=None, text="", text_color=(0,0,0), font="freesansbold.ttf", font_size=20):
        self.window = window

        self.x = x
        self.y = y
        self.width = width
        self.height = height

        self.color = color

        self.text = text
        self.text_color = text_color

        self.font = font
        self.font_size = font_size

        self.formated_font = pygame.font.Font(self.font, self.font_size)
        self.formated_text = self.formated_font.render(self.text, False, self.text_color)
        self.textRect = self.formated_text.get_rect()
        self.textRect.center = ((self.x + self.width / 2), (self.y + self.height / 2))

        self.set_text(self.text)

    def draw(self, replace=True):
        """remove old text"""
        if replace:
            self.window.blit(self.old_formated_text, self.old_textRect)

        """draw button"""
        if self.color is not None:
            pygame.draw.rect(self.window, self.color, (self.x, self.y, self.width, self.height))

        """draw text"""
        self.window.blit(self.formated_text, self.textRect)

        self.old_text = self.text

    def set_text(self, new_text, replace_color=(0,0,0)):
        self.old_formated_font = pygame.font.Font(self.font, self.font_size)
        self.old_formated_text = self.formated_font.render(self.text, False, replace_color)
        self.old_textRect = self.formated_text.get_rect()
        self.old_textRect.center = ((self.x + self.width / 2), (self.y + self.height / 2))

        self.formated_font = pygame.font.Font(self.font, self.font_size)
        self.formated_text = self.formated_font.render(new_text, False, self.text_color)
        self.textRect = self.formated_text.get_rect()
        self.textRect.center = ((self.x + self.width / 2), (self.y + self.height / 2))

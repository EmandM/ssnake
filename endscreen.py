import pygame, variables
from variables import Colour
from variables import Text

def center_x(width):
    return variables.GAME_WIDTH//2 - width//2
def center_y(height):
    return variables.GAME_HEIGHT//2 - height//2


class GameOver:
    text_colour = Colour.WHITE
    anti = True

    main_text = 'GAME OVER'
    cont_text = 'Press SPACE to retry'
    end_text = 'Press X to quit'
    gap = Text.GAP

    def __init__(self):
        self.m_font = pygame.font.Font(Text.FONT, Text.SIZE_LARGE)
        self.c_font = pygame.font.Font(Text.FONT, Text.SIZE_MEDIUM)
        self.x_font = pygame.font.Font(Text.FONT, Text.SIZE_SMALL)

        # Set up location data
        main_width, main_height = (self.m_font.size(self.main_text))
        c_width, c_height = (self.c_font.size(self.cont_text))
        x_width, x_height = (self.x_font.size(self.end_text))
        total_height = main_height+c_height+x_height+ self.gap*2

        self.m_location = [center_x(main_width), center_y(total_height)]
        self.c_location = [center_x(c_width), self.m_location[1] + main_height + self.gap*2]
        self.x_location = [center_x(x_width), self.c_location[1] + c_height + self.gap]

    def draw(self, surface):
        main_message = self.m_font.render(self.main_text, self.anti, self.text_colour)
        cont_message = self.c_font.render(self.cont_text, self.anti, self.text_colour)
        end_message = self.x_font.render(self.end_text, self.anti, self.text_colour)

        surface.blit(end_message, self.x_location)
        surface.blit(cont_message, self.c_location)
        surface.blit(main_message, self.m_location)

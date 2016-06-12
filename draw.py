import pygame, variables
from variables import Colour

class Draw:
    def draw_canvas(self, surface):
        game = surface.fill(Colour.BLACK)
        # pygame.draw.rect(surface, Colour.BLACK, game.inflate(-B_WIDTH//2, -B_WIDTH//2), B_WIDTH)

    def get_overlay(self):
        game_overlay = pygame.Surface([variables.GAME_WIDTH, variables.GAME_HEIGHT])
        game_overlay.set_alpha(variables.OPACITY)
        return game_overlay

    def draw_queue(self, surface, draw_queue, flip = True):
        for piece in draw_queue:
            piece.draw(surface)

        if flip:
            pygame.display.flip()

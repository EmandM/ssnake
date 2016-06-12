import sys, pygame, variables
from variables import Movement

# Keyboard shit
class Keyboard:
    def continue_game(self, key):
        return key == pygame.K_RETURN or key == pygame.K_SPACE

    def is_exit(self, key):
        return key == pygame.K_x or key == pygame.K_ESCAPE

    def get_key_press(self, game_event):
        for event in game_event:
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and self.is_exit(event.key)):
                pygame.quit ()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                return event.key

    def get_direction(self, key, currentDir, allowOpposite):
        if (key == pygame.K_UP or key == pygame.K_w) and (allowOpposite or currentDir != Movement.DOWN):
            return Movement.UP
        elif (key == pygame.K_DOWN or key == pygame.K_s) and (allowOpposite or currentDir != Movement.UP):
            return Movement.DOWN
        elif (key == pygame.K_LEFT or key == pygame.K_a) and (allowOpposite or currentDir != Movement.RIGHT):
            return Movement.LEFT
        elif (key == pygame.K_RIGHT or key == pygame.K_d) and (allowOpposite or currentDir != Movement.LEFT):
            return Movement.RIGHT
        return currentDir

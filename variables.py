scale = 2;
base_square = 8

UNIT = base_square*scale
GAME_WIDTH = 31 *UNIT
GAME_HEIGHT = 25 *UNIT
FOOD_DIFF = 2 *scale
INITIAL_SNAKE_LENGTH = 5

# Disabled because of fuckery
BORDER_WIDTH = scale

OPACITY = 100

CLOCK_SPEED = 2

class Movement:
    UP = [0, -UNIT]
    DOWN = [0, UNIT]
    LEFT = [-UNIT, 0]
    RIGHT = [UNIT, 0]

class Colour:
    BLACK = 0, 0, 0
    WHITE = 255, 255, 255
    BLUE = 173, 216, 230
    GREY = 200, 200, 200

class Text:
    SIZE_LARGE = 40*scale
    SIZE_MEDIUM = 20*scale
    SIZE_SMALL = 10*scale
    GAP = 5*scale
    FONT = './resources/Cabin-Bold-TTF.ttf'

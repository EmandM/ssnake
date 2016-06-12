import pygame, variables
from game.location import Location
colour = variables.Colour()
UNIT = variables.UNIT
FOOD_DIFF = variables.FOOD_DIFF

# to initialise rect: location, size
# to draw rect: surface to draw on, colour, rect, width?

class Piece(object):
    location = Location()
    size = 0
    colour = 0
    edge = 0

    def get_location(self):
        return self.location
    def get_size(self):
        return self.size
    def get_colour(self):
        return self.colour
    def get_width(self):
        return self.edge

    def get_rect(self):
        # Adjust the drawing location so rect is drawn in the center of a square unit
        newLoc = Location().create(self.location).transform((UNIT - self.size) // 2)
        return pygame.Rect(newLoc.get_location(), [self.size, self.size])

    def update_location(self, loc):
        self.location = loc

    def draw(self, surface):
        return pygame.draw.rect(surface, self.colour, self.get_rect(), self.edge)

    def __init__(self, loc):
        self.location = loc

class SnakeHead(Piece):
    size = UNIT
    colour = colour.WHITE
    edge = size//2-1

class SnakeBody(Piece):
    size = UNIT
    colour = colour.WHITE

class Food(Piece):
    size = UNIT - FOOD_DIFF
    colour = colour.BLUE


class PieceFactory():
    def create(self, typ, loc=Location()):
        if typ == "snake_head": return SnakeHead(loc)
        if typ == "snake_body": return SnakeBody(loc)
        if typ == "food": return Food(loc)
        assert 0, "Bad shape creation: " + typ

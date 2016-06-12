import pygame, variables, random
from game.location import Location
from game.piece import PieceFactory

UNIT = variables.UNIT
MIN_LEN = variables.INITIAL_SNAKE_LENGTH
G_WIDTH, G_HEIGHT = variables.GAME_WIDTH, variables.GAME_HEIGHT
piece_factory = PieceFactory()
snake_locations = []
food = None

# Generate locations using unit to simulate a grid
def generate_food():
    return Location(random.randint(0,G_WIDTH//UNIT-1)*UNIT, random.randint(0,G_HEIGHT//UNIT-1)*UNIT)
def generate_snake():
    return Location(((G_WIDTH//UNIT)//2)*UNIT,((G_HEIGHT//UNIT)//2)*UNIT)

# Helper functions
def has_collision(piece, snake):
    return piece in snake

def move_food(snake):
    new = generate_food()
    while has_collision(new, snake):
        new = generate_food()
    return new

def move_head(old_head, direc):
    head = Location(old_head.get_x() + direc[0], old_head.get_y() + direc[1])

    if head.get_x() < 0:
        head.set_x(G_WIDTH - UNIT)
    elif head.get_x() >= G_WIDTH:
        head.set_x(0)
    elif head.get_y() < 0:
        head.set_y(G_HEIGHT - UNIT)
    elif head.get_y() >= G_HEIGHT:
        head.set_y(0)

    return head

# Code for running the ssnake game
def initialise():
    global snake_locations, food
    snake_locations = [generate_snake()]
    food = piece_factory.create('food', move_food(snake_locations))
    return GameResult()

def run_frame(surface, direction):
    draw_queue = []
    snake_locations.insert(0, move_head(snake_locations[0], direction))
    if snake_locations[0] == food.get_location():
        # Create new food piece to have a blue piece show under the head
        draw_queue.append(piece_factory.create('food', food.get_location()))
        food.update_location(move_food(snake_locations))
    elif len(snake_locations) > MIN_LEN:
        snake_locations.pop(len(snake_locations) - 1)

    # Draw everything
    draw_queue.append(food)
    draw_queue.append(piece_factory.create('snake_head', snake_locations[0]))
    for piece in snake_locations[1:len(snake_locations)]:
        draw_queue.append(piece_factory.create('snake_body', piece))

    return GameResult(not has_collision(snake_locations[0], snake_locations[1:]), len(snake_locations), draw_queue)

class GameResult:
    def __init__(self, success=True, snake_length=0, draw_queue=[]):
        self.success = success
        self.snake_len = snake_length
        self.draw_queue = draw_queue

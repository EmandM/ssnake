import pygame, variables, math, game.main as Game
from draw import Draw
from endscreen import GameOver
from keyboard import Keyboard

# Initialise shit
CLOCK_SPEED = variables.CLOCK_SPEED
clock = pygame.time.Clock()
global clock_speed
key_handler = Keyboard()
draw = Draw()

# Game states
def start_game():
    global state, result
    state = 'game'
    result = Game.initialise()
    return variables.Movement.RIGHT

def end_game():
    global state, clock_speed
    clock_speed = CLOCK_SPEED
    state = 'over'
    return 0

pygame.init()

pygame.display.set_caption('ssnake')
screen = pygame.display.set_mode([variables.GAME_WIDTH, variables.GAME_HEIGHT])

direction = start_game()

while 1:
    key_press = key_handler.get_key_press(pygame.event.get())
    if state == 'game':
        direction = key_handler.get_direction(key_press, direction, result.snake_len < 3)
        result = Game.run_frame(screen, direction)
        if not result.success:
            increment = end_game()
            continue
        draw.draw_canvas(screen)
        draw.draw_queue(screen, result.draw_queue)
        clock_speed = CLOCK_SPEED + int(2*math.log(result.snake_len))

    if state == 'over':
        if key_handler.continue_game(key_press):
            direction = start_game()
            continue
        game_over = [GameOver()]
        draw.draw_canvas(screen)
        if increment%2 != 0:
            game_overlay = draw.get_overlay()
            draw.draw_queue(game_overlay, result.draw_queue, False)
            screen.blit(game_overlay, [0,0])
        draw.draw_queue(screen, game_over)
        increment += 1

    clock.tick(clock_speed)

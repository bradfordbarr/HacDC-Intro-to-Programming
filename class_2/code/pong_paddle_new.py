#!/usr/bin/python
# there are some magic numbers around, but that's the point
# right?

"""
A simple ball that hits a pong paddle
"""

import pygame
from pygame.locals import *

# some globals
SCREEN_WIDTH  = 640
SCREEN_HEIGHT = 480
FRAMERATE = 60
# initialize pygame
pygame.init()
# make a clock so things don't move ungodly fast
clock = pygame.time.Clock()
# create a display surface
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pong paddle!")


# background stuff
background = pygame.Surface(screen.get_size())
background.fill((0, 0, 0))

def draw_paddle(paddle):
    # draw paddle
    pygame.draw.rect(screen, (0, 100, 200), paddle)

def draw_ball(ball):
    # draw ball
    pygame.draw.circle(screen, (0, 255, 0), ball, 10)

def update_ball(ball, dx):
    # update the position of the ball
    updated_x = ball[0] + dx
    return (updated_x, ball[1])

def check_ball_collision(ball, paddle, dx):
    # check for collisions
    # if the ball reaches the ends of the screen or hits the paddle, bounce back
    if (ball[0] >= SCREEN_WIDTH) or (ball[0] <= 0) or (ball[0]-10 <= paddle[0] + 20):
        return dx * -1
    else:
        return dx

# infinite loop
def game_loop():
    # define paddle variables -- a tuple (x, y, width, height)
    paddle = (20, (SCREEN_HEIGHT /2) -50, 20, 100)

    # define ball variables -- a tuple (x, y)
    ball = (SCREEN_WIDTH / 2, (SCREEN_HEIGHT / 2))
    ball_dx = 1
    while True:
        clock.tick(FRAMERATE)
        # clear the screen
        screen.blit(background, (0, 0))
        draw_paddle(paddle)
        draw_ball(ball)
        # this function gives us a new ball tuple, so we need to assign it to
        # the ball again
        ball = update_ball(ball, ball_dx)
        # check collisions
        ball_dx = check_ball_collision(ball, paddle, ball_dx)
        # flip display
        pygame.display.flip()

if __name__ == '__main__':
    game_loop()

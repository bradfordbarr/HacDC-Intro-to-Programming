#!/usr/bin/python
# there are some magic numbers around, but that's the point
# right?
#

"""
A simple ball that hits a pong paddle
"""

import pygame
from pygame.locals import *

# some globals
SCREEN_WIDTH  = 640
SCREEN_HEIGHT = 480 
# initialize pygame
pygame.init()
# create a display surface
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pong paddle!")
# define paddle variables
paddle_x = 20
paddle_y = SCREEN_HEIGHT / 2

# define ball variables
ball_x = SCREEN_WIDTH / 2
ball_y = SCREEN_HEIGHT / 2
ball_dx = 5

# background stuff
background = pygame.Surface(screen.get_size())
background.fill((0, 0, 0))

# infinite loop
while True:
    # clear the screen
    screen.blit(background, (0, 0))
    # draw paddle
    pygame.draw.rect(screen, (0, 100, 200), (paddle_x, paddle_y-50, 20, 100))
    # draw ball
    pygame.draw.circle(screen, (0, 255, 0), (ball_x, ball_y-5), 10)
    # update ball's position
    ball_x += ball_dx
    # if the ball reaches the ends of the screen, bounce back
    if (ball_x >= SCREEN_WIDTH) or (ball_x <= 0):
        ball_dx *= -1
    # if the ball hits the paddle, bounce back
    if ball_x-5 <= paddle_x + 10:
        ball_dx *=-1
    # flip display
    pygame.display.flip()


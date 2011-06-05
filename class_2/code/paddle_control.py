#!/usr/bin/python
# there are some magic numbers around, but that's the point
# right?


# Think about the following while reading this code:
# - both the paddle and the ball are represented as tuples, this forces
#   some interesting choices in the update functions. Can you spot them?
#
# - if we were to represent the paddle and the ball as lists, what would we
#   need to change in the update_ball and update_paddle functions. What other
#   things do we need to take into account in making the change
#
# - the way this code is checking for collisions with the paddle and the wall
#   is not optimal and causes some strange behavior, can you spot it?
#
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

def update_paddle(paddle, direction):
    if direction == 'UP':
        # move up by 10
        return paddle[0], paddle[1]-10, paddle[2], paddle[3]
    elif direction == 'DOWN':
        # move down by 10
        return paddle[0], paddle[1]+10, paddle[2], paddle[3]

def update_ball(ball, dx):
    # update the position of the ball
    updated_x = ball[0] + dx
    return (updated_x, ball[1])

def check_ball_collision(ball, paddle, dx):
    # check for collisions
    # if the ball reaches the ends of the screen or hits the paddle, bounce back
    if (ball[0] >= SCREEN_WIDTH) or (ball[0] <= 0):
        return dx * -1
    elif (ball[0]-10 <= paddle[0] + 20) and (ball[1] > paddle[1]) and (ball[1] < paddle[1] + paddle[3]):
        return dx * -1
    else:
        return dx

# infinite loop
def game_loop():
    # define paddle variables -- a tuple (x, y, width, height)
    paddle = (20, (SCREEN_HEIGHT /2) -50, 20, 100)

    # define ball variables -- a tuple (x, y)
    ball = (SCREEN_WIDTH / 2, (SCREEN_HEIGHT / 2))
    ball_dx = 10
    while True:
        # get events
        for event in pygame.event.get():
            print event.type
            if event.type == pygame.QUIT:
                return
            # move paddle up if we press the up arrow
            if event.type == KEYDOWN and event.dict['key']== 273:
                paddle = update_paddle(paddle, 'UP')
            # move paddle down if we press the down arrow
            if event.type == KEYDOWN and event.dict['key'] == 274:
                paddle = update_paddle(paddle, 'DOWN')

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

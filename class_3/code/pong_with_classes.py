#!/usr/bin/python
#
# 1st version of pong with classes
#
#

import pygame, sys, random
from pygame.locals import *

# we will still keep some globals around for things like the
# game world constants

SCREEN_WIDTH  = 640
SCREEN_HEIGHT = 480
FRAMERATE     =  60

# initialize pygame
pygame.init()
# make a global clock
CLOCK = pygame.time.Clock()
# our display surface will also be global for now
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("A game of pong!")

# let's create a paddle class
class Paddle(object):
    """
    Represents a player paddle for a game of pong.
    It keeps track of the paddle's position, velocity, and color.
    It handles control of the paddle and collision detection as well.
    """
    def __init__(self, x, y, color=(255, 0, 0)):
        self.x = x
        self.y = y
        self.w = 10 # width
        self.h = 100# height
        self.color = color
        self.dy = 10 # motion speed
        self.paddle_up = self.paddle_down = False # paddle is not moving
        self.draw()

    def set_paddle_up(self):
        """
        Set the paddle to move up
        """
        self.paddle_up = True

    def set_paddle_down(self):
        """
        Set the paddle to move down
        """
        self.paddle_down = True

    def stop_paddle(self):
        """
        Stops the paddle from moving
        """
        self.paddle_up = self.paddle_down = False

    def update(self):
        """
        This is the method that actually moves the paddle
        """
        if self.y > 0 and self.paddle_up:
            self.y -= self.dy

        if (self.y + 100) < SCREEN_HEIGHT and self.paddle_down:
            self.y += self.dy

    def draw(self):
        """
        Draws the paddle
        """
        self.bounding_box = pygame.draw.rect(SCREEN, self.color, (self.x, self.y, self.w, self.h))

class Ball(object):
    """
    A very simple ball to represent the ball
    """
    # there's a lot of room for improvement here, left as an
    # exercise to the reader
    def __init__(self):
        self.radius = 10
        self.color  = (0, 0, 255)
        self.reset()
        self.draw()

    def reset(self):
        """
        Resets the ball to it's start position in the middle of the screen
        and gives it an initial velocity in x and y
        """
        # so that is truly centered
        self.x = (SCREEN_WIDTH / 2) - self.radius
        self.y = (SCREEN_HEIGHT / 2) - self.radius
        self.dx = random.randint(-3, 3)
        self.dy = random.randint(-6, 6)

    def update(self):
        """
        Updates the position of the ball
        """
        self.x += self.dx
        self.y += self.dy
        if self.y < 0 or (self.y+self.radius) > SCREEN_HEIGHT:
            self.dy = -self.dy
        # we would like to check this for the scoring in the future
        if self.x < 0 or (self.x+self.radius) > SCREEN_WIDTH:
            self.reset()

    def check_collisions(self, paddle):
        """
        Check collision against a paddle
        """
        # what else can we do here???
        if self.bounding_box.colliderect(paddle.bounding_box):
            self.dx = -self.dx

    def draw(self):
        """
        Draws the ball onto the screen
        """
        self.bounding_box = pygame.draw.circle(SCREEN, self.color, (self.x, self.y), self.radius)

def game_loop():
    # create the players
    player1 = Paddle(40, SCREEN_HEIGHT/2 - 50)
    player2 = Paddle(SCREEN_WIDTH-50, SCREEN_HEIGHT/2-50, (0, 255, 0))
    # create the ball
    ball = Ball()
    # background
    background = pygame.Surface(SCREEN.get_size())
    background.fill((0, 0, 0))
    while True:
        # get events
        # can we thing of a better way to manage this events?
        # an event manager object??? 
        for event in pygame.event.get():
            # print(event)
            if event.type == QUIT:
                sys.exit(0)
            if event.type == KEYDOWN:
                if event.key == K_w:
                    player1.set_paddle_up()
                if event.key == K_s:
                    player1.set_paddle_down()
                if event.key == K_UP:
                    player2.set_paddle_up()
                if event.key == K_DOWN:
                    player2.set_paddle_down()
            if event.type == KEYUP:
                if event.key == K_w or event.key == K_s:
                    player1.stop_paddle()
                if event.key == K_UP or event.key == K_DOWN:
                    player2.stop_paddle()
        # clear the SCREEN
        SCREEN.blit(background, (0, 0))
        # update things
        player1.update()
        player2.update()
        # check for ball collisions
        ball.check_collisions(player1)
        ball.check_collisions(player2)
        ball.update()
        # draw things
        player1.draw()
        player2.draw()
        ball.draw()
        # tick the clock
        CLOCK.tick(FRAMERATE)
        # flip the display
        pygame.display.flip()

if __name__ == '__main__':
    game_loop()

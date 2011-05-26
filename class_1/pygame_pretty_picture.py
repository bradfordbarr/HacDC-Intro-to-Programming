#! /usr/bin/env python

# imports needed to use pygame.
import pygame
from pygame.locals import *

# the resolution of our picture.
RESOLUTION = (200, 200)

# initialize the pygame library
pygame.init()

# make the screen
screen = pygame.display.set_mode(RESOLUTION)

# set the caption
pygame.display.set_caption("My pretty picture!")

# draw the box for the house.
# box_x and box_y are the upper left hand corner of the box
box_x = (RESOLUTION[0] / 2) - 25 
box_y = RESOLUTION[1] - 50
pygame.draw.rect(screen, (255, 0, 255), (box_x, box_y, 50, 50))

# draw the roof.
pygame.draw.polygon(screen, (255, 255, 255), [(box_x, box_y), (box_x+25, box_y - 25), (box_x+50, box_y)])

# render things to the screen (I forgot to do this when I wrote this code).
pygame.display.flip()

# keep everything on screen until a quit.
while True:
	pass


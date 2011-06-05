#!/usr/bin/python
#
# This programs opens a window with a black background and listens to all events,
# move your mouse over the window and press keys to see what the events look like.
#
# look at the output on your shell, do you recognize some constructs from the class?
#
# take a look at the code for the paddle_control.py example to see how to access
# particular event values
#

# import all the pygame required stuff
import sys, pygame
pygame.init()
size = width, height = 500,600
# make the color black as a tuple
black = 0, 0, 0

# create a screen
screen = pygame.display.set_mode(size)
pygame.display.set_caption('events')

# our loop
while 1:
    # get events and loop through them
    for event in pygame.event.get():
        # print the contents of the event
        print(event)
        # if the event is QUIT, exit the program
        if event.type == pygame.QUIT:
            sys.exit(0)

    # continue updating a black background
    screen.fill(black)
    pygame.display.flip()

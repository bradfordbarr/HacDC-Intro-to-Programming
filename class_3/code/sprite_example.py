#! /usr/bin/env python
""" 
Simple class for animating sprites!

Two helper functions are in this file, they'll help you use
images in pygame. load_image opens and loads an image file.
split_image splits up a character sheet into a list of lists
containing images of the individual sprites.

One class is defined in this file. It's a class that animates
a sprite. No motion control is attached to it. It is a subclass
of the sprite class. We didn't cover this in class, but a link
will be provided below.

The try, catch, raise stuff is exception handling!
http://docs.python.org/tutorial/errors.html

The object and class documentation can be found here.
http://docs.python.org/tutorial/classes.html
"""

import pygame
from pygame.locals import *

RESOLUTION = (640, 480)
FRAMERATE = 60

def load_image(name, colorkey=None):
	""" Loads an image from file.
	When the image is loaded it's converted to pix mappings
	for quick blits, and it's colorkey is set.
	
	The colorkey makes whatever color is specified transparent.
	"""

	# Try to load the image, crash if it doesn't work
	try:
		image = pygame.image.load(name)
	except pygame.error, message:
		print('Cannot load image:', name)
		raise SystemExit, message

	# convert the image to a representation that's quick
	# and easy to blit to the screen
	image = image.convert()

	# if there's a color key, use it to set the transparency
	if colorkey is None or colorkey != -1:
		colorkey = image.get_at((0,0))
		image.set_colorkey(colorkey, RLEACCEL)
	else:
		image.set_colorkey(colorkey, RLEACCEL)

	# return the image surface
	return image

def split_image(surface, point, cols, rows, width, height):
	""" Splits up a sprite sheet and returns a list of subsurfaces."""

	# this is where the list of images will be contained
	subsurfaces = []

	# we're setting posx and orix to the first item in the point tuple
	# and setting poxy and oriy to the second item in the point tuple
        posx, posy = orix, oriy = point

	# for each row in the sprite sheet 
	#	for each column in the sprite sheet
	#		grab the image at that location and append 
	#		it to the row of sprites
	#	add the row to the subsurfaces list 
	#	reset the x position on the image
	#	add the height of the sprite to the y position
        for i in range(rows):
		row = []
                for j in range(cols):
			# subsurfaces are just subsections of the surface provided
			row.append(surface.subsurface((posx, posy, width, height)))
                        posx += width
                subsurfaces.append(row)
                posx = orix
                posy += height

	# return the list of lists containing subsurfaces of the main sprite sheet
        return subsurfaces

class AnimatedSprite(pygame.sprite.Sprite):
	def __init__(self, images, max_ticks, pos, *groups):
		""" Sets up the sprite for animation. Stores some variables."""
		# initialize the super class
		super(AnimatedSprite, self).__init__(*groups)

		# store variables needed for the object
		self.images = images # the images we'll loop through in the animation
		self.max_ticks = max_ticks # amount of clock ticks until animation change
		self.ticks = 0 # amount of clock ticks that have passed since last reset
		self.counter = 0 # the image we're currently on
		
		# make the sprites initial display work
		self.rect = pos
		self.image = self.images[0]
	
	def update(self):
		""" Updates the image for the animation every max_ticks calls."""
		# update the ticks
		self.ticks += 1
		
		# if the number of ticks since last ticks reset is equal to max_ticks
		# reset the tick counter
		# update the image counter
		# udate the sprite image based on the new image counter
		if self.ticks == self.max_ticks:
			self.ticks = 0
			self.counter += 1
			self.image = self.images[self.counter % len(self.images)]

def main():
	# initialize pygame
	pygame.init()

	# initialize the screen
	screen = pygame.display.set_mode(RESOLUTION)

	# load image and split it up (for animation)
	charsheet = load_image('chars.png')
	charsplit = split_image(charsheet, (0, 0), 3, 4, 32, 48)

	# make a clock so we don't use 100% of the cpu power
	clock = pygame.time.Clock()

	# make a sprite and a sprite group
	# sprites can't display without being in a group
	sprite = AnimatedSprite(charsplit[0], 20, (100, 100, 0, 0))
	sprite_group = pygame.sprite.GroupSingle(sprite)

	while True:
		# update the clock
		clock.tick(FRAMERATE)

		# update the sprites image
		sprite_group.update()

		# draw the sprite to screen
		sprite_group.draw(screen)

		# make the screen update
		pygame.display.flip()

		# quit if you hit the 'x' button or the 'q' key
		for e in pygame.event.get():
			if e.type == QUIT:
				return
			elif e.type == KEYDOWN and e.key == K_q:
				return

# in the wild, this is how people call scripts from the command line
# it basically checks to see if this script was called or
# imported with that import statement
if __name__ == "__main__":
	main()

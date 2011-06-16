#! /usr/bin/env python

import serial
import pygame
from pygame.locals import *

DEV = '/dev/ttyACM0'
BAUD = 9600
SIZE = (500,600)

def main():
	pygame.init()

	ser = serial.Serial(DEV, BAUD) # this assumes you have an FTDI cable or some other USB to serial connection.

	screen = pygame.display.set_mode(SIZE)
	pygame.display.set_caption('serial')

	while True:
		events = pygame.event.get()
		for event in events:
			if event.type == KEYDOWN:
				if event.key == K_SPACE:
					print "on"
					ser.write('a') # writes the byte 'a' to the serial device
				elif event.key == K_q:
					return
			elif event.type == KEYUP:
				if event.key == K_SPACE:
					print "off"
					ser.write('b') # writes the byte 'b' to the serial device

	ser.close() # free the device when you're done with it

if __name__ == "__main__":
	main()

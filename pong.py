#! /usr/bin/env python

import sys, serial, math, random
import pygame as pg
from pygame.locals import *

class Ball(object):
	def __init__(self, screen, size=3, heading=0, position=(0,0)):
		self.screen = screen
		self.size = size
		self.heading = heading
		self.position = position
		self.bounding_box = pg.draw.circle(self.screen, (255,255,255), self.position, self.size)
		self.velocity = [math.radians(random.randrange(-90,90)),5]
		self.hit = False
		self.counter = 0

	def update(self):
		point = 0
		deltas = self.get_position_change()
		self.position = (int(self.position[0]+deltas[0]), int(self.position[1]+deltas[1]))
		if self.position[0] > self.screen.get_width():
			point = 1
			angle = math.radians(random.randrange(90,270))
			angle = angle if angle != 180 else mrandom.randrange(90,270)
			self.velocity = [angle,5]
			self.position = (self.screen.get_width()/2, self.screen.get_height()/2)
		elif self.position[0] < 0:
			point = 2
			angle = math.radians(random.randrange(-90,90))
			angle = angle if angle != 0 else mrandom.randrange(-90,90)
			self.velocity = [angle,5]
			self.position = (self.screen.get_width()/2, self.screen.get_height()/2)
		elif self.position[1] <= 0:
			self.velocity = [-self.velocity[0], self.velocity[1]]
			self.position = (self.position[0], self.size)
		elif self.position[1] >= self.screen.get_height():
			self.velocity = [-self.velocity[0], self.velocity[1]]
			self.position = (self.position[0], self.screen.get_height())
		self.bounding_box = pg.draw.circle(self.screen, (255,255,255), self.position, self.size)

		if self.hit:
			self.counter += 1

		if self.counter == 10:
			self.counter = 0
			self.hit = not self.hit

		return point

	def get_position_change(self):
		return (self.velocity[1]*math.cos(self.velocity[0]), self.velocity[1]*math.sin(self.velocity[0]))

	def check_collision(self, paddle):

		if self.bounding_box.colliderect(paddle.bounding_box) and not self.hit:
			paddle_center = (paddle.bounding_box[0]+paddle.bounding_box[2]/2, paddle.bounding_box[1]+paddle.bounding_box[3]/2)

			deltas = self.get_position_change()
			if paddle_center[1] > self.screen.get_height()/2:
				magnitude = (paddle_center[1] - self.bounding_box[1]) + 1
			else:
				magnitude = (self.bounding_box[1] - paddle_center[1]) + 1
			magnitude = 5 if magnitude > 5 else magnitude

			self.velocity = [math.pi - self.velocity[0], self.velocity[1]]
			# self.velocity = (math.pi - self.velocity[0], magnitude)
			self.update()

class Paddle(object):
	def __init__(self, screen, dimensions=(2, 20), position=(0,0)):
		self.screen = screen
		self.dimensions = dimensions
		self.position = position
		self.bounding_box = pg.draw.rect(self.screen, (255,255,255), self.compose_rect())

	def update(self):
		if self.position[1] <= 0:
			new_position = (self.position[0], 0, self.dimensions[0], self.dimensions[1])
			self.bounding_box = pg.draw.rect(self.screen, (255,255,255), new_position)
			self.position = (self.position[0], 0)
		elif self.position[1] + self.dimensions[1] >= 480:
			new_position = (self.position[0], 480-self.dimensions[1], self.dimensions[0], self.dimensions[1])
			self.bounding_box = pg.draw.rect(self.screen, (255,255,255), new_position)
			self.position = (self.position[0], 480-self.dimensions[1])
		else:
			self.bounding_box = pg.draw.rect(self.screen, (255,255,255), self.compose_rect())

	def compose_rect(self):
		return (self.position[0], self.position[1], self.dimensions[0], self.dimensions[1])

	def up(self):
		self.position = (self.position[0], self.position[1]-20)

	def down(self):
		self.position = (self.position[0], self.position[1]+20)

def main():
	pg.init()

	size = width, height = 640, 480
	screen = pg.display.set_mode(size, pg.FULLSCREEN)
	clock = pg.time.Clock()
	font = pg.font.Font(None, 92)

	p1_score = 0
	p2_score = 0

	ball = Ball(screen, 10, position=(width/2,height/2))
	paddle1 = Paddle(screen, (8, 60), (15, 0))
	paddle2 = Paddle(screen, (8, 60), (width-15-8, height-60))

	paddle1_up = paddle1_down = False
	paddle2_up = paddle2_down = False

	while True:
		clock.tick(60)

		for event in pg.event.get():
			if event.type == QUIT:
				return
			elif event.type == KEYDOWN:
				if event.key == K_ESCAPE or event.key == K_q:
					return
				elif event.key == K_j:
					paddle2_down = True
				elif event.key == K_k:
					paddle2_up = True
				elif event.key == K_f:
					paddle1_down = True
				elif event.key == K_d:
					paddle1_up = True
			elif event.type == KEYUP:
				if event.key == K_j:
					paddle2_down = False
				elif event.key == K_k:
					paddle2_up = False
				elif event.key == K_f:
					paddle1_down = False
				elif event.key == K_d:
					paddle1_up = False

		if paddle1_down:
			paddle1.down()
		elif paddle1_up:
			paddle1.up()

		if paddle2_down:
			paddle2.down()
		elif paddle2_up:
			paddle2.up()

		screen.fill((0,0,0))
		ball.check_collision(paddle1)
		ball.check_collision(paddle2)
		point = ball.update()
		if point == 1:
			p1_score += 1
		elif point == 2:
			p2_score += 1
		paddle1.update()
		paddle2.update()
		screen.blit(font.render(str(p1_score), False, (255,255,255)), (screen.get_width()/4, 10))
		screen.blit(font.render(str(p2_score), False, (255,255,255)), (screen.get_width()/2+screen.get_width()/4, 10))
		ball.velocity[1] += .1
		pg.display.flip()

if __name__ == "__main__":
	main()

#! /usr/bin/env python
import pickle

class Player (object):
	def __init__(self):
		self.hitpoints = 100
		self.manapoints = 100
		self.location = 'veridian hills'
	
	def take_damage(self, damage):
		self.hitpoints -= damage

	def use_mana(self, mana):
		self.manapoints -= mana

	def change_location(self, location):
		self.location = location

	def __str__(self):
		return "<Player -- HP:%d MP:%d Loc:%s>" % (self.hitpoints, self.manapoints, self.location)

	def __repr__(self):
		return self.__str__()
	
def main():
	player1 = Player()

	print player1

	player1.take_damage(20)
	player1.use_mana(44)
	player1.change_location('mordor')

	print player1

	with open('saved_player.pkl', 'w') as f:
		pickle.dump(player1, f)

	player1 = None

	print player1

	with open('saved_player.pkl', 'r') as f:
		player1 = pickle.load(f)

	print player1

if __name__ == "__main__":
	main()

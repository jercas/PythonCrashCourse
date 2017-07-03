#coding=utf-8
#random P160 2017.4.20
from random import randint

class Die():
	def __init__(self,sides=6):
		self.sides = sides
	def rollDie(self):
		x = randint(1,self.sides)
		return x
die = Die(100)
print(die.rollDie())

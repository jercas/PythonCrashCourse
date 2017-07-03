#coding=utf-8
#冰淇淋小店P153 2017.4.20
from restaurant import Restaurant
class IceCreamStand(Restaurant):
	"""继承餐厅类，加以重写"""
	def __init__(self,name,cuisine,flavors):
		super().__init__(name,cuisine)
		self.flavors = flavors
	def showFlavors(self):
		print(flavors)
flavors = ['strawberry','chocolate','watermelon']
iceCreamStand = IceCreamStand('Haagen-Dazs','ice-cream',flavors)
print()
iceCreamStand.openRestaurant()
iceCreamStand.describeRestaurant()
iceCreamStand.showFlavors()

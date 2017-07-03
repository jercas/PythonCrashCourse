#coding=utf-8
#餐馆P142 2017.4.20
class Restaurant():
	"""餐厅类 模拟餐厅运营"""
	def __init__(self,restaurantName,cuisineType):
		self.restaurantName = restaurantName
		self.cuisineType = cuisineType
		self.numberService = 0
	def describeRestaurant(self):
		print("Our restaurant name is " + self.restaurantName.title())
		print("The best cuisine type of our chef is " + self.cuisineType.upper())
	def showGuestNum(self):
		print("Now there are " + str(self.numberService) + " guests" )
	def setNumberService(self,numberService):
		self.numberService = numberService
	def incrementService(self,numberService):
		self.numberService += numberService
	def openRestaurant(self):
		print("Open now!")
	
restaurantJer = Restaurant('stella','Chinese Food')
restaurantJer.describeRestaurant()
restaurantJer.openRestaurant()
restaurantJer.showGuestNum()
restaurantJer.numberService = 10
restaurantJer.showGuestNum()
restaurantJer.setNumberService(20)
restaurantJer.showGuestNum()
restaurantJer.incrementService(10)
restaurantJer.incrementService(10)
restaurantJer.incrementService(10)
restaurantJer.showGuestNum()

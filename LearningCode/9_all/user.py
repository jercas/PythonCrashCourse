#coding=utf-8
#用户P142 2017.4.20
class User():
	"""用户简介类"""
	def __init__(self,firstName,lastName):
		self.firstName = firstName
		self.lastName = lastName
		self.loginAttempts = 0
	def describeUser(self):
		print("User's name is " + self.firstName.title() + " " + self.lastName.title())
	def greetingUser(self):
		print("Welcome back!")
	def incrementLoginAttempts(self):
		self.loginAttempts += 1
	def resetLoginAttempts(self):
		self.loginAttempts = 0
	def showLoginAttempts(self):
		print("LoginAttempts: " + str(self.loginAttempts))
jer = User("jercas","cas")
jer.describeUser()
jer.greetingUser()
jer.incrementLoginAttempts()
jer.showLoginAttempts()
jer.incrementLoginAttempts()
jer.incrementLoginAttempts()
jer.incrementLoginAttempts()
jer.incrementLoginAttempts()
jer.showLoginAttempts()
jer.resetLoginAttempts()
jer.showLoginAttempts()

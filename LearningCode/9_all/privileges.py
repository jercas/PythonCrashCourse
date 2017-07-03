#coding=utf-8
#权限P153 2017.4.20
from user import User
class Privileges(User):
	"""用户权限类"""
	def __init__(self,firstName,lastName,privileges):
		super().__init__(firstName,lastName)
		self.privileges = privileges
	def showPrivileges(self,key):
		key = int(key)
		if key >2:
			print("ERROR LEVEL！")
		else:
			print("Dear " + self.firstName.title() + self.lastName.title() +
			  ",Your level is " + self.privileges[key].title())

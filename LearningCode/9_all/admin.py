#coding=utf-8
#管理员P153 2017.4.20
from user import User
from privileges import Privileges

class Admin(User):
	"""继承并重写用户类，构建管理员类"""
	def __init__(self,firstName,lastName,privileges):
		super().__init__(firstName,lastName)
		self.privileges = Privileges(firstName,lastName,privileges)
		
privileges = ['can add post','can delete post','can ban user'] 
admin = Admin('jercas','cas',privileges)
print()
admin.describeUser()
admin.greetingUser()
admin.privileges.showPrivileges(0)

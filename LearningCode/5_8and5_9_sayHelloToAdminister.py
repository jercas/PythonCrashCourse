#coding=utf-8
#以特殊方式跟管理员打招呼P79 2017.4.14
users = ['jer','cas','ety','admin']
for user in users:
	if user == 'admin':
		print("Hello admin,would you like see a status report?")
	else:
		print('Hello '+user+',thank you for logging in again!')
index = 3
while index >= 0:
	del users[index]
	index -= 1
if len(users)==0:
	print("\nWe need to find some users!")
else:
	print("\nWe still have "+str(len(users))+' users')

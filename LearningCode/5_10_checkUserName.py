#coding=utf-8
#检查用户名P79 2017.4.14
current_users = ['jer','cas','ety','a','b']
new_users     = ['JER','Cas','x','y','z'  ]

for new_user in new_users:
	if new_user.upper() in current_users:
		print('Sorry!The username '+new_user.title()+' has been used,You must change your input!')
	elif new_user.title() in current_users:
		print('Sorry!The username '+new_user.title()+' has been used,You must change your input!')
	elif new_user.lower() in current_users:
		print('Sorry!The username '+new_user.title()+' has been used,You must change your input!')
	else:
		print('Register Success!')

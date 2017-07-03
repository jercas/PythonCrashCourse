#coding=utf-8
#人生不同阶段P76 2017.4.14
age = 1
while age>0:
	try:
		age = input('please input your age (input 0 to exit)\n')
		age = int(age)
	except:
		print("ERROR INPUT,please input a right age!\n")
		age = 1
		continue
	if age<2:
		print('You are just a little baby')
	elif age>=2 and age<4:
		print('oh~ You should learn how to walk and run')
	elif age>=4 and age<13:
		print("Little guy,it's time to go to school")
	elif age>=13 and age<20:
		print('Teenager go to search your own lover')
	elif age>=20 and age<65:
		print('MAN,you are the middle of your famliy')
	elif age>=65 and age<120:
		print("Oldman,which moment you can forgot in your whole life?")
	else:
		print("Don't kidding me,OK?")


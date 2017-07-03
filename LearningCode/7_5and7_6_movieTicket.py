#coding=utf-8
#电影票P110 2017.4.17
active = True
fee = [value*5 for value in range(0,4)]
del fee[1]
while active:
	age = input("Please input your age to buy ticket!(input any negative num to exit)\n")
	try:
		age = int(age)
	except:
		print("You must input a num not a character!\n")
		continue
	if age<=0:
		break
	elif age>0 and age<3:
		print("The baby is free"+"\n")
	elif age>=3 and age<12:
		print("The fee of little child is " + str(fee[1])+"\n")
	elif age>=12:
		print("The fee of adult is " + str(fee[2])+"\n")

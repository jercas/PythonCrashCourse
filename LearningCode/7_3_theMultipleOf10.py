#coding=utf-8
#10的整数倍P104 2017.4.17
active = True
while active:
	num = input("Please input a num and we'll check it!(input any negative num to exit)\n")
	try:
		num = int(num)
	except:
		print("You must input a num not a character!\n")
		continue
	if num<=0:
		break
	elif num%10==0:
		print('\n'+str(num)+' is a multiple of 10')
	else:
		print('\n'+str(num)+" isn't a multiple of 10")

#coidng=utf-8
#外星人P75-76 2017.4.13
alien_color = ['green','yellow','red']
scores = 0
short = 1

print("Let's kill the aliens!")
while short>0:
	try:
		short = input("please short in '1,2,3'.(input 0 o quit)\n")
		short = int(short)
	except:
		print("ERROR INPUT! You must input a number! Please try again!\n")
		short = 1
		continue
	if short == 1: 
		scores += 5
		print('You kill a '+alien_color[0]+' alien! '+'You got 5 score!\t'+'Now you have '+str(scores)+'！')
	elif short == 2:
		scores += 10
		print('You kill a '+alien_color[1]+' alien! '+'You got 10 score!\t'+'Now you have '+str(scores)+'！')
	elif short == 3:
		scores += 15
		print("You kill a "+alien_color[2]+" alien! "+"You got 15 score!\t"+"Now you have "+str(scores)+"！")
	else:
		print('MISS!')
print('Welcome back!')

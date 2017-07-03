#coding=utf-8
#加法运算器P179 2017.4.21
def add():
	active = True
	filename = 'addResult.txt'
	while active:
		num1 = input("Please input your addend.\n")
		num2 = input("Please input your summand.(input a negative num to exit)\n")
		try:
			num1 = int(num1)
			num2 = int(num2)
		except:
			print("Sorry cann't calculate!!!You must input a num not a character!Please try again\n")
			continue
		else:
			if num1<0 or num2<0:
				active = False
				continue
			else:
				result = num1 + num2
				print('Both of them add result is '+str(result)+'\n')
				with open(filename,'a') as file_object:
					file_object.write(str(num1)+'+'+str(num2)+'='+str(result)+'\n')
add()

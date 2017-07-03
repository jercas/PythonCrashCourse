#coding=utf-8
#喜欢的数字P185 2017.4.21
import json

def getNum(filename):
	try:
		with open(filename,'r')as file_object:
			num = json.load(file_object)
	except FileNotFoundError:
		print("We cann't found the file: "+filename+'\n')
	else:
		return num

def newNum(filename):
	num = input("Please input your favorite num \n")
	with open(filename,'w')as file_object:
		json.dump(num,file_object)
	return num
	
def greet(filename):
	num = getNum(filename)
	if num:
		if num:
			print("Your favorite num is " + num)
	else:
		num = newNum(filename)
		print("We remeber that your favorite num is "+ num)

greet('num.json')

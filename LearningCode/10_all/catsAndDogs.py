#coding=utf-8
#猫和狗P179 2017.4.21
def writeIt(filename,t):
	while t>0:
		petName = input("Please input a pet's name\n")
		with open(filename,'a') as file_object:
			file_object.write(petName+'\n')
		t-=1
def readIt(filename):
	try:
		with open(filename,'r') as file_object:
			for line in file_object:
				print(line.rstrip())
	except FileNotFoundError:
		print("We cann't found the file: "+filename)
		#pass
writeIt('dogs.txt',3)
readIt('cats.txt')
#readIt('dogs.txt')
		

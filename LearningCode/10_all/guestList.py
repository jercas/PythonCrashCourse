#coding=utf-8
#访客名单P172 2017.4.21
filename = 'guestBook.txt'
def writeIt():
	active = True
	while active:
		guestName = input("Please input your name.(input 'quit' to exit)\n")
		if guestName == 'quit':
			active = False
			continue
		else:
			print("Welcome join in ! " + guestName + '\n')
			with open(filename,'a') as file_object:
				file_object.write(guestName + '\n')
def readIt():
	with open(filename,'r') as file_object:
		for line in file_object:
			print(line.rstrip())
writeIt()
readIt()

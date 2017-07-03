#codnig=utf-8
#访客P172 2017.4.21
def guestPrint():
	guestName = input("Welcome! Please input your name.\n")
	filename = 'guest.txt'
	with open(filename,'w') as file_object:
		file_object.write(guestName)
	with open(filename,'r') as file_object:
		print(file_object.read())
guestPrint()

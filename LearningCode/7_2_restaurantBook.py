#coding=utf-8
#餐馆订位P104 2017.4.17
active = True
while active:
	bookNum = input("How many peopel are having dinner？\n")
	try:
		bookNum = int(bookNum)
	except:
		print("You must input a num not a character!\n")
		continue
	if bookNum>=8:
		print("Sorry,you should wait for another table.")
	else:
		print("Please follow me,wish you'll have a nice dinner!")
	active = False

#coding=utf-8
#披萨配料P110 2017.4.17
active = True
while active:
	seasoning = input("please input the seasoning that you want to add in your pizza"+
					"(input 'quit' to exit)\n")
	if seasoning == 'quit':
		break
	else:
		print("We'll add "+seasoning+' your pizza!')

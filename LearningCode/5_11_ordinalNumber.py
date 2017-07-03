#coding=utf-8
#序数P80 2017.4.14
ordinalNumbers = ['1','2','3','4','5','6','7','8','9']
for ordinalNumber in ordinalNumbers:
	if int(ordinalNumber) == 1:
		print(ordinalNumber+'st\n')
	elif int(ordinalNumber) == 2:
		print(ordinalNumber+'nd\n')
	elif int(ordinalNumber) == 3:
		print(ordinalNumber+'rd\n')
	else:
		print(ordinalNumber+'th\n')

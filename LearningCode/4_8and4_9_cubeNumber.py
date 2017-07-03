#coding=utf-8
#立方P54 2017.4.12
number1 = []
for value in range(1,11):
	baseNum = value
	number1.append(baseNum**3)
print(number1)

number2 = [value**3 for value in range(1,11)]
print(number2)

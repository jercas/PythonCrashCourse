#coding=utf-8
#河流P93 2017.4.14
rivers = {
	'Nile':'egypt',
	'Yangtza':'china',
	'Mississippi':'america',
	}
print("Let's view some of the most famous river in the world!\n")
for riverName in rivers.keys():
	print(riverName)
print("\nSo,where does it been?\n")
for riverNation in rivers.values():
	print(riverNation.title())
print("\nNow you know that:\n")
for riverName,riverNation in rivers.items():
	print("The "+riverName+" runs through "+riverNation.upper())

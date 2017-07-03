#coding=utf-8
#自助餐P60 2017.4.12
foods = ('chicken','noodles','dumplings','steamd-dumplings','steak')
for food in foods:
	print(food)
try:
	foods[0] = 'fish'
except:
	print("\nyou cann't assignment the item of it\n")
print('But you can change the whole of it\n')
foods=('fish','pudding','milk','cooks','cake')
for food in foods:
	print(food)

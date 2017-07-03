#coding=utf-8
#你的披萨和我的披萨P58 2017.4.12
myPizzas = ['apple','banana','cherrys']
yourPizzas = myPizzas[:]
myPizzas.append('myFavoriteFruit')
yourPizzas.append('yourFavoriteFruit')
print('My favorite pizza are: '+str(myPizzas))
print('Your favorite pizza are: '+str(yourPizzas))

for myPizza in myPizzas:
	print(myPizza)
	for pizza in myPizza[0:1]:
		print(pizza)

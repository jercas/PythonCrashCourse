#coding=utf-8
#喜欢的水果P76 2017.4.14
favorite_fruit = ['apple','banana','watermelon']
fruit = input("'apple','banana','watermelon' Which one is your favorite fruit?\n")

if fruit == favorite_fruit[0]:
	print('You really like apple!')
elif fruit == favorite_fruit[1]:
	print('You really like banana')
elif fruit == favorite_fruit[2]:
	print('You really like watermelon')
else:
	print('ERROR INPUT,please just input one of apple,banana or watermelon')


#coding=utf-8
#熟食店P113 2017.4.17
sandwichOrders = ['fruitSandwich','baconicSandwich','beefSandwich','pastrmiSandwich']
finishedSandwiches = []
print("Now we have")
print(sandwichOrders)
print("\nOpps!The pastramiSandwich is sold out!")
for sandwichOrder in sandwichOrders:
	if sandwichOrder == 'pastrmiSandwich':
		sandwichOrders.remove(sandwichOrder)
while sandwichOrders:
	sandwich = sandwichOrders.pop()
	print("I made your "+sandwich+'\n')
	finishedSandwiches.append(sandwich)
print(finishedSandwiches)

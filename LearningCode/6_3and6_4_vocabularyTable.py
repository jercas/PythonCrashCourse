#coding=utf-8
#词汇表P87andP93 2017.4.14
vocabularyTables = {
	'fruit':'apple',
	'sport':'basketball',
	'digitalDevice':'iphone',
	}
def showTheTable():
	for vocabulary in vocabularyTables.keys():
		print(vocabulary+"'s meaning is "+vocabularyTables[vocabulary])
showTheTable()

vocabularyTables['fruit'] = 'banana'
print("\n Let's change a value in vocabulary")
showTheTable()

vocabularyTables['person'] = 'jercas'
print("\n Let's insert a key-value in vocabulary")
showTheTable()

del vocabularyTables['person']
print("\n Let's delete a key-value in vocabulary")
showTheTable()
	

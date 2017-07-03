#coding=utf-8
#条件测试P70 2017.4.13
num = 1994
name = 'jercas'
lists = ['jer','cas','ety']
jercasIsHandsome = True

print("Let's start our test!")
print("\nIs name equal 'jercas'?")
if name == 'jercas':
	print('Yes!')
else:
	print('Nope!') 

print("\nIs name equal 'Jercas'?")
if name.title() == 'jercas':
	print('Yes!')
else:
	print('Nope!') 

print("\nIs num equal 80?")
if num == 80:
	print('Yes!')
else:
	print('Nope!') 

print("\nSo,Which is bigger between 80 and num?")
if num>80:
	print('num is bigger!')
else:
	print('80 is bigger!') 

print("\nIs item-'cas' in the list?")
if 'cas' in lists:
	print('Yes!')
else:
	print('Nope!') 

print("\nSo？How about 'abc'?")
if 'abc' in lists:
	print('Yes!')
else:
	print('Nope!') 

print("\nWoo!Let me think,'xyz' must not in the list")
if 'xyz' not in lists:
	print('Yes!')
else:
	print('Nope!') 

print("\nLast one,Is jercas handsome?")
if jercasIsHandsome:
	print('Yes!')
else:
	print('Nope!') 

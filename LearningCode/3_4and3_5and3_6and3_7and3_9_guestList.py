#coding=utf-8
#嘉宾名单P38 2017.4.11
print('3.4 输出嘉宾名单')
guestLists = ['wade','kobe','jordan']
def hiGuest():
	for guestList in guestLists:
		print('Hi '+guestList+',welcome to my party!')
hiGuest()
print('\n3.5 修改嘉宾名单')
print("it's so sorry that maybe "+guestLists[1]+" don't have time to join us")
guestLists[1]='harden'
hiGuest()
print('\n3.6 添加嘉宾名单')
print("amazing! guess what? I just find a bigger table,Let's invite more bobdys to come here! ")
guestLists.append('curry')
guestLists.insert(0,'durant')
hiGuest()
print('\n3.7 删除嘉宾名单')
print("oh!damn it!The table is too small to contain us... so i'd better tell them to stay home")
t=2
while t>=0:
	loser = guestLists.pop()
	print('sorry '+loser+" maybe next time?")
	t -= 1
for guestList in guestLists:
	print(guestList+" don't worry,you still in my list!")
del guestLists[0]
print('\ncongratulation! '+guestLists[0]+' you are the only one!')
print('I already invite '+str(len(guestLists))+' guys to my party')



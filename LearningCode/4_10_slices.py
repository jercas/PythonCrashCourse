#coding=utf-8
#切片P58 2017.4.12
print("Let's try to slice our list")
lists = ('a','b','c','d','e','f','g')
print('The first three items of the list are:\t'+str(lists[:3]))
count = int(len(lists))
print('The middle three items of the list are:\t'+str(lists[count//2-1:count//2+2]))
#Python 3 中的地板除： A//B 结果为int 而普通除：A/B 结果为float
print('The last three items of the list are:\t'+str(lists[-3:]))

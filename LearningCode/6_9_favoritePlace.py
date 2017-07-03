#coding=utf-8
#喜欢的地方P99 2017.4.17
favoritePlaces = {
	'jer':['beijing','guangzhou','zhuhai'],
	'cas':['zhenzhou','nanjing','luoshan'],
	'ety':['fuzhou','xiamen','hongkoo'],
	}
for key,value in favoritePlaces.items():
	print(key+"'s favorite place as follows -- "+str(value))
print(favoritePlaces['jer'][1]) 

#coding=utf-8
#城市P99 2017.4.17
cities = {
	'beiJing':{
		'country':'China',
		'fact':'capital',
		},
	'newYork':{
		'country':'America',
		'fact':'economicalCity',
		},
	'oxford':{
		'country':'britain',
		'fact':'educationCity',
		}
	}
cities['luoshan']={
	'country':'China',
	'fact':'myHometown',
}
del cities['newYork']
for cityName,cityInfo in cities.items():
	print('cityName:'+cityName.title())
	print('country:'+cityInfo['country'])
	print('fact:'+cityInfo['fact'].title()+'\n')

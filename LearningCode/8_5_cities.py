#coding=utf-8
#城市描述P121 2017.4.18
def describeCity(cityName,belongCountry = 'China'):
	print(cityName.title() + ' is in ' + belongCountry.title())
describeCity('beijing')
describeCity('guangzhou')
describeCity('los angles','american')

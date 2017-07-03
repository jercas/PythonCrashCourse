#coding=utf-8
#城市名P125 2017.4.18
def cityCountry(cityName,belongCountry):
	info = cityName.title() + ' - ' + belongCountry.upper()
	return info
print(cityCountry('beijing','china'))
print(cityCountry('london','britain'))
print(cityCountry('houston','the-USA'))

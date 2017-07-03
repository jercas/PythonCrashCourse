#coding=utf-8
#汽车信息P132 2017.4.18
def describeCar(manufacturer,model,**otherInfo):
	carInfo = {}
	carInfo['manufacturer'] = manufacturer
	carInfo['model'] = model
	for key,value in otherInfo.items():
		carInfo[key] = value
	return carInfo
carInfo = describeCar('Benz','C200L',
					 color = 'Blue',
					 towPackage = True)
print(carInfo)

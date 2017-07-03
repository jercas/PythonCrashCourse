#coding=utf-8
#用户简介P132 2017.4.18
def buildProfile(firstName,lastName,**userInfo):
	profile={}
	profile['firstName'] = firstName
	profile['lastName']  = lastName
	for key,value in userInfo.items():
		profile[key] = value
	return profile
	
userProfile = buildProfile('Jercas','Ety',
							hometown = 'LuoShan',
							educationBackground = 'master')
print(userProfile)

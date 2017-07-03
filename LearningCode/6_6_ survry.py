#coding=utf-8
#调查P93 2017.4.17
favoriteLanguages = {
	'jen':'python',
	'sarah':'c',
	'edward':'ruby',
	'phil':'java',
	}
surveyLists = ['jen','sarah','edward','phil','jercas']
alreadyHaveSurveys = []
for name in favoriteLanguages.keys():
	if name in surveyLists:
		alreadyHaveSurveys.append(name)
		
for surveyList in surveyLists:
	if surveyList in alreadyHaveSurveys:
		for name,result in favoriteLanguages.items():
			if surveyList == name:
				print("Thanks,"+name+',thank you for join my survey!Your favorite language is '+result+'\n')	
	else:
		print(surveyList+" come to have a survey!")

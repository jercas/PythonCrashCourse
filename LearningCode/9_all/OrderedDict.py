#coding=utf-8
#使用OrderedDict P160 2017.4.20
from collections import OrderedDict
languages = OrderedDict()
languages['jen'] = 'python'
languages['sarah'] = 'c'
languages['edward'] = 'ruby'
languages['phil'] = 'c++'
for name,language in languages.items():
	print(name.title()+"--"+language.title())

xyz = {
	'a':'a',
	'b':'b',
	'c':'c',
	}
xyz['d']='d'
for key,value in xyz.items():
	print(key+"--"+value)

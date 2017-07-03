#coding=utf-8
#魔术师P129 2017.4.18
magicians = ['liu qian','david copperfield','jay zhou']

def makeGreat(magicians):
	t=0
	for magician in magicians:
		#两种字符串拼接方法
		#1
		#together = ['The Great ',magician]
		#magician = ''.join(together)
		#2
		magician = 'The Great '+magician
		magicians[t] = magician
		t+=1
	return magicians
		
def showMagician(magicians):
	for magician in magicians:
		print(magician)
#仅传递列表副本 不修改所传实参本身，于是只有函数范围内的返回列表被修改，原传列表内容不变
alterMagicians = makeGreat(magicians[:])
showMagician(alterMagicians)
print()
showMagician(magicians)

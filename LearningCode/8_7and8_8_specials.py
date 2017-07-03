#coding=utf-8
#专辑P125 2017.4.18
def makeAlbum(singer,album,songNum = ''):
	info = {
		'singer':singer,
		'album':album,
		}
	if songNum:
		info['songNum']=songNum
	return info
print(makeAlbum('a','b'))
print(makeAlbum('a','b','10'))

active = True
while active:
	print("\nLet's input info of album (input 'quit' to exit)")
	singer = input("Please input the singer's name:\n")
	if singer == 'quit':
		break
	album  = input("Please input the album's name:\n")
	if album == 'quit':
		break
	songNum = input("Please input the songNum of the album:\n")
	if songNum == 'quit':
		break
	print(makeAlbum(singer,album,songNum))

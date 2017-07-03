#coding=utf-8
#常见单词统计P180 2017.4.21
def countWords(filename):
	try:
		with open(filename,'r') as file_object:
			contents = file_object.read()
	except FileNotFoundError:
		print("We cann't found the file: "+filename)
	else:
		words = contents.split()
		wordNum = len(words)
		theWord = words.count('than')
		print("The file " + filename + " has about " +str(wordNum)+" words\n")
		print("The word 'than' has about " + str(theWord) )
countWords('zen.txt')

#coding=utf-8
#Python学习笔记 P169 2017.4.20
fileName = 'pythonStudyNote.txt'
with open(fileName) as file_object:
	print(file_object.read())
print()

with open(fileName) as file_object:
	for line in file_object:
		print(line.replace('better','worse').rstrip())
print()

with open(fileName) as file_object:
	lines = file_object.readlines()
for line in lines:
	print(line.replace('s','AAA',2).rstrip())
#字符串替换函数replace只修改副本不修改内存本身，即只在当前句有效，且三个参数 old,new,max 其中
#max参数是指只对当前句中的字符修改有效，而非循环中多次的效用

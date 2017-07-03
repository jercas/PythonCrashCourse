#coding=utf-8
#打印模型P137 2017.4.18

import printFunction
printFunction.printIt('abc')

import printFunction as prt
prt.printIt('efg')

from printFunction import printIt
printIt('ety')

from printFunction import printIt as printForMe
printForMe('Jer cas')

from printFunction import *
printIt('xyz')

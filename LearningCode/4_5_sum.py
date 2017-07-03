#coding=utf-8
#计算1~1000000的总和P54 2017.4.12
numbers = [value for value in range(0,1000001)]
print('起始数字：'+str(min(numbers)))
print('结尾数字：'+str(max(numbers)))
print('总和：'+str(sum(numbers)))
#PS:对min max sum 函数 直接用print输出时是输出其返回值，无需str变数据类型 例print(min(numbers))可直接输出，但如上格式如果
#不加str 会报不是str类型无法输出Bug

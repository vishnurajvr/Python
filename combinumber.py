from argparse import ArgumentParser
import sys

#argparse help us to command line argument 
parser = ArgumentParser(
						description ="sum of the combined number(like:1234) in string or int",
						epilog ='''
								py combinumber.py -v 1234
										 or 
								py combinumber.py -i 1234
								'''
						)
rparser = parser.add_argument_group("Required options")
rparser.add_argument('-v','--value',type=str,dest='value2',help='Enter the value')
rparser.add_argument('-i','--intergers',type=int,dest='value1',help='Enter the value')

args = parser.parse_args()

#one() function is convert string to int and sum of the value
def one(value):
	store = []

	#sum is default function in python so i use _sum
	_sum = 0

	#The string convert to list like casting 
	value = list(value)

	#They have combined value is split and save to list 
	#in the type of string
	for x in value:
		store.append(x)

	#sum of value like 1234 ===> 1+2+3+4=10
	for x in store:
		_sum = int(x) + _sum

	print('The sum of String number is :',_sum)
	
	return _sum

#two() fuction is they value is int not string 
#so we use this type of method
def two(value):
	_sum = 0
	
	while value != 0:
		_sum = (value%10) + _sum
		value = value//10
	
	print("The sum of Interger number is : ",_sum)

#This num() function is check the value is string or int
value = args.value1 or args.value2
def num(value):	
	if(type(value) == str ):
		one(value)
	else:
		two(value)

if(len(sys.argv)!=0):
	try:
		num(value)
	except Exception as e:
		pass
else:
	sys.exit()
import termcolor
import random
import time

color_list = [
              'cyan','red','white','green',
              'blue','yellow'
              ]
rand = random.choice(color_list)
color = termcolor.colored

##Get number
num = int(input("Enter ur number : "))
sleep_get = int(input("Enter ur sleep value : "))
name=[]

#Get name
name_get=input("Enter your name : ")
#All letter convert to upper case sensitive
name_get=name_get.upper()

print()

##For word save in letter 
for x in name_get:
	name.append(x)

def star(name,num):
	num1=0
	num2=num

	for loop in range(num):
		print(color("%s "%(name),rand,attrs=['blink','bold'])*(num1+1)+
			  color(". ",'white',attrs=['bold'])*((num2-1)+(num2-1))+
			  color("%s ",rand,attrs=['blink','bold'])%(name)*(num1+1))
		num1=num1+1
		num2=num2-1
	time.sleep(sleep_get)
	for loop in range(num,1,-1):
		print(color("%s "%(name),rand,attrs=['blink','bold'])*(num1-1)+
			  color(". ",'white',attrs=['bold'])*((num2+1)+(num2+1))+
			  color("%s "%(name),rand,attrs=['blink','bold'])*(num1-1))
		num1=num1-1
		num2=num2+1
	time.sleep(sleep_get)	
	
	print()


##Each letter call to function(star)
for x in name:
	star(x,num)
	


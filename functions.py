'''
Write a simple script that demonstrate your understanding of functions in python 
'''
import re
#check if the string starts with "The" and ends with "spain"
txt = "The rain in Spain"
x = re.search("^The.*Swahili$", txt)

if x:
  print("YES! We have a match!")  
else:
  print("No match")
##########
import re
txt = "the rain in spain"
x = re.search("^the.*spain$", txt)

if x:
  print("YES! We have a match!")

else:
  print("No match")


#The findall() Function

import re
#Return a list containing every occurance of "ai"
txt = "The rain in Japan"
x = re.findall("ai", txt)
print(x)

#The search() Function
import re
txt = "The rain in china"
x = re.search("\s", txt)
print("The first white-space character is located in position:", x.start())

#The split() Function
import re
txt = "The rain in Swahili"
x =  re.split("\s", txt)
print(x)

#The sub() function
import re 
txt = "The flood in kaributule"
x = re.sub("\s", "9", txt)
print(x)

#match object
#this will print object
import re
txt = "The rain in tumbombele"
x = re.search("ai", txt)

#x = re.search("hellow", txt)
print(x)
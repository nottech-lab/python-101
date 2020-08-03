'''
Write a simple script that would take input from user using keyboard 
'''
#An exception is an event, which occurs during the execution of a program that disrupts the normal flow of the program's
#instructions.

#python Try Except
try:
  print(x)
except:
    print("An exception occured")

#Many exceptions
try:
  print(x)
except NameError:
  print("variable x is not defined")  
except:
   print("Something else went wrong") 

try:
  print("My name is Zuri")
except:
   print("something else went wrong") 

#Else
try:
   print("Hellow world")
except:
    print("something went wrong")
else:
    print("Everything is okay")
   
#Finally
try:
  print(b)
except:
    print("something going wrong")
finally:    
    print("The 'try except' is finished")
'''    
#try to open and write to a file that is not writable
try:
  f = open("kazimototo.txt")  
  f.write("hello")
except:
   print("something went wrong when writing to the file") 
finally:
    f.close()
 '''   
try:
  f = open("family-short.txt")
  f.write("Hellow")
except:
   print("Everything is okay to the file") 
finally:    
     f.close("family-short.txt")

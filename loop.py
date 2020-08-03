'''
Write a simple script that demonstrate your understanding of loops in python   
'''
#Create a class
#To create a class use keyword class
class MyOrange:
  x = 2
#create an objects namep1  
p1 = MyOrange()
print(p1.x)

#The __init__() Function
class Person:
  def __init__(self, name,age):
     self.name = name
     self.age = age
     
p1 = Person("John",89)
print(p1.name)
print(p1.age)

class Person:
  def __init__(self, name, age):  
    self.name = name
    self.age = age

  def myfunc(self):
   print("Hello my name is " + self.name)   
p1 = Person("John",89)   
p1.myfunc()

#The self parameter
class Person:
   def __init__(mysillyobject, name, age): 
    mysillyobject.name = name
    mysillyobject.age = age
    
   def myfunc(abc):   
    print("Hellow my name is " + abc.name)
   
p1 = Person("John",89)    
p1.myfunc()    



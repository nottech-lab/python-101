''' 
Write a simple script that demonstrate your understanding of conditional statements 
Simple If , if else , elif  
'''
#if statement
is_hot = True

if True:
    print("It's a hot day")
print("Enjoy Your Day")

#if else
is_hot = True
if is_hot:
    print("It's a hot day")
else:
    print("It's a cold day")  
  
#elif
name = "G"
if len(name) < 3:
    print("Name must be at least 3 characters long")
elif len(name) > 50:
    print("Name must be a maximum of 50 characters")
else:
    print("Name looks good")        



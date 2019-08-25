''' 
Write a simple script that demonstrate your understanding of conditional statements 
Simple If , if else , elif  
'''

#code for all condition statement

print("You enter a dark room with two doors. Do you go through #1 or #2")

door = raw_input(">")

if door == "1":
    print ("There is a giant bear here eating a cheese cake. What do you do?")
    print ("1. Take the cake.")
    print("2. Scream at the bear.")
    
    bear = raw_input(">")
    
    if bear == "1":
        print("The bear eats your face off. Good job!")
    elif bear == "2":
        print("The bear eats your legs off. Good job!")
    else:
        print("Well, doig %s is probably better. Bear runs away." % bear)
        
elif door == "2":
    print ("YOu stare into endless abyss at jedi retina.")
    print ("1. Blueberries.")
    print("2. Blue leather jackets")
    print("3. Understanding python for future use.")
    
    insanity = raw_input(">")
    
    if insanity -- "1" or insanity == "2":
        print("Your body survive powered by a mind of jello. Good job!")
    else:
        print("THe insanity rots your eyes into pools of muck. Good job!")
else:
    print("Yuo stumble and falls on a knife and die. Good job!")
        
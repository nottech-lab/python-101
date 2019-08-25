'''
Write a simple script to demonstrate your understanding of Variable,identifier and keywords
'''
my_name = ' Adams Simon'
my_age = 53 #its a lie
my_height = 6.2 #feet
my_weight = 63 #kg not sure
my_eyes = 'black'
my_teeth = 'gold'
my_hair = 'black'

print "Lets talk about %s."% my_name
print "He's %d feet tall."% my_height
print "He's %d pound heavy."% my_weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair."% (my_eyes,my_hair)
print "His teeth are usually %s depending on the coffee."%my_teeth

#This line is tricky, try to get it exactly right
print "If i add %d, %d, and %d I get %d."%(my_age, my_height, my_weight, my_age + my_height + my_weight)
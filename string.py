# '''
# Write a simple script to demonstrate your understanding of strings 
# '''
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who knows %s and those who %s "%(binary, do_not)

print x
print y

print "I said: %r." % x
print "I also said: '%s" % y

hilarious = "false"
joke_evaluation = "Isn't that a joke so funny?! %r"

print joke_evaluation % hilarious

w = "This is the left side of "
e = "a string with a right side"

print w + e
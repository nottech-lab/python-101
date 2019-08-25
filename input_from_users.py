'''
Write a simple script that would take input from user using keyboard 
'''
from sys import argv

script, Adam = argv
prompt = '>'

print "Hi %s I'm the %s script."% (Adam, script)
print "I'd like to ask you few questions."
print "Do you like me %s?" % Adam
likes = raw_input(prompt)

print "Where do you live %s" % Adam
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print """
Alright, so you said %r about liking me.
You live in %r, Not sure where that is. 
And you have a %r computer. Nice.
""" % (likes, lives, computer)
'''
Write a simple script that would take input from user using keyboard 
'''

fhand = open('family-short.txt')
inp = fhand.read()
print(len(inp))
print(inp[:6])
print(fhand)
print(inp[1:4])
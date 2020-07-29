'''
Write a simple script that demonstrate your understanding of loops in python   
'''

#count loop

count = 1
while (count < 6):
   print 'The count is:', count
   count = count + 1

print "Count!"


#break loop

for letter in 'Python': 
   if letter == 'h':
      break
   print 'Current Letter :', letter


#Sequence

    number = ["1","2","3","4"]
    for n in number:
        print(n)
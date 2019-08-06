count = 0
total = 0
while count <= 10:
    total += count 
    count += 1

print('Sum of first 10 numbers is:', total)

for num in range(10,20):
  for i in range(2,num):
    if num%i == 0:
        j= num / i
        print ('%d equals %d * %d' % (num,i,j))
        break
    else:
        print (num, 'is prime number')        

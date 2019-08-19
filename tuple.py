'''
Write a simple script to demonstrate your understanding of tuples as data types 
'''
#here is the demostration of tuple with its function ie max(), min(), and len()
tuple1 = ( 'Mine' , 'Yours' , 'Ours' )
tuple2 = ( 30 ,45, 60 , 90 , 180 , 360 )
tuple3 = tuple1 + tuple2
print ("tuple3",tuple3)
print ("first tuple length:", len(tuple1))
print ("second tuple length:", len(tuple2))
print ("max value element:", max(tuple1))
print ("max value element:", max(tuple2))
print ("min value element:", min(tuple1))
print ("min value element:", min (tuple2))
print ("tuple1[1:5]:", tuple1[1:5])
print ("tuple2[1:5]:", tuple2[1:5])
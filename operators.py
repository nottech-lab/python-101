'''
Write a simple script that demonstrate your understanding of Operators,operands and operator precedence
'''
#Operators are used to perform operations on variables and values(Mathematical and logical operations)

single_watch_cost = 22000
available_watches = 20
parking_cost = 1000
available_money= 50000


#1.Arithmetic Operations
total_cost = single_watch_cost + parking_cost                        #addition,[total_cost is 23000]

remaining  = available_money - total_cost                            #substraction,[remaining is 27000]

parking_slots = available_money / parking_cost                       #division,[parking_slots is 50]

total_watch_cost = single_watch_cost * available_watches             #multiplication,[total_watch_cost is 440,000]

remainder = available_money % total_cost                             #modulus,[remainder is 4000]

watches_i_can_buy = available_money // single_watch_cost             #floor division,[watches_i_can_buy is 2]

#2.Assignment operators
watches_i_want =  20                                        #Assigning 20 to watches
watches_i_want += 5                                         #Same as: watches_i_want =watches_i_want + 5
watches_i_want -= 5                                         #Same as: watches_i_want = watches_i_want- 5
watches_i_want *= 10                                        #Same as: watches_i_want= watches_i_want * 10
watches_i_want /= 10                                        #Same as: watches_i_want = watches_i_want / 10


#3.Comparison operators
m == n                                              #checking if m equals n
m != n                                              #checking if m is not equal to n
m  > n                                              #checking if m is greater than n
m <= n                                              #checking if m  is less or equal to n

#4.Logical operators
available_watches < 10  and   watches_i_can_buy >10       #use of "and",returns TRUE if both are correct
available_watches < 5 or available_money > 50000          #use of "or",returns TRUE if one is correct
not(watches_i_want >10  and watches_i_can_buy < 7)                                     #reverses the answer
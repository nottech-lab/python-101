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
watches =  20                                        #Assigning 20 to watches
watches += 5                                         #Same as: watches = watches + 5
watches -= 5                                         #Same as: watches = watches - 5
watches *= 10                                        #Same as: watches = watches * 10
watches /= 10                                        #Same as: watches = watches / 10


#3.Comparison operators
m == n                                              #checking if m equals n
m != n                                              #checking if m is not equal to n
m  > n                                              #checking if m is greater than n
m <= n                                              #checking if m is less or equal to n

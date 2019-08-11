''' 
Write a simple script that demonstrate your understanding of conditional statements 
Simple If , if else , elif  
'''
                        # DECISION MAKING.

# Decision making structures require that programmer specifies one or more conditions to be evaluated or tested by the program.
# The statement or statements is executed if the condition is determined to be true or false.


                        # IF STATEMENTS.
# The if statement is used to check a condition: if the condition is true, we run a block of statements (called the if-block).
# Is used when there is only one option.

# if some_condition:
#   algorithm


# Example avoid division by zero
val = 0
num = 10
if val == 0:
    val += 2e-07
result = num / val
print("{0} dived {1:.2f} = {2:.2f}".format(num, val, result))


    
                          #  IF...ELSE STATEMENTS.
# Used when there is two option.

#   if some_condition:
#       algorithm
#   else:
#      algorithm



# Example avoid division by zero
user_name = "Daudi"
password = "1234"
if user_name=="Daudi":
    print("Hello ",user_name)
    if password !="1234":
        print("Wrong password")
    else: 
        print("Access granted")
else:
    print("user does not exist")

      
                        #  NESTED IF STATEMENTS.

# Is used when there is more than two option

#   if some_condition:
#      algorithm
#   elif some_condition:
#       algorithm
#   else:
#      algorithm


# Unlike other languages, indentation is significant
a = 5
if a > 10:
    print ('a is greater than 10')
    if a >= 15:
        print  ('a is also at least 15')
elif a > 5:
    print ('a is greater than 5 but not greater than 10')
else:
    print ('no condition matched')
    print ('so a is 5 or less')





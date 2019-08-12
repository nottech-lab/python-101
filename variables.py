'''
Write a simple script to demonstrate your understanding of Variable,identifier and keywords
'''

# The following script allows a user fill His or Her own required infomations and stores them

print("Please provide the required information")
# Takes the user inputs and stores them in the given variables
fullName = input("Full name: ")
dateOfBirth = input("Date of birth: ")
gender = input("Sex: ")
print("\n")

print("Please make sure the information you provided are correct")
# Prints out the received and stored user information
print("Full name: " + fullName)
print("Date of birth: " + dateOfBirth)
print("Sex: " + gender + "\n")

userFinalResponse = input("Type yes to submit and no to re-enter the required information: ")

'''
Write a simple script that would take input from user using keyboard 
'''
# NOTTECH FORM
print("NOTTECH DEVS REGISTRATION FORM")
age = int(input("We Need To Check Your Age \n Enter Your Age: "))
while(age < 18):
    print("Sorry Your Required To Have 18 Years and Above To Join ")
    age = int(input("We Need To Check Your Age \n Enter Your Age: "))

gender = input("Enter Your Gender: ")      
name = input("Enter Your Name: ")
address = input("Enter Your Address: ")
status = input("Enter Your Maritual Status: ")
                   
print("Your Have Successfuly Fill Details \n")
print("DEV'S DETAILS")
print("FULLNAME: " + name)
print("AGE: " + str(age))
print("GENDER: " + gender)
print("ADDRESS: " + address)
print("STATUS: " + status)
    #print(gender)
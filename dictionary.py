'''
Write a simple script to demonstrate your understanding of dictionaries as data types 
'''

#A dictionary is a collection which is unordered, changeable and indexed


#Creating a dictionary and printing it
TeamCaptains=	{
  "Liverpool": "Henderson",
  "Manchester city": "Silva",
  "Arsenal": "Shaka",
  "Tottenham": "Loris",
  "Real madrid": "Ramos",
}
print(TeamCaptains)

#Accessing items
print(TeamCaptains["Real madrid"])

#Change values
TeamCaptains["Liverpool"] ="Jkarage"
print(TeamCaptains)

#Looping in a dictionary
for k,y in TeamCaptains.items():
    print(k,y)

#Check if a key exists
if "Manchester united" in TeamCaptains:
    print("A great team")
else:
    print("Looser")

#Adding items
TeamCaptains["Simba"] ="Bocco"

#Remove an item
TeamCaptains.pop("Liverpool")

#Emptying the dictionary
TeamCaptains.clear()


#deleting the dictionary
del(TeamCaptains)
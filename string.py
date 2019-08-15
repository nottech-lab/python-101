'''
Write a simple script to demonstrate your understanding of strings 
''' 

motd = "Take it from me,being alive is lucky"
print(motd[1])                                     #returns second charecter, a

print(motd[2:5])                                   #returns 3rd char to 4th charecter,ke 

print(motd.strip())                                #returns "You say lucky is on your side!??",removes space at the begining and end of our str

print(len(motd))                                   #returns the length of the str

print(motd.lower())                                #returns the str in lower cases

print(motd.upper())                                #returns the str in upper cases

print(motd.replace("me", "Karage"))                #returns a str where me is replaced by Karage

print(motd.split(","))                             # returns a list of substrings separated by ,


print(motd.capitalize())                           #Capitalizes the first character and lowercases all others

print(motd.swapcase())                             ##Swaps case of each character
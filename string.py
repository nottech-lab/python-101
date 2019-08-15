'''
Write a simple script to demonstrate your understanding of strings 
''' 

motd = "Take it from me,being alive is lucky"
print(motd[1])                                     #returns second charecter,
#returns "a" 
                                                   
print(motd[2:5])                                   #returns 3rd char to 4th charecter,
#returns "ke" 
                                                    

motd_2= "   Take it from me,being alive is lucky   "
print(motd_2.strip())                              #removes space at the begining and end of our str,
#"Take it from me,being alive is lucky"
                                                    

print(len(motd))                                   #returns the length of the str,
#returns 36
                                                    

print(motd.lower())                                #returns the str in lower cases,
#"take it from me,being alive is lucky"
                                                  

print(motd.upper())                                 #returns the str in upper cases,
#"TAKE IT FROM ME,BEING ALIVE IS LUCKY"
                                                   


print(motd.replace("me", "Karage"))                  #returns a str where me is replaced by Karage,
#"Take it from Karage,being alive is lucky"
                                                   

print(motd.split(","))                               #returns a list of substrings separated by,
#['Take it from me', 'being alive is lucky']

                                                    

print(motd.capitalize())                             #Capitalizes the first character and lowercases all others,
#"Take it from me,being alive is lucky"
                                                     

print(motd.swapcase())                               #Swaps case of each charcter
#"tAKE IT FROM ME,BEING ALIVE IS LUCKY"

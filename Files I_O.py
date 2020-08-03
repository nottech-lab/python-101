'''
Write a simple script to demonstrate your understanding of Files IO
 
'''

#there must be a file in a computer with the specific name used in the codes to have results   

#opens the file in read mode

fileptr = open("file.txt","r")    
    
if fileptr:    
    print("file is opened successfully")
    
#open the file.txt in write mode.

fileptr = open("file2.txt", "w")
fileptr.write('''''Created file 2 and wrote.''')
fileptr.close()

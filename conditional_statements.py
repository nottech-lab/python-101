# Does if line execute?    
# let'see                    

if 'food' in ['banana', 'yams', 'potato']:        #  yes this condition executes
    print('Outer condition is true')      #  yes this condition executes


    if 10 > 20:   
        print('Inner condition 1') #this one does not execute

    print('Between inner conditions')     #  yes it does executes

    if 10 < 20:                           #  yes it does executes

        print('Inner condition 2')        #  yes it does executes
    print('End of outer condition')       #  yes it does executes

print('After outer condition')   #yes it does execute
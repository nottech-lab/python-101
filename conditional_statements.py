''' 
Write a simple script that demonstrate your understanding of conditional statements 
Simple If , if else , elif  
'''
watch_price =32000
shoe_price =40000
football_jersey =35000

#if 
if football_jersey <= 35000:
    print("I will buy the jersey")

#Testing conditions
if watch_price < shoe_price:
    print("I will take a watch")
else:
    print("I will take a shoe")

#using or
if watch_price = shoe_price or football_jersey <40000:
    print("I can afford both of them")

elif watch_price >football_jersey:
    print("I can never afford that")

else:
    print("I have to check the prices before deciding")
    
    

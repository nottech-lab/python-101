'''
Write a simple script to demonstrate your understanding of sets as data types 
'''
# Same as {"Adam", "Luka","Bruno"} 
normal_set = set(["adam", "luka","bruno"]) 

# Adding an element to normal set is fine 
normal_set.add("Brian") 

print("Normal Set") 
print(normal_set) 

# A frozen set 
disabled = frozenset(["James", "Hussein", "Peter"]) 

print("Disabled Set or Frozen") 
print(disabled) 
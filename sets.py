# Python program to demonstrate differences 
# between normal and frozen set 

# Same as {"yeuni", "john","Asha"} 
normal_set = set(["yeuni", "john","Asha"]) 

# Adding an element to normal set is fine 
normal_set.add("Angel") 

print("Normal Set") 
print(normal_set) 

# A frozen set 
frozen_set = frozenset(["Willian", "Kante", "Pedro"]) 

print("Frozen Set") 
print(frozen_set) 


#OUTPUTTTT
# Normal Set
#set(['yeuni', 'john', 'Asha', 'Angel'])
#Frozen Set
#frozenset(['Willian', 'Kante', 'Pedro'])

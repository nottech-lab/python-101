'''
Write a simple script that demonstrate your understanding of Modules'''

#creating modules and the file should be saved mymodule.py

mode = {
  "name": "Stephen",
  "age": 36,
  "country": "USA"
}
import mymodule

a = mymodule.mode["age"]
print(a)
from mymodule import mode
print (mode["country"])
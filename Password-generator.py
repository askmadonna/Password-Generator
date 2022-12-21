
#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
"""
n = 4
m = 2
o = 2
password1 = random.sample(letters, n)
password2 = random.sample(symbols, m)
password3 = random.sample(numbers, o)
print(str(password1) + str(password2) + str(password3))
"""


password = ""
for char in range(1, nr_letters +1):
    password += random.choice(letters)
  
for char in range(1, nr_symbols +1):
    password += random.choice(symbols)

for char in range(1, nr_numbers +1):
    password += random.choice(numbers)

#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
sr = ''.join(random.sample(password, len(password)))
print(sr)

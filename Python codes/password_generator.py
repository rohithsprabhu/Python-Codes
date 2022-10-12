# Program to generate a password.

import random
import string

print("Welcome to Password Generator\n")

# Get length of the password from the user

length = int(input("Enter the length of the password: "))

# Assigning different characters

letters = string.ascii_letters
numbers = string.digits
specials = "!@#$%&"

# Combining all different characters

all = letters + numbers + specials

# Shuffling all characters to get random password

temp_password = random.sample(all,length)
password = "".join(temp_password)

# Printing the password.

print("Your password is:",password)
input()




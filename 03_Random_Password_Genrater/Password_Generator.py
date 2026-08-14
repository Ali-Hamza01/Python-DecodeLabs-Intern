# Python Intern Project-03
# Random Password Generator

# importing the required modules
import random
import string

print("Welcome to the Random Password Generator")


letters = string.ascii_letters 
digits =string.digits
special_characters = "!@#$%&*"
characters = letters + digits + special_characters

# Ask the User to enter password length
length = int(input("Enter length of password: "))

if length < 8:
    print("Password must be 8 length or more and should contain atleast one special character and number")

else:
    password =[
        random.choice(letters),
        random.choice(digits),
        random.choice(special_characters)
    ]
    for i in range(length - 3):
        password.append(random.choice(characters))

    password = "".join(password)

    print("Your Random Password is:", password)

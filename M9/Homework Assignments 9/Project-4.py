import random

def generate_password(length):
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890_."
    password = ""
    for _ in range(length):
        password += random.choice(characters)
    return password

# The following code is getting the length from the user while making sure the user does not enter anything other than the length of password.
try:
    length = int(input("Enter the desired password length: "))
    if length <= 0:
        print("Password length must be a positive number.")
    else:
        password = generate_password(length)
        print("Generated Password:", password)
except ValueError:
    print("Invalid input. Please enter a number.")
import random

lst = list(range(1, 21))
chosen_number = random.choice(lst)

num = int(input("Enter the number you guessed: "))

while num != chosen_number:
    if num < chosen_number:
        print("Your guess is less than the chosen number. Try again!")
    elif num > chosen_number:
        print("Your guess is greater than the chosen number. Try again!")
    num = int(input("Enter the number you guessed: "))

print("Congratulations! You've guessed the number!")

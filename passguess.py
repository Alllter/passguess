# importing random
from random import *

# pass input
user_pass = input("Please enter your password ")

# alphabet pass guessing
password = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j','k', 
            'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't','u','v', 
            'w', 'x', 'y', 'z',]

# initialize empty string
guess = ""


# looping and generate many pass
# if does not match
while (guess != user_pass):
    guess = ""
    # generate random pass
    for letter in range(len(user_pass)):
        guess_letter = password[randint(0, 25)]
        guess = str(guess_letter) + str(guess)
    # print guessed pass
    print(guess)
    
# this will print the pass that is match.
print("I already guess it, Your password is",guess)
# this program demonstrates a guessing game


# generate a random number
from random import randint 

# 1.get user input
user_name = input("What is your name? ")
print("Hello there " + user_name + "!")


number = randint(10, 50)


# 2. Using a while loop, get the user number
counter = 0
while counter < 5:
    number = input(eval("Enter your guess: "))
    


# 3.generate a random number

# 4.using a while loop, check if the user input is equal to the generated number
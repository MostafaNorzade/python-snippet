#Write a programme where the computer randomly generates a number between 0 and 20. 
#The user needs to guess what the number is. If the user guesses wrong, tell them their guess is either too high, or too low. 
#This will get you started with the random library if you haven't already used it.

import random

original = random.randrange(1, 20)

 
guess = int(input("Please enter your guess: "))
 
if guess == original:
    print("Hit!")
elif guess < original:
    print("Your guess is too low")
else:
    print("Your guess is too high")
    
print("The No: ",original)

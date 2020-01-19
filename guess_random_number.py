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

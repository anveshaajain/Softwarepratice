import random

number = random.randint(1, 10)

print("Number Guessing Game")
print("Guess a number between 1 and 10")

guess = int(input("Enter your guess: "))

if guess == number:
    print("Correct! You won!")
else:
    print("Wrong! The number was", number)

print("Thank you for playing!")

import random

target_number = random.randint(1, 100) 

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
print("You have 5 chances to guess the correct number (default for medium).")

difficulty = input("Choose difficulty. 1. Easy (10 chances)  2. Medium (5 chances)  3. Hard (3 chances): ")

if difficulty == "1":
    print("You chose Easy difficulty.")
    chance = 10
elif difficulty == "2":
    print("You chose Medium difficulty.")
    chance = 5
elif difficulty == "3":
    print("You chose Hard difficulty.")
    chance = 3

attempts = 0

while chance > 0:
    attempts += 1
    guess = int(input("Guess the number"))
    if guess == target_number:
        print(f"That is the number! You guessed it in {attempts} attempt(s).")
        break
    elif guess > target_number:
        print("The number is smaller")
    else:
        print("The number is larger")
    chance -= 1 


if chance == 0:
    print(f"You lost. The correct number was {target_number}")

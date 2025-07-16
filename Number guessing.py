import random

numbers = [4, 8, 15, 16, 23, 42]

secret_number = random.choice(numbers)

print("Guess the number from this list:", numbers)

while True:
    guess = int(input("Enter your guess: "))
    
    if guess not in numbers:
        print("❌ That number is not in the list! Try again.")
    elif guess < secret_number:
        print("Too low!")
    elif guess > secret_number:
        print("Too high!")
    else:
        print("🎉 Correct! You guessed the number.")
        break
import random

print("=" * 40)
print("🎮 WELCOME TO NUMBER GUESSING GAME 🎮")
print("=" * 40)

while True:

    print("\nChoose Difficulty Level:")
    print("1. Easy   (1 - 50)")
    print("2. Medium (1 - 100)")
    print("3. Hard   (1 - 200)")

    choice = int(input("Enter your choice (1/2/3): "))

    if choice == 1:
        limit = 50
    elif choice == 2:
        limit = 100
    elif choice == 3:
        limit = 200
    else:
        print("Invalid Choice! Defaulting to Medium Level.")
        limit = 100

    number = random.randint(1, limit)
    attempts = 0

    print(f"\nI have selected a number between 1 and {limit}.")
    print("Try to guess it!")

    while True:
        guess = int(input("Guess the number : "))
        attempts += 1

        if guess > number:
            print("Too High! Try a lower number.")
        elif guess < number:
            print("Too Low! Try a higher number.")
        else:
            print("\n Congratulations!")
            print(f"You guessed the number {number} correctly.")
            print(f"Total Attempts: {attempts}")

            # Score Calculation
            score = max(100 - (attempts - 1) * 10, 10)
            print(f"Your Score: {score}")
            break

    play_again = input("\nDo you want to play again? (yes/no): ").lower()

    if play_again != "yes":
        print("\nThanks for playing! 👋")
        break
# Number Guessing Game
# Python 3.x

import random

def choose_difficulty():
    print("Choose difficulty:")
    print("  1) Easy   (range 1-20, 10 attempts)")
    print("  2) Medium (range 1-100, 7 attempts)  <-- recommended")
    print("  3) Hard   (range 1-500, 10 attempts)")
    print("  4) Unlimited (range 1-1000, unlimited attempts)")

    while True:
        choice = input("Select 1/2/3/4: ").strip()
        if choice == "1":
            return 1, 20, 10
        elif choice == "2":
            return 1, 100, 7
        elif choice == "3":
            return 1, 500, 10
        elif choice == "4":
            return 1, 1000, None  # None means unlimited
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")

def get_int(prompt, low, high):
    while True:
        try:
            val = int(input(prompt))
            if val < low or val > high:
                print(f"Please enter a number between {low} and {high}.")
                continue
            return val
        except ValueError:
            print("That's not a valid integer. Try again.")

def play_game():
    low, high, max_attempts = choose_difficulty()
    secret = random.randint(low, high)
    attempts = 0

    print(f"\nI've picked a number between {low} and {high}. Good luck!")
    if max_attempts:
        print(f"You have {max_attempts} attempts.\n")
    else:
        print("You have unlimited attempts. Try to be efficient!\n")

    while True:
        guess = get_int(f"Enter your guess ({low}-{high}): ", low, high)
        attempts += 1

        if guess == secret:
            print(f"🎉 Correct! You guessed the number in {attempts} attempt(s).")
            break

        # Give a helpful hint
        diff = abs(secret - guess)
        if guess < secret:
            direction = "higher"
        else:
            direction = "lower"

        # Granular hint based on closeness
        if diff == 1:
            closeness = "🔥 You're boiling hot!"
        elif diff <= 5:
            closeness = "Very warm."
        elif diff <= 15:
            closeness = "Warm."
        elif diff <= 40:
            closeness = "Cold."
        else:
            closeness = "❄️ Ice cold."

        print(f"Try {direction}! ({closeness})")

        # Check attempt limit (if any)
        if max_attempts and attempts >= max_attempts:
            print(f"\n😢 Out of attempts. The number was {secret}. Better luck next time!")
            break

    # Replay option
    while True:
        again = input("\nPlay again? (y/n): ").strip().lower()
        if again in ("y", "yes"):
            print("\n" + "-"*40 + "\n")
            return True
        elif again in ("n", "no"):
            print("Thanks for playing — bye! 👋")
            return False
        else:
            print("Please answer 'y' or 'n'.")

if __name__ == "__main__":
    print("=== Number Guessing Game ===")
    while play_game():
        pass

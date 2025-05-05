def reverse_guessing_game():
    print("Imagine a number between 1 and 100, and  try to guess it!")
    input("Press Enter when ready...")

    # Initial range
    low = 1
    high = 100
    attempts = 0

    # Loop until guess is correct or range is invalid
    while low <= high:
        guess = (low + high) // 2  # Computer guesses the middle of the range
        attempts += 1

        print(f"\nIs the number {guess}?")
        feedback = input("Type 'h' if high, 'l' if low, or 'c' if correct: ").strip().lower()

        if feedback == 'c':
            print(f"\n🎉 Yup! guessed the number in {attempts} attempts.")
            break
        elif feedback == 'h':
            high = guess - 1  # Narrow the range down
        elif feedback == 'l':
            low = guess + 1   # Narrow the range up
        else:
            print("Please enter only 'h', 'l', or 'c'.")

    else:
        # If the loop ends without a correct guess
        print("Hmm, are you sure about the number? I couldn't find the number!")

# Run the game
if __name__ == "__main__":
    reverse_guessing_game()

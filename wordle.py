import logic

def play():
    answer = logic.setAnswer()
    attempts = 6

    print("Welcome to Wordle!\nGuess the 5 letter word. You have 6 attempts.\n")

    for turn in range(attempts):
        guess = input(f"Attempt {turn+1}/{attempts}: ").lower().strip()

        while not logic.isValid(guess):
            print("\nInvalid word.\n")
            guess = input(f"Attempt {turn+1}/{attempts}: ").lower().strip()

        result = logic.getResult(guess, answer)
        print("Result:", result)

        if logic.isCorrect(guess, answer):
            print(f"\nCorrect!\nYou successfully solved the Wordle in {turn+1} guesses.\n")
            break

        elif (turn + 1 == attempts):
            print(f"\nIncorrect!\nThe correct answer was: {answer}\n")


if __name__ == "__main__":
    play()

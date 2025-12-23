from collections import Counter

# Read in possible answers
answers = set()
with open('wordle_answers.txt', 'r') as file:
    for line in file:
        answers.add(line.strip())

# Read in possible guesses (excludes answers)
guesses = set()
with open('wordle_guesses.txt', "r") as file:
    for line in file:
        guesses.add(line.strip())

# Randomly select an answer
def setAnswer():
    return next(iter(answers))

# Check if a guess is valid
def isValid(guess):
    if guess in guesses or guess in answers:
        return True
    else:
        return False

# Check if guess matches the answer  
def isCorrect(guess, answer):
    if guess == answer:
        return True
    else:
        return False

# Check for matching letters
# Return a list of 'grey' and 'green' assignments to letters  
def getGreens(guess, answer):
    colors = ['grey'] * 5

    for i in range(5):
        if guess[i] == answer[i]:
            colors[i] = 'green'

    return colors

# Helper function
# Return a list of unique characters in guess
def getUniqueChars(guess):
    seen = set()
    unique_chars = []

    for char in guess:
        if not char in seen:
            unique_chars.append(char)
        seen.add(char)

    return unique_chars

# Alter 'grey' and green' assignments to include 'yellow' letters
def getYellows(guess, answer, colors):
    unique_chars = getUniqueChars(guess)

    guess_counter = Counter(guess)
    answer_counter = Counter(answer)

    for char in unique_chars:
        if not char in answer_counter:
            continue
        
        guess_count = guess_counter.get(char)
        answer_count = answer_counter.get(char)
        
        if (guess_count <= answer_count):
            for i in range(5):
                if (guess[i] == char) and (answer[i] != char):
                    colors[i] = 'yellow'
       
        elif (guess_count > answer_count):
            num_matches = 0
            
            for i in range(5):
                if (guess[i] == char) and (answer[i] == char):
                    num_matches += 1
           
            if (num_matches == answer_count):
                continue

            num_yellows = answer_count - num_matches

            for i in range(5):
                if (guess[i] == char) and (answer[i] != char) and (num_yellows > 0):
                    colors[i] = 'yellow'
                    num_yellows -= 1

# Determine the result for a given guess and answer
# Return string of color assignments in the correct order
def getResult(guess, answer):
    colors = getGreens(guess, answer)
    getYellows(guess, answer, colors)

    result = ""

    for i in range(5):
        if (colors[i] == 'grey'):
            result += '⬛'
        elif (colors[i] == 'green'):
            result += '🟩'
        elif (colors[i] == 'yellow'):
            result += '🟨'

    return result


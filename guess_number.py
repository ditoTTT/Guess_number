import random
from guess_art import logo

number = (random.randint(1, 100))
print(f"{logo}\nWelcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.\nPsst, the correct answer is {number}")
question = input('Choose difficult "easy" or "hard" ')
level_dict = {'easy': 10, 'hard': 5}

def difficulty():
    if question in level_dict:
        return level_dict[question]
difficulty_level = difficulty()

while difficulty_level > 0:
    def guessnum():
        global difficulty_level
        chosen_number = int(input(f"You have {difficulty_level} attempts remaining to guess the number\nMake a guess:"))
        if chosen_number == number:
            print(f'You got it! The answer was {number}.')
            difficulty_level = -1
        elif chosen_number > number:
            print('Too high.\nGuess again.')
            difficulty_level -= 1
        elif chosen_number < number:
            print('Too low.\nGuess again.')
            difficulty_level -= 1
    guessnum()
    if difficulty_level == 0 :
        print("You've run out of guesses, you lose.")
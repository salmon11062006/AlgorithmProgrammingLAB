import random

def intro():
    print("Welcome to my number guessing game!")

def scoring(name, attempts):
    with open('score.txt', 'a') as file:
        file.write(f'{name}: {attempts} attempts\n')

def game():
    intro()
    name = input("Your name: ")
    replay = True
    
    while replay:
        randomNumber = random.randint(1,101)
        attempts = 0
        correctGuess = False
        guesses = int(input("Enter your guess: "))
        while not correctGuess:
            if guesses < randomNumber:
                print('The number is higher')
                guesses = int(input('Try again: '))
                attempts += 1

            elif guesses > randomNumber:
                print('The number is lower')
                guesses = int(input('Try again: '))
                attempts += 1

            elif guesses == randomNumber:
                print('Yay! You are correct! Here have a cake! 🎂')
                scoring(name, attempts)
                correctGuess = True

        play_again = input("Play again? (Y/N): ")
        if play_again != 'Y':
            replay = False
game()
import random
randomNumber = random.randint(1,101)
correctGuess = 0    
guesses = int(input('Guess the secret number: '))
while correctGuess == 0:

    if guesses < randomNumber:
        print('The number is higher')
        guesses = int(input('Try again: '))
    elif guesses > randomNumber:
        print('The number is lower')
        guesses = int(input('Try again: '))
    elif guesses == randomNumber:
        print('Yay! You are correct! Here have a cake! 🎂')
        break
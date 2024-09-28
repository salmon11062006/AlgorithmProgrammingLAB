import random
randomNumber = random.randint(1,101)
guesses = int(input('Guess the secret number: '))
while True:

    if guesses < randomNumber:
        print('The number is higher')
        guesses = int(input('Try again: '))
    elif guesses > randomNumber:
        print('The number is lower')
        guesses = int(input('Try again: '))
    elif guesses == randomNumber:
        print('Yay! You are correct! Here have a cake! 🎂')
        break
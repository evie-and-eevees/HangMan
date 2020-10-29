import random
E = ('able', 'carpenter', 'damage', 'forever', 'helmet', 'mountain', 'record', 'total')
M = ('activity', 'calendar', 'currency', 'famous', 'industry', 'mention', 'picture', 'reduce', 'televise', 'wrist')
H= ['achieve', 'calculator', 'exasperating', 'leather', 'propel', 'territory']
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
bank = input('Welcome to Hangman! Please enter [E]asy, [M]edium, or [H]ard for difficulty: ')
difficulties = ['E','M','H']
bank = bank.capitalize()
while bank not in difficulties:
    bank = input('Please enter the capital letter E, M, or H: ')
if bank == 'E':
    bank = E
if bank == 'H':
    bank = H
if bank == 'M':
    bank = M
word = bank[random.randint(0,len(bank))]
word = "".join(word)
word = list(word)
length = len(word)
answers = []
guesses = []
for x in range(0, length):
    answers.append('_')
r = 5
print(' '.join(answers))
while r != 0:
    guess = input(f'{r} Guesses remain. Guess a letter: ')
    while guess not in alphabet:
        guess = input('Please enter only lower case letters: ')
    while guess in guesses:
        guess = input('Letter already guessed. Guess again: ')
    guesses.append(guess)
    if guess in word:
        while guess in word:
            index = word.index(guess)
            answers[index] = guess
            word[index] = '_'
        if '_' not in answers:
            exit(f"{' '.join(answers)} You win!")
        print(f"{' '.join(answers)} Good job!")
    elif guess not in word:
        r = r - 1
        print(f"{' '.join(answers)} Good try.")
if r == 0:
    finish = input('0 guesses remaining. You lose! Would you like to keep guess? [y/n] ')
options = ['y','n']
while finish not in options:
    finish = input('Please enter the lower case letter y or n: ')
while finish == 'y':
    while '_' in answers:
        guess = input(f'{r} Guesses remain. Guess a letter: ')
        while guess not in alphabet:
            guess = input('Please enter only lower case letters: ')
        while guess in guesses:
            guess = input('Letter already guessed. Guess again: ')
        guesses.append(guess)
        if guess in word:
            while guess in word:
                index = word.index(guess)
                answers[index] = guess
                word[index] = '_'
            if '_' not in answers:
                exit(f"{' '.join(answers)} Game over.")
            print(f"{' '.join(answers)} Good job!")
        elif guess not in word:
            print(f"{' '.join(answers)} Good try.")
if finish == 'n':
    print('Game over.')

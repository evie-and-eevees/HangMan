import random
E = [['a','b','l','e'], ['c','a','r','p','e','n','t','e','r'], ['d','a','m','a','g','e'], ['f','o','r','e','v','e','r'],
        ['h','e','l','m','e','t'], ['m','o','u','n','t','a','i','n'], ['r','e','c','o','r','d'], ['t','o','t','a','l']]
M = [['a', 'c', 't', 'i', 'v', 'i', 't', 'y'], ['c','a','l','e','n','d','a','r'], ['c','u','r','r','e','n','c','y'],
        ['f','a','m','o','u','s'], ['i','n','d','u','s','t','r','y'], ['m','e','n','t','i','o','n'], ['p','i','c','t','u','r','e'],
        ['r','e','d','u','c','e'], ['t','e','l','e','v','i','s','e'], ['w','r','i','s','t']]
H= [['a','c','h','i','e','v','e'], ['c','a','l','c','u','l','a','t','o','r'], ['e','x','a','s','p','e','r','a','t','i','n','g'],
        ['l','e','a','t','h','e','r'], ['p','r','o','p','e','l'], ['t','e','r','r','i','t','o','r','y']]
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
word = bank[random.randrange(0, len(bank), 1)]
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

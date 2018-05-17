import random
import string

WORDLIST_FILENAME = "palavras.txt"

def loadwords():
    """
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    infile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = infile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return random.choice(wordlist)


def iswordguessed(secretword, lettersguessed):
    secretletters = []

#    for letter in secretWord:
#        if letter in secretLetters:
#            secretLetters.append(letter)
#        else:
#            pass

    for letter in secretword:
        if letter in lettersguessed:
            pass
        else:
            return False

    return True

def getguessedword():

    guessed = ''


    return guessed

def getavailableletters():
    # 'abcdefghijklmnopqrstuvwxyz'
    available = string.ascii_lowercase


    return available

def hangman(secretword):

    guesses = 8
    lettersguessed = []
    print 'Welcome to the game, Hangam!'
    print 'I am thinking of a word that is', len(secretword), ' letters long.'
    print '-------------'

    while  iswordguessed(secretword, lettersguessed) == False and guesses >0:
        print 'You have ', guesses, 'guesses left.'

        available = getavailableletters()
        for letter in available:
            if letter in lettersguessed:
                available = available.replace(letter, '')

        print 'Available letters', available
        letter = raw_input('Please guess a letter: ')
        if letter in lettersguessed:

            guessed = getguessedword()
            for letter in secretword:
                if letter in lettersguessed:
                    guessed += letter
                else:
                    guessed += '_ '

            print 'Oops! You have already guessed that letter: ', guessed
        elif letter in secretword:
            lettersguessed.append(letter)

            guessed = getguessedword()
            for letter in secretword:
                if letter in lettersguessed:
                    guessed += letter
                else:
                    guessed += '_ '

            print 'Good Guess: ', guessed
        else:
            guesses -= 1
            lettersguessed.append(letter)

            guessed = getguessedword()
            for letter in secretword:
                if letter in lettersguessed:
                    guessed += letter
                else:
                    guessed += '_ '

            print 'Oops! That letter is not in my word: ', guessed
        print '------------'

    else:
        if iswordguessed(secretword, lettersguessed) == True:
            print 'Congratulations, you won!'
        else:
            print 'Sorry, you ran out of guesses. The word was ', secretword, '.'




secretword = loadwords().lower()
hangman(secretword)

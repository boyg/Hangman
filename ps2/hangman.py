# -----------------------------------
# The following helper code is taken from problem set 2 of MIT 6.0001
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# Load the list of words into the variable wordlist so that it can be accessed from anywhere in the program
wordlist = load_words()
# End of helper code
# -----------------------------------

def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    my_secret_word = secret_word # We will be stripping the string, so use a copy instead

    for char in my_secret_word:
        if char not in letters_guessed and char != ' ':
            return False
        my_secret_word = my_secret_word.replace(char, "")

    return True

def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    progress = secret_word

    for char in secret_word:
        if char not in letters_guessed and char != ' ':
            progress = progress.replace(char, '_ ')

    return progress

def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    letters_not_guessed = ""

    # Use ascii values to iterate over alphabet:
    # https://terrameijar.wordpress.com/2017/02/03/python-how-to-generate-a-list-of-letters-in-the-alphabet/
    for ascii in range(ord('a'), ord('z') + 1):
        letter = chr(ascii)
        if letter not in letters_guessed:
            letters_not_guessed += letter

    return letters_not_guessed

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    '''
    letters_guessed = []
    guesses_remaining = 6
    warnings_remaining = 3

    print('Welcome to the game Hangman!')
    print('I am thinking of a word that is', len(secret_word), 'letters long.')
    print('You have', warnings_remaining, 'warnings left.')
    print('-------------')

    while True:
        print('You have', guesses_remaining, 'guesses left.')
        print('Available letters:', get_available_letters(letters_guessed))
        guess = input('Please guess a letter:').lower()

        if not guess.isalpha():
            if warnings_remaining == 0:
                guesses_remaining -= 1
                print('Oops! That is not a valid letter. You have no warnings left so you lose one guess:', get_guessed_word(secret_word, letters_guessed))
            else:
                warnings_remaining -= 1
                print('Oops! That is not a valid letter. You have', warnings_remaining, 'warnings left:', get_guessed_word(secret_word, letters_guessed))
        elif guess in letters_guessed:
            if warnings_remaining == 0:
                guesses_remaining -=1
                print('Oops! You\'ve already guessed that letter. You have no warnings left so you lose one guess:', get_guessed_word(secret_word, letters_guessed))
            else:
                warnings_remaining -= 1
                print('Oops! You\'ve already guessed that letter. You have', warnings_remaining, 'warnings left :', get_guessed_word(secret_word, letters_guessed))
        elif guess in secret_word:
            letters_guessed.append(guess)
            print('Good guess:', get_guessed_word(secret_word, letters_guessed))
        else:
            if guess in ['a', 'e', 'i', 'o', 'u']:
                guesses_remaining -= 2
            else:
                guesses_remaining -= 1
            letters_guessed.append(guess)
            print('Oops! That letter is not in my word:', get_guessed_word(secret_word, letters_guessed))
        
        print('------------')

        if is_word_guessed(secret_word, letters_guessed):
            score = guesses_remaining * len(set(secret_word)) # guesses_remaining * number unique letters in secret_word
            print('Congratulations, you won!')
            print('Your total score for this game is:', score)
            break
        elif guesses_remaining <= 0:
            print('Sorry, you ran out of guesses. The word was', secret_word + '.')
            break

def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    word = my_word.replace(' ', '')
    if len(word) != len(other_word):
        return False

    already_revealed = set()

    for i in range(0, len(word)):
        # False case 1: letter is not hidden, and they don't match. False
        if word[i] != '_' and word[i] != other_word[i]:
            return False

        # False case 2: letter is not hidden, but was supposed to be in a previous underscore. False
        if word[i] == other_word[i] and other_word[i] in already_revealed:
            return False

        # Update already_revealed set
        if word[i] == '_' and other_word[i] not in already_revealed:
            already_revealed.add(other_word[i])

    return True

def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    found_one = None
    
    for word in wordlist:
        if match_with_gaps(my_word, word):
            print(word, end=' ')
            found_one = True
    print('\n')

    if not found_one:
        print('No matches found')

def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    letters_guessed = []
    guesses_remaining = 6
    warnings_remaining = 3

    print('Welcome to the game Hangman!')
    print('I am thinking of a word that is', len(secret_word), 'letters long.')
    print('You have', warnings_remaining, 'warnings left.')
    print('-------------')

    while True:
        print('You have', guesses_remaining, 'guesses left.')
        print('Available letters:', get_available_letters(letters_guessed))
        guess = input('Please guess a letter:').lower()

        if guess == '*':
            print('Possible word matches are:')
            show_possible_matches(get_guessed_word(secret_word, letters_guessed))

        elif not guess.isalpha():
            if warnings_remaining == 0:
                guesses_remaining -= 1
                print('Oops! That is not a valid letter. You have no warnings left so you lose one guess:', get_guessed_word(secret_word, letters_guessed))
            else:
                warnings_remaining -= 1
                print('Oops! That is not a valid letter. You have', warnings_remaining, 'warnings left:', get_guessed_word(secret_word, letters_guessed))
        elif guess in letters_guessed:
            if warnings_remaining == 0:
                guesses_remaining -=1
                print('Oops! You\'ve already guessed that letter. You have no warnings left so you lose one guess:', get_guessed_word(secret_word, letters_guessed))
            else:
                warnings_remaining -= 1
                print('Oops! You\'ve already guessed that letter. You have', warnings_remaining, 'warnings left :', get_guessed_word(secret_word, letters_guessed))
        elif guess in secret_word:
            letters_guessed.append(guess)
            print('Good guess:', get_guessed_word(secret_word, letters_guessed))
        else:
            if guess in ['a', 'e', 'i', 'o', 'u']:
                guesses_remaining -= 2
            else:
                guesses_remaining -= 1
            letters_guessed.append(guess)
            print('Oops! That letter is not in my word:', get_guessed_word(secret_word, letters_guessed))
        
        print('------------')

        if is_word_guessed(secret_word, letters_guessed):
            score = guesses_remaining * len(set(secret_word)) # guesses_remaining * number unique letters in secret_word
            print('Congratulations, you won!')
            print('Your total score for this game is:', score)
            break
        elif guesses_remaining <= 0:
            print('Sorry, you ran out of guesses. The word was', secret_word + '.')
            break

if __name__ == "__main__":
    
    secret_word = choose_word(wordlist)

    # Uncomment one of the two following lines below
    # Depending on whether or not you want to play with hints
    #hangman(secret_word)
    hangman_with_hints(secret_word)

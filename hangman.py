# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import re
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


# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    if get_guessed_word(secret_word, letters_guessed) == secret_word:
        return True
    else:
        return False


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    letters_string = ''
    for i in secret_word:
        if i in letters_guessed:
            letters_string += i
        else:
            letters_string += '_ '
    return letters_string


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    letters_available = list(string.ascii_lowercase)
    for i in letters_guessed:
        if i in letters_available:
            letters_available.remove(i)
    letters_available_string = ''
    for i in letters_available:
        letters_available_string += i
    return letters_available_string


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
    
    Follows the other limitations detailed in the problem write-up.
    '''
    print(secret_word)
    guesses_left = 6
    warnings = 0
    letters_guessed = ''
    print('Welcome to game Hangman!')
    print(f"I'm thinking of a word that is {len(secret_word)} letters long")
    print('-' * 10)
    print(f'You have {guesses_left} guesses left.\nAvailable letters: {get_available_letters(letters_guessed)}')
    letter = str(input('Please guess a letter: ')).lower()

    if letter not in string.ascii_lowercase:
        warnings += 1
        print(f'Only letters can be written in my word.\nYou have {warnings} warning! If you will have {3 - warnings} '
              f'more, you will loose one guess!')
        letter = str(input('Please guess a letter: ')).lower()
    if len(letter) > 1:
        warnings += 1
        print(
            f'Only one letter can be entered in one guess.\nYou have {warnings} warning! If you will have {3 - warnings} '
            f'more, you will loose one guess!')
        letter = str(input('Please guess a letter: ')).lower()
        while letter not in string.ascii_lowercase or len(letter) > 1:
            warnings += 1
            print(f'You have {warnings} warning! If you will have {3 - warnings} more, you will loose one guess!')
            letter = str(input('Please guess a letter: ')).lower()
            if warnings == 3:
                guesses_left -= 1
                warnings = 0
                print("You've lost one guess because of too many warnings.")

    while not is_word_guessed(secret_word, letters_guessed):
        if letter in secret_word:
            letters_guessed += letter
            print(f'Good guess: {get_guessed_word(secret_word, letters_guessed)}')
            is_word_guessed(secret_word, letters_guessed)
            if is_word_guessed(secret_word, letters_guessed):
                break
            letter = str(input('Please guess a letter: ')).lower()
            print(
                f'You have {guesses_left} guesses left.\nAvailable letters: {get_available_letters(letters_guessed)}')
        else:
            if letter not in ['a', 'e', 'i', 'o']:
                guesses_left -= 1
            else:
                guesses_left -= 2
            if guesses_left == 0:
                break
            print(f"Oops! The letter is not in my word: {get_guessed_word(secret_word, letters_guessed)}")
            print(
                f'You have {guesses_left} guesses left.\nAvailable letters: {get_available_letters(letters_guessed)}')
            letter = str(input('Please guess a letter: ')).lower()

    if guesses_left == 0:
        print(f'You have lost! My secret word: {secret_word}')
    if is_word_guessed(secret_word, letters_guessed):
        print(
            f'You have won! Your score: {guesses_left * len([i for i in secret_word if list(secret_word).count(i) == 1])}')


# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
# (hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------

regex = r''
def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    global regex
    my_word = my_word.replace(' ', '')
    regex = fr"{my_word.replace('_', '[a-z]')}"
    # for i in my_word:
    #     if i != '_':
    #         regex += f'[{i}]'
    #     else:
    #         regex += r'[a-z]'
    #
    if other_word in list(re.findall(regex, str(wordlist))):
        return True
    else:
        return False


def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    global regex
    regex = fr"{my_word.replace('_', '[a-z]')}"
    all_matches = []
    for i in wordlist:
        if match_with_gaps(my_word, i):
            all_matches.append(i)

    if not all_matches:
        return 'No matches found'

    all_matches_str = ''
    for i in all_matches:
        all_matches_str += f'{i}, '
    return all_matches_str

print(show_possible_matches('t_ _ t'))


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
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    print(secret_word)
    guesses_left = 6
    warnings = 0
    letters_guessed = ''
    print('Welcome to game Hangman!')
    print(f"I'm thinking of a word that is {len(secret_word)} letters long")
    print('-' * 10)
    print(f'You have {guesses_left} guesses left.\nAvailable letters: {get_available_letters(letters_guessed)}')
    letter = str(input('Please guess a letter: ')).lower()

    if letter == '*':
        if get_guessed_word(secret_word, letters_guessed) == f"{'_ ' * len(secret_word)}":
            print('You must make at least one guess before asking for a hint.')
            letter = str(input('Please guess a letter: ')).lower()
        else:
            show_possible_matches(get_guessed_word(secret_word, letters_guessed))
    elif letter not in string.ascii_lowercase:
        warnings += 1
        print(f'Only letters can be written in my word.\nYou have {warnings} warning! If you will have {3 - warnings} '
              f'more, you will loose one guess!')
        letter = str(input('Please guess a letter: ')).lower()
    if len(letter) > 1:
        warnings += 1
        print(
            f'Only one letter can be entered in one guess.\nYou have {warnings} warning! If you will have {3 - warnings} '
            f'more, you will loose one guess!')
        letter = str(input('Please guess a letter: ')).lower()
        while letter not in string.ascii_lowercase or len(letter) > 1 or letter == '*':
            warnings += 1
            print(f'You have {warnings} warning! If you will have {3 - warnings} more, you will loose one guess!')
            letter = str(input('Please guess a letter: ')).lower()
            if warnings == 3:
                guesses_left -= 1
                warnings = 0
                print("You've lost one guess because of too many warnings.")

    while not is_word_guessed(secret_word, letters_guessed):
        if letter in secret_word:
            letters_guessed += letter
            print(f'Good guess: {get_guessed_word(secret_word, letters_guessed)}')
            is_word_guessed(secret_word, letters_guessed)
            if is_word_guessed(secret_word, letters_guessed):
                break
            letter = str(input('Please guess a letter: ')).lower()
            print(
                f'You have {guesses_left} guesses left.\nAvailable letters: {get_available_letters(letters_guessed)}')
        else:
            if letter not in ['a', 'e', 'i', 'o']:
                guesses_left -= 1
            else:
                guesses_left -= 2
            if guesses_left == 0:
                break
            print(f"Oops! The letter is not in my word: {get_guessed_word(secret_word, letters_guessed)}")
            print(
                f'You have {guesses_left} guesses left.\nAvailable letters: {get_available_letters(letters_guessed)}')
            letter = str(input('Please guess a letter: ')).lower()

    if guesses_left == 0:
        print(f'You have lost! My secret word: {secret_word}')
    if is_word_guessed(secret_word, letters_guessed):
        print(
            f'You have won! Your score: {guesses_left * len([i for i in secret_word if list(secret_word).count(i) == 1])}')

# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


# if __name__ == "__main__":
# pass

# To test part 2, comment out the pass line above and
# uncomment the following two lines.

# secret_word = choose_word(wordlist)
# hangman(secret_word)

###############

# To test part 3 re-comment out the above lines and
# uncomment the following two lines.

# secret_word = choose_word(wordlist)
# hangman_with_hints(secret_word)

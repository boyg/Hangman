import string
import unittest
import collections

WORDLIST_FILENAME = 'words.txt'
VOWELS_LOWER = 'aeiou'
VOWELS_UPPER = 'AEIOU'
CONSONANTS_LOWER = 'bcdfghjklmnpqrstvwxyz'
CONSONANTS_UPPER = 'BCDFGHJKLMNPQRSTVWXYZ'
alpha_len = len(string.ascii_lowercase)

### HELPER CODE ###
def load_words(file_name):
    '''
    file_name (string): the name of the file containing 
    the list of words to load    
    
    Returns: a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    print("Loading word list from file...")
    inFile = open(file_name, 'r')
    wordlist = []
    for line in inFile:
        wordlist.extend([word.lower() for word in line.split(' ')])
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.
    
    Returns: True if word is in word_list, False otherwise

    Example:
    >>> is_word(word_list, 'bat') returns
    True
    >>> is_word(word_list, 'asdf') returns
    False
    '''
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list

def get_story_string():
    """
    Returns: a story in encrypted text.
    """
    f = open("story.txt", "r")
    story = str(f.read())
    f.close()
    return story
### END OF HELPER CODE ###

def number_of_valid_words(word_list, text):
	count = 0
	for word in text.split():
		if is_word(word_list, word):
			count += 1
	return count

def insert_letter_everywhere(letter, word):
    '''
    Returns a list containing all possible ways of 
    inserting letter into word

    letter: char
    word: string
    returns: list

    Example:
    >>> insert_letter_everywhere('a', 'bc')
    ['abc', 'bac', 'bca']
    '''
    insertions = []

    for i in range(len(word)+1):
        insertions.append(word[:i] + letter + word[i:])

    return insertions

def get_permutations(sequence):
    '''
    Returns a list containing all permutations of sequence

    sequence: string
    returns: list

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
    '''
    if len(sequence) == 1:
        return sequence

    else:
        permutations = []
        sub_sequence = get_permutations(sequence[1:])
        for permutation in sub_sequence:
            permutations += insert_letter_everywhere(sequence[0], permutation)

    return permutations

class get_permutations_tests(unittest.TestCase):

    def test_foo(self):
        foo_result = ['foo', 'foo', 'ofo', 'ofo', 'oof', 'oof']
        self.assertEqual( collections.Counter(get_permutations('foo')), collections.Counter(foo_result) )

    def test_bar(self):
        bar_result = ['bar', 'bra', 'abr', 'arb', 'rba', 'rab']
        self.assertEqual( collections.Counter(get_permutations('bar')), collections.Counter(bar_result) )

    def test_abc(self):
        abc_result = ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
        self.assertEqual( collections.Counter(get_permutations('abc')), collections.Counter(abc_result) )

if __name__ == '__main__':
    unittest.main()
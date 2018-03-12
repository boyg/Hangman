from utils import *

class SubMessage(object):
    def __init__(self, text):
        '''
        Initializes a SubMessage object
                
        text (string): the message's text

        A SubMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)
    
    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class
        
        Returns: self.message_text
        '''
        return self.message_text

    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class.
        This helps you avoid accidentally mutating class attributes.
        
        Returns: a COPY of self.valid_words
        '''
        return self.valid_words[:]
                
    def build_transpose_dict(self, vowels_permutation):
        '''
        vowels_permutation (string): a string containing a permutation of vowels (a, e, i, o, u)
        
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to an
        uppercase and lowercase letter, respectively. Vowels are shuffled 
        according to vowels_permutation. The first letter in vowels_permutation 
        corresponds to a, the second to e, and so on in the order a, e, i, o, u.
        The consonants remain the same. The dictionary should have 52 
        keys of all the uppercase letters and all the lowercase letters.

        Example: When input "eaiuo":
        Mapping is a->e, e->a, i->i, o->u, u->o
        and "Hello World!" maps to "Hallu Wurld!"

        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
        '''
        transpose_dict = {}

        i = 0
        for letter in vowels_permutation:
            transpose_dict[VOWELS_LOWER[i]] = letter.lower()
            transpose_dict[VOWELS_UPPER[i]] = letter.upper()
            i += 1

        for letter in CONSONANTS_LOWER:
            transpose_dict[letter] = letter
            transpose_dict[letter.upper()] = letter.upper()

        return transpose_dict
    
    def apply_transpose(self, transpose_dict):
        '''
        transpose_dict (dict): a transpose dictionary
        
        Returns: an encrypted version of the message text, based 
        on the dictionary
        '''
        return ''.join([transpose_dict[char] if char in transpose_dict else char for char in self.get_message_text()])
     
class EncryptedSubMessage(SubMessage):
    def __init__(self, text):
        '''
        Initializes an EncryptedSubMessage object

        text (string): the encrypted message text

        An EncryptedSubMessage object inherits from SubMessage and has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        super().__init__(text)

    def decrypt_message(self):
        '''
        Attempt to decrypt the encrypted message 
        
        Idea is to go through each permutation of the vowels and test it
        on the encrypted message. For each permutation, check how many
        words in the decrypted text are valid English words, and return
        the decrypted message with the most English words.
        
        If no good permutations are found (i.e. no permutations result in 
        at least 1 valid word), return the original string. If there are
        multiple permutations that yield the maximum number of words, return any
        one of them.

        Returns: the best decrypted message    
        
        Hint: use your function from Part 4A
        '''
        best_decryption = super().get_message_text()
        best_score = number_of_valid_words(super().get_valid_words(), best_decryption)

        for permutation in get_permutations(VOWELS_LOWER):
            transpose_dict = super().build_transpose_dict(permutation)
            decryption = super().apply_transpose(transpose_dict)
            score = number_of_valid_words(super().get_valid_words(), decryption)

            if score > best_score:
                best_decryption = decryption
                best_score = score

        return best_decryption

class Sub_tests(unittest.TestCase):

    def __init__(self):
        self.message = SubMessage("Hello World!")
        self.permutation = "eaiuo"
        self.enc_dict = message.build_transpose_dict(permutation)
        self.enc_message = EncryptedSubMessage(message.apply_transpose(enc_dict))

    def SubMessage_test(self):
        self.assertEqual('Hallu Wurld!', self.message.apply_transpose(enc_dict))

    def EncryptedSubMessage_test(self):
        self.assertEqual('Hello World!', self.enc_message.decrypt_message())

if __name__ == '__main__':
    unittest.main()
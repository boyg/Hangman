# Hangman
The objective of the game is to gain as many points as possible across all hands.
## Dealing
- The player is dealt a hand of `HAND_SIZE` letters of the alphabet, chosen at random. This may include multiple instances of a particular letter
- The player arranges the hand into as many words as they want out of the letters, but using each letter at most once
- Some letters may remain unused, though the size of the hand when a word is played does affect its score
## Scoring
- The score for the hand is the sum of the score for each word formed
- The score for a word is the product of:
-- The sum of the points for letters in the word
-- The max of 7 * `word_length` - 3 * (`n` - `word_length`) and 1

## Credits
This project was inspired by problem set 3 of [MIT 6.0001](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/). Functions `load_words`, `choose_word`, and `is_word_guessed`, as well as the function docstrings were taken from the skeleton code supplied. The rest of the code was written independently by me.
## Example
```
Loading word list from file...
55900 words loaded.
Welcome to the game Hangman!
I am thinking of a word that is 5 letters long.
--------
You have 6 guesses left.
Available letters: abcdefghijklmnopqrstuvwxyz
Please guess a letter: a
Good guess: a_ _ _ _
--------
You have 6 guesses left.
Available letters: bcdefghijklmnopqrstuvwxyz
Please guess a letter: l
Good guess: a_ _ l_
--------
You have 6 guesses left.
Available letters: bcdefghijkmnopqrstuvwxyz
Please guess a letter: *
Possible word matches are:
addle adult agile aisle amble ample amply amyls angle ankle apple apply aptly arils atilt
--------
You have 6 guesses left.
Available letters: bcdefghijkmnopqrstuvwxyz
Please guess a letter: e
Good guess: a_ _ le
--------
```

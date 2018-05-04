# Hangman
The objective of the game is to gain as many points as possible across all hands.
## Dealing
- The player is dealt a hand of `HAND_SIZE` letters of the alphabet, chosen at random. This may include multiple instances of a particular letter
- The player arranges the hand into as many words as they want out of the letters, but using each letter at most once
- Some letters may remain unused, though the size of the hand when a word is played does affect its score
## Scoring
- The score for the hand is the sum of the score for each word formed
- The score for a word is the product of:
  - The sum of the points for letters in the word
  - The max of 7 × `word_length` − 3 × (`n` - `word_length`) and 1, where:
    - `word_length` is the number of letters used in the word
    - `n` is the number of letters available in the current hand
## Wildcards
Each hand dealt contains exactly one wildcard as one of its letters, denoted by an asterisk (*). Wildcards can only replace vowels. The player does not receive any points for using the wildcard (unlike all the other letters), though it does count as a used or unused letter when scoring.

## Credits
This project was inspired by problem set 3 of [MIT 6.0001](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/). Functions `load_words` and `get_frequency_dict`, as well as the function docstrings were taken from the skeleton code supplied. The rest of the code was written independently by me.

## Example
```
Enter total number of hands: 2
Current hand: a c i * p r t
Would you like to substitute a letter? no
Current hand: a c i * p r t
Please enter a word or '!!' to indicate you are done: part
"part" earned 114 points. Total: 114 points
Current hand: c i *
Please enter a word or '!!' to indicate you are done: ic*
"ic*" earned 84 points. Total: 198 points
Ran out of letters
Total score for this hand: 198
----------
Would you like to replay the hand? no
Current hand: d d * l o u t
Would you like to substitute a letter? yes
Which letter would you like to replace: l
Current hand: d d * a o u t
Please enter a word or '!!' to indicate you are done: out
"out" earned 27 points. Total: 27 points
Current hand: d d * a
Please enter a word or '!!' to indicate you are done: !!
Total score for this hand: 27
----------
Would you like to replay the hand? yes
Current hand: d d * a o u t
Please enter a word or '!!' to indicate you are done: d*d
"d*d" earned 36 points. Total: 36 points
Current hand: a o u t
Please enter a word or '!!' to indicate you are done: out
9
"out" earned 54 points. Total: 90 points
Current hand: a
Please enter a word or '!!' to indicate you are done: !!
Total score for this hand: 90
----------
Total score over all hands: 288
```

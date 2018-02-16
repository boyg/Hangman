# Hangman
The objective of the game is to guess all of the letters of the secret word correctly before running out of guesses. The user may choose to play with or without hints by commenting out the appropriate code in the main of `hangman.py`.
## Rules
- If the user is playing with hints, they may enter an asterisk `*` to see possible answers based on what they have guessed correctly so far.
- If user inputs a character not in the alphabet or a letter already guessed, they lose a warning.
- If user has no warnings left, they lose a guess.
- If the user inputs a consonant not in the word, they lose 1 guess.
- If the user inputs a vowel not in the word, they lose 2 guesses.
- If they win, their total score is the number of guesses remaining multiplied by the number of unique letters in the word.
## Credits
This project was inspired by problem set 2 of [MIT 6.0001](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/). Functions `load_words`, `choose_word`, and `is_word_guessed`, as well as the function docstrings were taken from the skeleton code supplied. The rest of the code was written independently by me.
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

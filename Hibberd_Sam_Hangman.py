import os
import random
    
# Open Text Document containing Hangman words (Directory will need changing dependent on user)

file = open('words_list.txt', 'r')

# Pull words form document

document_list = file.readlines()
document_list = [string.replace('\n','') for string in document_list]
     
# Produce list length (Number of words)

len_document_list = len(document_list)

# Select random word from list

select_word = random.randint(0,len_document_list-1)

hangman_word_string = document_list[select_word].lower()

hangman_word_list = list(hangman_word_string)

# Create user display
hangman_word_display_digits = len(hangman_word_list)
hangman_guess_display = '*'*hangman_word_display_digits
hangman_guess_display_list = list(hangman_guess_display)

# PLay the game
attempts = 7 
while (attempts > 0 and '*' in hangman_guess_display_list):
    
    # Ask to choose a string (must be exact)
    
    letter_guess = str(input('\nPlease enter your next guess: ')).lower()
    
    # loop for incorrect guesses
    if letter_guess not in hangman_word_list:
        attempts -= 1
        if attempts>0:
            print (f'\nYou have {attempts} remaining')
        else:
            print ('\nYou lose')
            print (f'\nThe word was {hangman_word_string}')
            
    else: # For correct guess and letter replacement
        for i in range(len(hangman_word_list)):
            if hangman_word_list[i]==letter_guess:
                hangman_guess_display_list[i] = letter_guess
                
    print (' '.join(hangman_guess_display_list))
    
if "*" not in hangman_guess_display_list:
    print('\nCongratulations you win')

import random

from list import word_list 
from art import hangman

print("Welcome to the Hangman Game!")
word = random.choice(word_list) #Random choose a word from the word_list
blank = ""
print(word)

#Replace all the letters in the word with a blank
word_length = len(word)
for space in range(word_length):
    blank += "_"
print(blank)

#Use a while loop to let the user guess again
game_over = False
result = []
lives = 6

while not game_over:
    #Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
    guess = input("Guess a letter: ").lower()
    display = ""
    
    #Check if the letter the user guessed (guess) is one of the letters then replace the letter in right position if it is right
    for letter in word:
        if guess == letter:
            display += letter
            result.append(letter)
        elif letter in result:
            display += letter
        else:
            display += "_"
    print(display)
    
    #remind the letter player had guessed right
    if guess in result:
        print(f"You've already guessed {guess}")
    
    #reduce live if player guess wrong
    if guess not in word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life")
        print(f"You have {lives}/6 left")
        if lives == 0:
            game_over = True
            print("You lose")
            
    #the player win
    if "_" not in display:
        game_over = True
        print("You win")
    
    #print hangman
    print(hangman[lives])
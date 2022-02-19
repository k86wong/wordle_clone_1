import random
import sys
import pandas as pd

word_df = pd.read_csv(r'C:\Users\kylew\Documents\dev_mans\wordle_clone_1\word_list.txt', sep=" ", header=None)
word_list = word_df[0].values.tolist()

day_word = random.choice(word_list)
letter_list = list(day_word)
print("INSTRUCTIONS:\n^ means that you have this letter is in the right place.\n* means that this letter is correct, but at another position.\n_ means that the letter is not present in the word.\n")

for i in range(6):
    print(f"You have {6 - i} guesses left.")
    guess = input("Guess a 5 letter word!\n")
    while guess not in word_list:
        guess = input("Your word must be an actual 5 letter word.\n")
    if guess == day_word:
        print('Congrats, you got the word of the day!')
        sys.exit()

    for i in range(5):
        if guess[i] == day_word[i]:
            print('^', end="")
        elif guess[i] in letter_list:
            print('*', end="")
        else:
            print('_', end="")
    print("\n")

print("Sorry, you did not get the word of the day this time around! Better luck next time.")


# #Still need to implement the letter bank - which letters are not used? 
# #also want to implement a better way to import a word list.
        






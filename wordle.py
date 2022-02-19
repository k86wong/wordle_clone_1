import random
import sys
import pandas as pd

word_df = pd.read_csv(r'C:\Users\kylew\Documents\dev_mans\wordle_clone_1\word_list.txt', sep=" ", header=None)
word_list = word_df[0].values.tolist()

day_word = random.choice(word_list)
#print(day_word)
letter_list = list(day_word)
alphabet = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'
alphabet_sign = '_ '
alphabet_sign = alphabet_sign * 26
print("INSTRUCTIONS:\n^ means that you have this letter is in the right place.\n* means that this letter is correct, but at another position.\nx means that the letter is not present in the word.\n")

record_correct = []
for i in range(6):
    print(f"You have {6 - i} guesses left.")
    guess = input("Guess a 5 letter word.\n\n")

    while guess not in word_list:
        guess = input("\nYour word must be an actual 5 letter word.\n")
    if guess == day_word:
        print('Congrats, you got the word of the day!')
        sys.exit()
    
    for i in range(5):
        asc = ord(guess[i]) - 97
        if guess[i] == day_word[i]:
            print('^', end="")
            if asc not in record_correct:
                alphabet_sign = alphabet_sign[:asc*2] + "^" + alphabet_sign[(asc*2)+1:]
                record_correct.append(asc)
                #print(record_correct)
        elif guess[i] in letter_list:
            print('*', end="")
            if asc not in record_correct:
                alphabet_sign = alphabet_sign[:asc*2] + "*" + alphabet_sign[(asc*2)+1:]
        else:
            print('x', end="")
            alphabet_sign = alphabet_sign[:asc*2] + "x" + alphabet_sign[(asc*2)+1:]

    print("\n")

    print(alphabet)
    print(alphabet_sign)
    print("")

print(f"Sorry, you did not get the word of the day this time around! Better luck next time.\nThe word of the day was {day_word}.")


# #Still need to implement the letter bank - which letters are not used? 
# #also want to implement a better way to import a word list.
        






# PROJECT_05_hangman_game
# this project requires the module "req_words" to run. Please download that from the library!

import random
from req_words import lst
HANGMANPICS = [r'''
    +---+
    |   |
        |
        |
        |
        |
=========== ''', r'''
    +---+
    |   |
    O   |
        |
        |
        |
=========== ''', r'''
    +---+
    |   |
    O   |
    |   |
        |
        |
=========== ''', r'''
    +---+
    |   |
    O   |
   /|   |
        |
        |
=========== ''', r'''
    +---+
    |   |
    O   |
   /|\  |
        |
        |
===========''', r'''
    +---+
    |   |
    O   |
   /|\  |
   /    |
        |
===========''', r'''

    +---+
    |   |
    O   |
   /|\  |
   / \  |
        |
=========== ''']

hang_obj = (random.choice(lst)).lower()
#print(hang_obj)

word= hang_obj
lst_ind = []
blanks = ""
fill = ""
length_of_word = len (hang_obj)
print ("Guess the word!")
for i in range (0, length_of_word):
    blanks += "_"
print (blanks)
print (HANGMANPICS[0])
lives = 1
while lives <= 6:
    if fill != hang_obj:
        cond1 = True
        while cond1:
            chr = ""
            chr = input ("Enter a letter! :-    ")
            print ("\n\n\n")
            chr = chr.lower()
            chr= chr.strip()
            if len(chr)>1 or not chr.isalpha():
                print ("Not valid imput! Try again!\n")
                cond1 = True
            else:
                cond1 = False
        for j in hang_obj:
            if j == chr:
                cond2 = True
                break
            else:
                cond2 = False
        if cond2:
            ind = word.find(chr)
            fill = ""
            for j in range (length_of_word):
                if (j == ind) and (j not in lst_ind) :
                    fill += chr
                    word = word[:ind] + "_" + word[ind + 1 :]
                else:
                    fill += blanks[j]
            lst_ind.append(ind)
            blanks = fill
        else:
            print ("****************************************************************************************      WRONG!      ****************************************************************************************")
            print (HANGMANPICS[lives])
            print (f"You only have {6 - lives} lives remaining! \n\n\n")
            lives += 1
        print  (fill+'\n\n\n')
    else:
        break
if fill == hang_obj:
    print ("Congratulations! You have Won!")
else:
    print ("Alas! You have lost! The right word is : "+hang_obj.upper())
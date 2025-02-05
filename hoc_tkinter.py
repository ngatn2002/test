import random

print("welcome to hangman")
print("-------------------------------------------")

words = ["sunflower", "house","diamond","memes","yeet","hello","like"]
random_word = random.choice(words)

for word in random_word:
    print("_",end=" ")

def print_hangman(wrong):
    if(wrong == 0):
        print("\n+---+")
        print("    |")
        print("    |")
        print("    |")
        print("   ===")
    elif(wrong==1):
        print("\n+---+")
        print("o   |")
        print("    |")
        print("    |")
        print("   ===")
    elif(wrong==2):
        print("\n+---+")
        print("o   |")
        print("|   |")
        print("    |")
        print("   ===")
    elif(wrong==3):
        print("\n+---+")
        print(" o  |")
        print("/|  |")
        print("    |")
        print("   ===")
    elif(wrong==4):
        print("\n+---+")
        print(" o  |")
        print("/|\ |")
        print("    |")
        print("   ===")
    elif(wrong==5):
        print("\n+---+")
        print(" o  |")
        print("/|\ |")
        print("/  |")
        print("   ===")
    elif(wrong==6):
        print("\n+---+")
        print(" o  |")
        print("/|\ |")
        print("/ \ |")
        print("   ===")

def printword(guess):
    counter = 0
    right = 0
    for char in random_word:
        if(char in guess):
            print(random_word[counter],end=" ")
            right += 1
        else:
            print(" ",end=" ")
            counter+=1
    return right

def printline():
    print("\r")
    for char in random_word:
        print("\u203E",end=" ")

length_word = len(random_word)
amount_times_wrong = 0
current_guess_index = 0
current_letter_guess = []
current_letter_right = 0

while(amount_times_wrong != 6 and current_letter_right != length_word):
    print("\nLetters guessed so far")
    for letter in current_letter_guess:
        print(letter, end=" ")
    letterguess = input("\nGuess a letter: ")
    if(random_word[current_guess_index] == letterguess):
        print_hangman(amount_times_wrong)
        current_guess_index +=1
        current_letter_guess.append(letterguess)
        current_letter_right = printword(current_letter_guess)
        printline()
    
    else:
        amount_times_wrong += 1
        current_letter_guess.append(letterguess)

        print_hangman(amount_times_wrong)

        current_letter_right = printword(current_letter_guess)
        printline()
print("Game over")

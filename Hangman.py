import wordsHangman
import random
ply_name = input("Enter Your Name: ")
def random_word():
    imported_list = wordsHangman.words_list
    return  random.choice(imported_list)
    
def displaying_word(word,gussed_letters):
    displayed_word = ""
    for letter in word:
        if letter in gussed_letters:
            displayed_word += letter
        else:
            displayed_word +="_"
    return displayed_word

word = random_word()
gussed_letter = []
incorrect_guess = 0
Max_Attempts = 6

print(f"Welcome to the Hangman Game {ply_name} - ")

while True:
    print("\n" + displaying_word(word, gussed_letter))

    guess = input("Guess a letter: ").lower()
    if len(guess)>1:
        print("Please Enter a Single Alphabet!")
    elif guess.isnumeric()==True:
        print("Enter Alphabets only!")
    else:         
        if guess in gussed_letter:
            print("You have already gussed this letter: ")
            continue
        gussed_letter.append(guess)

        if guess not in word:
            print("incorrect Guess!")
            incorrect_guess+=1
            print("Attempts Remaining: ",Max_Attempts-incorrect_guess)
            if incorrect_guess==Max_Attempts:
                print("You Have runned out of attempts!")
                break
        else:
            print("Correct Guess")
            
        if all(letter in gussed_letter for letter in word):
            print(f"Congratulation You Guessed the Word {ply_name}!",word)
            break


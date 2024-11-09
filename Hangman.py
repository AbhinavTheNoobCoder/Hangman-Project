import os
def clear_shell():
    # Clear the shell based on the operating system
    os.system('cls' if os.name == 'nt' else 'clear')

print('''Welcome to Hangman.
Please enter a word which others must guess.
Minimum length of the word must be 5.
For every 4 letters in the word, you must reveal one letter.
''')

word_to_guess = input("Enter the word to be guessed by all: ").lower()

if len(word_to_guess) < 5: #Minimum length not met
    raise ValueError("You were supposed to input a word of length more than 5.")

revealed_list = []
guessed_list = []
for _ in range(len(word_to_guess)//4):
    reveal_letter = input("Reveal a letter: ").lower()
    revealed_list.append(reveal_letter)

clear_shell()
hidden_word = ""
incorrect_tries = 0
print("Start guessing the word.\n")
while incorrect_tries < 6:
    for letter in word_to_guess:
        if letter in (revealed_list + guessed_list) or (not letter.isalpha()):
            hidden_word += letter

        else:
            hidden_word += "_"
    
    print(" ".join(hidden_word))
    if "_" not in hidden_word:
        print("You won, congratulations.")
        break

    guess = input("Guess a letter of the word: ")
    if guess not in word_to_guess:
        incorrect_tries += 1
        print("Incorrect guess. Letter not in word.")
        print("Lives left:", 6 - incorrect_tries)
    
    else:
        guessed_list.append(guess)
        print("Correct guess. Letter found in word.")
    
    hidden_word = ""
    print()

else:
    print("You lost. The word was:", word_to_guess)

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
if len(word_to_guess) < 5:
    print("You were supposed to input a word of length more than 5.0")
else:
    letters = [i for i in word_to_guess if i.isalnum()]
    number_of_reveals = len(letters)//4
    list_of_revealers = []
    for i in range(number_of_reveals):
        revealer = input("Enter a letter you would like to reveal: ")
        list_of_revealers.append(revealer)
    hidden_word = ""
    for i in word_to_guess:
        if i not in list_of_revealers:
            if not i.isspace():
                hidden_word += "_ "
            else:
                hidden_word += " "
        else:
            hidden_word += f"{i} "
    clear_shell()
    print("Start guessing the word now.")
    print(hidden_word)
    wrong_turns = 0
    while wrong_turns < 6:
        user_guess = input("Enter a letter for the guess: ")
        if user_guess not in word_to_guess:
            wrong_turns += 1
            print(f"Letter not found in word. You have {6-wrong_turns} chances left. \n")
            print(hidden_word)
        else:
            correct_letter_count = word_to_guess.count(user_guess)
            print("Letter found in word.\n")
            list_of_indices = []
            for i in range(len(word_to_guess)):
                if word_to_guess[i] == user_guess:
                    list_of_indices.append(i)
            hidden_list = [].extend(word_to_guess)
            new_hidden_word = ''
            for ind in range(len(word_to_guess)):
                if ind not in list_of_indices:
                    if word_to_guess[ind] in hidden_word:
                        new_hidden_word += word_to_guess[ind]
                    else:
                        if not word_to_guess[ind].isspace():
                            new_hidden_word += "_ " 
                        else:
                            new_hidden_word += " "
                else:
                    new_hidden_word += f"{word_to_guess[ind]}"
            hidden_word = new_hidden_word
            print(hidden_word)
        if hidden_word == word_to_guess:
            print("You won. Congratulations.")
            break
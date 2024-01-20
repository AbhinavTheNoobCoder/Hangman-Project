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
    print("You were supposed to input a word of length more than 5.")
else:
    letters = [i for i in word_to_guess if i.isalnum()] #list of purely letters/numbers
    number_of_reveals = len(letters)//4 #reveal 1 letter per every 4
    list_of_revealers = [] #letters to be revealed
    for i in range(number_of_reveals):
        revealer = input("Enter a letter you would like to reveal: ")
        list_of_revealers.append(revealer)
    hidden_word = ""
    for i in word_to_guess:
        if i not in list_of_revealers: #keep the letter hidden
            if i.isalnum(): #not space or hyphen
                hidden_word += "_"
            else:
                hidden_word += i
        else: #letter to be revealed
            hidden_word += i
    clear_shell()
    print("Start guessing the word now.")
    print(" ".join(hidden_word)) #make it readable
    wrong_turns = 0
    while wrong_turns < 6: #6th mistake is fatal
        user_guess = input("Enter a letter for the guess: ").lower()
        if user_guess not in word_to_guess: #incorrect guess
            wrong_turns += 1
            print(f"Letter not found in word. You have {6-wrong_turns} chances left. \n")
            print(" ".join(hidden_word)) #make it readable
        else: #correct guess
            print("Letter found in word.\n")
            new_hidden_word = '' #new_hidden_word will contain letters of hidden_word as well as user_guess
            for character in word_to_guess: #each letter of the word
                if character in hidden_word: #already guessed/revealed letter
                    new_hidden_word += character
                else:
                    if character == user_guess: #user's correct guess
                        new_hidden_word += character
                    else: #not guessed yet
                        if character.isalnum():
                            new_hidden_word += "_"
                        else:
                            new_hidden_word += character
            hidden_word = new_hidden_word #reassign hidden_word to keep track
            print(" ".join(hidden_word)) #make it readable
        if "_" not in hidden_word: #all letters have been guessed
            print("You won. Congratulations.")
            break
    else:
        print("The word was", word_to_guess)
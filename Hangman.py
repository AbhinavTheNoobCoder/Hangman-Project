drawings = {
0: '''
  +---+
  |   |
      |
      |
      |
      |
=========''',

1: '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''',

2: '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''',

3: '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''',

4: r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''',

5: r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''',

6: r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
========='''}

mode = int(input('''Select the mode:
1 - Standard English words
2 - Manually enter a word, have the other person guess
>>> '''))

word_to_guess = "- "
if mode == 1:
  import random
  try:
    from wonderwords import RandomWord
    word_generator = RandomWord()
    word_to_guess = word_generator.word(word_min_length=6)
    unique_letters = list(dict.fromkeys(word_to_guess, None))
    # dict does not have duplicate keys, using list we get the keys of the dict
    # which are the letters of the word

    revealed_letters = random.sample(population=unique_letters, k=len(word_to_guess)//4)
  
  except ImportError:
    choice = int(input('''The "wonderwords" package is not installed.
Enter 1 to install it and continue with the code.
Enter any other digit to change the mode to manual.
>>> '''))
    
    if choice == 1:
      import subprocess, sys
      try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "wonderwords"])
        print("wonderwords has been installed successfully!")

        from wonderwords import RandomWord
        word_generator = RandomWord()
        word_to_guess = word_generator.word(word_min_length=6)
        unique_letters = list(dict.fromkeys(word_to_guess, None))
        revealed_letters = random.sample(population=unique_letters, k=len(word_to_guess)//4)

      except subprocess.CalledProcessError:
        print("Failed to install 'wonderwords'. Please install it manually.")
        sys.exit(1)
    
    else:
      mode = 2

if mode == 2:
  import os
  def clear_shell():
  # Clear the shell based on the operating system
    os.system('cls' if os.name == 'nt' else 'clear')

  word_to_guess = input("Enter the word to be guessed by all (min. length = 5): ").lower()

  if len(word_to_guess) < 5: #Minimum length not met
    raise ValueError("You were supposed to input a word of length more than 5.")

  revealed_letters = []
  for _ in range(len(word_to_guess)//4):
    reveal_letter = input("Reveal a letter: ").lower()
    revealed_letters.append(reveal_letter)

  clear_shell()

guessed_letters = []
hidden_word = ""
print("Start guessing the word now.")
wrong_tries = 0

while wrong_tries < 6:
  print(drawings[wrong_tries], '\n')
  for letter in word_to_guess:
    if letter in (revealed_letters + guessed_letters) or (not letter.isalpha()):
      hidden_word += letter

    else:
      hidden_word += "_"
  
  print(" ".join(hidden_word)) #make the hidden word more readable with spacing

  if "_" not in hidden_word:
    print("You won. Congratulations.")
    print("Incorrect tries:", wrong_tries, "\n")
    break
    
  guess = input("Guess a letter of the word: ").lower()
  if guess not in word_to_guess:
    wrong_tries += 1
    print("INCORRECT GUESS!", 6 - wrong_tries, "lives remaining.\n")
    hidden_word = ""
  
  else:
    guessed_letters.append(guess)
    print("CORRECT GUESS, LETTER FOUND IN WORD.\n")
    hidden_word = ""

else: #if the user loses, the while loop does NOT break, and reaches the ELSE block
  print("You lost. The word was:", word_to_guess)
  print(drawings[6], '\n')

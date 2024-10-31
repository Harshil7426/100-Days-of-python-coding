import random
HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
hang=0

listOfWords = [
    "british", "suave", "integrity", "accent", "evil", "genius", "downton"
]

wordChosen = random.choice(listOfWords)
print(wordChosen)
print("Hangman")
print("The word has", len(wordChosen), "letters.")

guessedLetters = []
letterlist = ["_" for _ in wordChosen]
lives = 7

while lives > 0:
    print(" ".join(letterlist))
    print()
    letter = input("Choose a letter: ").lower()
    if letter in guessedLetters:
        print("You've already guessed that letter.")
        continue
    else:
        guessedLetters.append(letter)

        if letter in wordChosen:
            print("Correct!")
            for j in range(len(wordChosen)):
                if wordChosen[j] == letter:
                    letterlist[j] = letter

            if "_" not in letterlist:
                print("Congratulations! You guessed the word:", wordChosen)
                break
        else:
          print(HANGMANPICS[hang])
          lives -= 1
          hang+=1
          print("Incorrect! You have", lives, "lives left.")

        if lives == 0:
            print("Game Over! The word was:", wordChosen)

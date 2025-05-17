import random,string
from words import words
def getValidWord(words):
    word=random.choice(words)
    while '-' in word or ' ' in word:
        word= random.choice(words)
    return word.upper()
def hangman():
    word=getValidWord(words)
    wordLetter=set(word)
    alphabet= set(string.ascii_uppercase)
    usedLetters=set()
    lives=6
    while len(wordLetter)>0 and lives > 0:
        print('You have',lives,'lives , You have used these letters ',' '.join(usedLetters))
        wordList = [letter if letter in usedLetters else '-'for letter in word]
        print('Current word:', ' '.join(wordList))
        userLetter=input('Guess the letter: ').upper()
        if userLetter in alphabet - usedLetters:
            usedLetters.add(userLetter)
            if userLetter in wordLetter:
                wordLetter.remove(userLetter)
            else:
                lives=lives-1
                print('letter not in word')
        elif userLetter in usedLetters:
            print('You already have used it')
        else:
            print('Invalid guess') 
    if(lives==0):
        print("You died, the word was",word)
    else:
        print('You have guessed the word',word,"!!")
hangman()
import random

class Hangman_game:
    def __init__(self):
        self.user_guesses = 7
        self.choose_word()

    def choose_word(self):
        self.words = []
        f = open("dictionary.txt")
        for line in f:
            self.words.append(line)
        self.word = random.choice(self.words)
        
        f.close()

    def guesses(self):
        self.letters = []
        self.unknown = []
        for ch in self.word:
            self.letters.append(ch)
            self.unknown.append("_ ")
        while self.user_guesses > 0:
            self.guess = input("What letter do you want to choose?")
            if self.guess in self.letters:
                for letter in self.word:
                    

def main():
    game = Hangman_game()
    print ("Welcome! You are playing hangman. To start, you will have 7 guesses.")
    print (game.word)
main()
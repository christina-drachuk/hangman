import random

class Hangman_game:
    def __init__(self):
        self.user_guesses = 7
        self.choose_word()
        self.guesses()

    def choose_word(self):
        self.words = []
        f = open("dictionary.txt")
        for line in f:
            line = line.strip()
            self.words.append(line)
        self.word = random.choice(self.words)
        
        f.close()

    def guesses(self):
        print (self.word)
        self.letters_guessed = ''

        while self.user_guesses > 0:
            self.letters_left = 0

            for letter in self.word:
                if letter in self.letters_guessed:
                    print (letter)
                else:
                    print ("_")
                    self.letters_left += 1
            
            if self.letters_left == 0:
                print ("Congrats")
                break

            self.guess = input ("Guess a letter: ")

            self.letters_guessed += self.guess

            if self.guess not in self.word:
                self.user_guesses -= 1
                print ("Nope, only " + str(self.user_guesses) + " left.")

                if self.user_guesses == 0:
                    print ("Play again")

                    

def main():
    print ("Welcome! You are playing hangman. To start, you will have 7 guesses.")
    game = Hangman_game()
    print (game.word)
# main()
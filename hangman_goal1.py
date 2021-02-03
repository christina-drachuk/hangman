import random
user_guesses = 7
print ("Welcome! You are playing hangman. To start, you will have 7 guesses.")

def choose_word(self):
    self.words = []
    f = open("dictionary.txt")
    for line in f:
        self.words.append(line)
    self.word = random.choice(self.words)
    
    f.close()

def main(self):
    print (self.word)
main()
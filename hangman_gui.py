import tkinter as tk
import string
import random
# from hangman_goal1 import Hangman_game

class Application(tk.Frame):
    def __init__ (self, master):
        super().__init__(master)
        self.grid()
        self.user_guesses = 7
        self.choose_word()
        self.create_widgets()
        self.letters_guessed = ''
        # self.guesses()

    def choose_word(self):
        self.words = []
        f = open("dictionary.txt")
        for line in f:
            line = line.strip()
            self.words.append(line)
        self.word = random.choice(self.words)

    def create_widgets(self):
        self.letter_buttons = {}
        # alphabet_string = string.ascii_lowercase
        # alphabet_list = list(alphabet_string)
        column = 0
        tk.Label(self, text = "Enter your guess here: ").grid(row = 0, column = 0)
        self.guess = tk.Entry(self, width = 10)
        self.guess.grid(row = 0, column = 1)
        self.enter_bttn = tk.Button(self, text = "Enter", command = self.guesses)
        self.enter_bttn.grid(row = 0, column = 2)
        self.underscores = []
        column = 0
        for letter in self.word:
            letter = letter.strip()
            # tk.Label(self, text = "_ ").grid(row = 1, column = column)
            self.underscores.append("_")
            column += 1
    
        y = " ".join(self.underscores)
        self.result = tk.Label(self, text = y)
        self.result.grid(row = 1, column = 0, columnspan = 3)
        self.guesses_left = tk.Label(self, text = "")

    def guesses(self):
        print (self.word)
        
        
        if self.user_guesses > 0:
            self.letters_left = 0
            for letter in self.word:
                if letter in self.letters_guessed:
                    pass
                else:
                    print ("_")
                    self.letters_left += 1
            
            if self.letters_left == 0:
                self.result["text"] = "Congrats, you guessed correct!"

            self.letters_guessed += self.guess.get()

            if self.guess.get() not in self.word:
                self.user_guesses -= 1
                print ("Nope, only " + str(self.user_guesses) + " left.")

                if self.user_guesses == 0:
                    print ("Play again")

root = tk.Tk()
app = Application(root)
root.mainloop()
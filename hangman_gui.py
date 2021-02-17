import tkinter as tk
import string
import random
# from hangman_goal1 import Hangman_game

class Application(tk.Frame):
    def __init__ (self, master):
        super().__init__(master)
        self.create_widgets()
        self.grid()

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

    def create_widgets(self):
        alphabet_string = string.ascii_lowercase
        alphabet_list = list(alphabet_string)
        column = 0
        for letters in alphabet_list[0:13]:
            self.letter = tk.Button(self, text = letters, command = lambda l=letters: self.button_press(l))
            self.letter.grid(row = 0, column = column)
            column += 1
        column = 0
        for letters in alphabet_list[13:]:
            self.letter = tk.Button(self, text = letters, command = self.guesses)
            self.letter.grid(row = 1, column = column)
            column += 1

    def button_press(self, letter):
        print(letter)



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

root = tk.Tk()
app = Application(root)
root.mainloop()
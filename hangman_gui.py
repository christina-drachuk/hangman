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
        self.all_letters = ''
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
        self.guess_message = tk.Label(self, text = "")
        self.guess_message.grid(row = 3, column = 0, columnspan = 3)
        self.guess_update = tk.Label(self, text = "")
        self.guess_update.grid(row = 2, column = 0, columnspan = 3)

    def guesses(self):
        # self.letters_guessed += self.guess.get()
        self.letters_guessed = self.guess.get()
        self.all_letters += self.guess.get()
        # for char in self.letters_guessed: # move into if statement, make a list for letters guessed and a current letter variable
        #     self.letters_guessed_list = []
        #     self.letters_guessed_list.append(self.letters_guessed) # this part has to be moved to before the entry is cleared
        #     print(self.letters_guessed_list)
        for char in self.all_letters:
            if char not in self.word:
                self.user_guesses -= 1
                self.guess_message["text"] = "Nope, only " + str(self.user_guesses) + " guesses left."
        print(self.all_letters)
        print(self.letters_guessed)
        self.guess.delete(0, tk.END) # this has to occur after the letter is appended to the list

        
        print (self.word) # TODO remove this!!!
        self.letter_list = []
        
        position = 0

        if self.user_guesses > 0: # TODO show how many guesses left
            self.guess_update["text"] = "Guesses: " + str(self.user_guesses)
            self.letters_left = 0
            for letter in self.word:
                self.letter_list.append(letter)
                if letter not in self.letters_guessed:
                    self.letter_list[position] = ('_')
                    # print ("_")
                    self.letters_left += 1 
                position += 1
            y = " ".join(self.letter_list)
            self.result["text"] = y
        
        # TODO add the following into a loop and make it check if the letter is not in the word
        # at all. If this is the case, subtract a guess from the user and draw a body part, and raise
        # the message.
        # if self.guess.get() not in self.word:
        #     self.user_guesses -= 1
        #     self.guess_message["text"] = "Nope, only " + str(self.user_guesses) + " left."
                
            
        if self.letters_left == 0:
            self.guess_message["text"] = "Congrats, you guessed correct!"

        if self.user_guesses == 0:
            print ("Play again")

root = tk.Tk()
app = Application(root)
root.mainloop()
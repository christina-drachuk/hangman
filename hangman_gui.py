# TODO change definitions for presentation, go through code + clean, change range, delete comments, paste new definitions.
import tkinter as tk
import string
import random
import sys
import os
class Application(tk.Frame):
    def __init__ (self, master):
        super().__init__(master)

        self.grid()

        self.user_guesses = 10
        self.amount = 0

        self.choose_word()
        self.create_widgets()

        self.letters_guessed = ''
        self.current = ''

        self.guesses()  
    
    def choose_word(self):
        self.words = []
        self.random_num = random.randrange(0, 172)
        f = open("dictionary.txt")
        
        for line in f:
            line = line.strip()
            self.words.append(line)
            
        self.word = self.words[self.random_num]

    def create_widgets(self):
        self.intro = tk.Label(self, text = "Enter your guess here (lowercase only): ")
        self.intro.grid(row = 0, column = 0)

        self.guess = tk.Entry(self, width = 10)
        self.guess.grid(row = 0, column = 1, sticky = tk.NSEW)

        self.enter_bttn = tk.Button(self, text = "Enter", command = self.guesses)
        self.enter_bttn.grid(row = 1, column = 1, sticky = tk.NSEW)
        self.underscores = []

        column = 0
        for letter in self.word:
            letter = letter.strip()
            self.underscores.append("_")
            column += 1

        y = " ".join(self.underscores)
        self.result = tk.Label(self, text = y)
        self.result.grid(row = 1, column = 0, columnspan = 3)

        self.guess_message = tk.Label(self, text = "")
        self.guess_message.grid(row = 2, column = 0, columnspan = 3)

        self.guess_update = tk.Label(self, text = "")
        self.guess_update.grid(row = 3, column = 0, columnspan = 3)

        self.final_word = tk.Label(self, text = "")
        self.final_word.grid(row = 4, column = 0, columnspan = 3)

        self.chars_guessed_label = tk.Label(self, text = "")
        self.chars_guessed_label.grid(row = 5, column = 0, columnspan = 3)

        self.definitions_text = tk.Label(self, text = "")
        self.definitions_text.grid(row = 6, column = 0, columnspan = 3)

        self.def_buttons = tk.Button(self, text = "Definition", command = self.definition)
        self.def_buttons.grid(row = 2, column = 1)

    def guesses(self):
        canvas = tk.Canvas(self, height = 350, width = 350)
        self.current = self.guess.get()
        if self.current not in self.letters_guessed: 
            self.letters_guessed += self.guess.get()

        self.chars_guessed_label["text"] = "Letters you've guessed: " + str(self.letters_guessed)
            
        self.guess.delete(0, tk.END)

        if self.current not in self.word and self.user_guesses > 0:
            self.user_guesses -= 1
            self.guess_message["text"] = "Nope, only " + str(self.user_guesses) + " guesses left."
        elif self.current == "":
            pass
        else:
            self.guess_message["text"] = "Keep guessing!"

        if self.user_guesses == 9:
            canvas.create_line(230, 300, 270, 300, fill="black")

        elif self.user_guesses == 8:
            canvas.create_line(250, 15, 250, 300, fill="black")
            canvas.create_line(230, 300, 270, 300, fill="black")

        elif self.user_guesses == 7:
            canvas.create_line(250, 15, 250, 300, fill="black")
            canvas.create_line(230, 300, 270, 300, fill="black")
            canvas.create_line(110, 15, 250, 15, fill="black")

        elif self.user_guesses == 6:
            canvas.create_line(250, 15, 250, 300, fill="black")
            canvas.create_line(110, 15, 110, 65, fill="black")
            canvas.create_line(110, 15, 250, 15, fill="black")
            canvas.create_line(230, 300, 270, 300, fill="black")

        elif self.user_guesses == 5:
            canvas.create_line(250, 15, 250, 300, fill="black")
            canvas.create_line(110, 15, 110, 65, fill="black")
            canvas.create_line(110, 15, 250, 15, fill="black")
            canvas.create_line(230, 300, 270, 300, fill="black")

            canvas.create_oval(75, 65, 150, 140, outline="magenta4", fill = "SlateGray1", width=1)

        elif self.user_guesses == 4:
            canvas.create_line(250, 15, 250, 300, fill="black")
            canvas.create_line(110, 15, 110, 65, fill="black")
            canvas.create_line(110, 15, 250, 15, fill="black")
            canvas.create_line(230, 300, 270, 300, fill="black")

            canvas.create_oval(75, 65, 150, 140, outline="magenta4", fill = "SlateGray1", width=1)

            canvas.create_line(110, 140, 110, 240, fill="magenta4")

        elif self.user_guesses == 3:
            canvas.create_line(250, 15, 250, 300, fill="black")
            canvas.create_line(110, 15, 110, 65, fill="black")
            canvas.create_line(110, 15, 250, 15, fill="black")
            canvas.create_line(230, 300, 270, 300, fill="black")
            canvas.create_oval(75, 65, 150, 140, outline="magenta4", fill = "SlateGray1", width=1)

            canvas.create_line(110, 140, 110, 240, fill="magenta4")

            canvas.create_line(35, 135, 110, 190, fill="magenta4")

        elif self.user_guesses == 2:
            canvas.create_line(250, 15, 250, 300, fill="black")
            canvas.create_line(110, 15, 110, 65, fill="black")
            canvas.create_line(110, 15, 250, 15, fill="black")
            canvas.create_line(230, 300, 270, 300, fill="black")

            canvas.create_oval(75, 65, 150, 140, outline="magenta4", fill = "SlateGray1", width=1)

            canvas.create_line(110, 140, 110, 240, fill="magenta4")
            
            canvas.create_line(35, 135, 110, 190, fill="magenta4")
            
            canvas.create_line(185, 135, 110, 190, fill="magenta4")

        elif self.user_guesses == 1:
            canvas.create_line(250, 15, 250, 300, fill="black")
            canvas.create_line(110, 15, 110, 65, fill="black")
            canvas.create_line(110, 15, 250, 15, fill="black")
            canvas.create_line(230, 300, 270, 300, fill="black")

            canvas.create_oval(75, 65, 150, 140, outline="magenta4", fill = "SlateGray1", width=1)

            canvas.create_line(110, 140, 110, 240, fill="magenta4")
            
            canvas.create_line(35, 135, 110, 190, fill="magenta4")
            
            canvas.create_line(185, 135, 110, 190, fill="magenta4")
            
            canvas.create_line(35, 295, 110, 240, fill="magenta4")

        elif self.user_guesses == 0:
            canvas.create_line(250, 15, 250, 300, fill="black")
            canvas.create_line(110, 15, 110, 65, fill="black")
            canvas.create_line(110, 15, 250, 15, fill="black")
            canvas.create_line(230, 300, 270, 300, fill="black")

            canvas.create_oval(75, 65, 150, 140, outline="magenta4", fill = "SlateGray1", width=1)

            canvas.create_line(110, 140, 110, 240, fill="magenta4")
        
            canvas.create_line(35, 135, 110, 190, fill="magenta4")

            canvas.create_line(185, 135, 110, 190, fill="magenta4")

            canvas.create_line(35, 295, 110, 240, fill="magenta4")

            canvas.create_line(185, 295, 110, 240, fill="magenta4")

        self.letter_list = []
        position = 0

        if self.user_guesses > 0:
            self.guess_update["text"] = "Guesses: " + str(self.user_guesses)
            self.letters_left = 0

            for letter in self.word:
                self.letter_list.append(letter)
                if letter not in self.letters_guessed:
                    self.letter_list[position] = ('_')
                    self.letters_left += 1 
                position += 1

            y = " ".join(self.letter_list)
            self.result["text"] = y

        if self.letters_left == 0:
            self.guess_message["text"] = "Congrats, you guessed correct!"

            self.guess_update.destroy()
            self.guess.destroy()
            self.enter_bttn.destroy()
            self.intro.destroy()

            self.exit_button = tk.Button(self, text = "Exit", command = self.root_destroy, width = 10) 
            self.exit_button.grid(row = 0, column = 0, sticky = tk.W)

            self.play_again = tk.Button(self, text = "Play Again", command = self.restart, width = 10)
            self.play_again.grid(row = 0, column = 1, sticky = tk.W, columnspan = 3)

        if self.user_guesses == 0:
            self.guess.destroy()
            self.enter_bttn.destroy()
            self.intro.destroy()

            self.exit_button = tk.Button(self, text = "Exit", command = self.root_destroy, width = 10) 
            self.exit_button.grid(row = 0, column = 0, sticky = tk.W)

            self.play_again = tk.Button(self, text = "Play Again", command = self.restart, width = 10)
            self.play_again.grid(row = 0, column = 1, sticky = tk.W, columnspan = 3)

            self.guess_message["text"] = "Nice Try"
            self.guess_update["text"] = "Guesses: 0"
            self.final_word["text"] = "The word was: " + str(self.word)

            self.canvas = canvas
    
        canvas.grid(row = 7, column = 0)
    
    def definition(self):
        self.def_buttons.destroy()
        self.definitions = []
        a = open("definitions.txt")
        
        for line in a:
            line = line.strip()
            self.definitions.append(line)
        self.definitions_text["text"] = "Definition: " + self.definitions[self.random_num]
        a.close()

    def root_destroy(self):
        root.destroy()

    def restart(self):
        python = sys.executable
        os.execl(python, python, * sys.argv)

root = tk.Tk()
root.title("Hangman")

app = Application(root)
root.mainloop()
import tkinter as tk
import string
import random
# from hangman_goal1 import Hangman_game
import sys
import os
class Application(tk.Frame):
    def __init__ (self, master):
        super().__init__(master)

        self.grid()

        self.user_guesses = 7

        self.choose_word()
        self.create_widgets()

        self.letters_guessed = ''
        self.all_letters = ''

        self.guesses()

    
    def choose_word(self):
        self.words = []
        f = open("dictionary.txt")
    def choose_word(self):
        self.words.append(line)
        self.word = random.choice(self.words)



    def create_widgets(self):
        self.letter_buttons = {}
        # alphabet_string = string.ascii_lowercase
        # alphabet_list = list(alphabet_string)
        column = 0
        self.intro = tk.Label(self, text = "Enter your guess here: ")
        self.intro = tk.Label(self, text = "Enter your guess here (lowercase only): ")
        self.intro.grid(row = 0, column = 0)

        self.guess = tk.Entry(self, width = 10)
        self.guess.grid(row = 0, column = 1)

        self.enter_bttn = tk.Button(self, text = "Enter", command = self.guesses)
        self.enter_bttn.grid(row = 0, column = 2)
        self.underscores = []
        column = 0

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

        self.final_word = tk.Label(self, text = "")
        self.final_word.grid(row = 4, column = 0, columnspan = 3)

        self.chars_guessed_label = tk.Label(self, text = "")
        self.chars_guessed_label.grid(row = 5, column = 0, columnspan = 3)

    def guesses(self):
        canvas = tk.Canvas(self, height = 350, width = 350)
        self.letters_guessed += self.guess.get()
        self.current = self.guess.get()
        # for char in self.letters_guessed: # move into if statement, make a list for letters guessed and a current letter variable
        #     self.letters_guessed_list = []
        #     self.letters_guessed_list.append(self.letters_guessed) # this part has to be moved to before the entry is cleared
        #     print(self.letters_guessed_list)
        self.chars_guessed_label["text"] = "Letters you've guessed: " + str(self.letters_guessed)

        print(self.all_letters)
        print(self.letters_guessed)
        self.guess.delete(0, tk.END) # this has to occur after the letter is appended to the list
        self.guess.delete(0, tk.END)

        if self.current not in self.word and self.user_guesses > 0:
            self.user_guesses -= 1
            self.guess_message["text"] = "Nope, only " + str(self.user_guesses) + " guesses left."

        elif self.current == "":
            pass

        else:
            self.guess_message["text"] = "Keep guessing!"

        if self.user_guesses == 6:
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

        print (self.word) # TODO remove this!!!
        self.letter_list = []
        position = 0

        if self.user_guesses > 0: # TODO show how many guesses left
        if self.user_guesses > 0:
            self.guess_update["text"] = "Guesses: " + str(self.user_guesses)
            self.letters_left = 0

    def guesses(self):
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

            self.guess_update.destroy()
            self.guess.destroy()
            self.enter_bttn.destroy()
            self.intro.destroy()

            self.exit_button = tk.Button(self, text = "Exit", command = self.root_destroy) 
            self.exit_button.grid(row = 0, column = 0)

            self.play_again = tk.Button(self, text = "Play Again", command = self.restart)
            self.play_again.grid(row = 0, column = 1)

        if self.user_guesses == 0:
            self.guess.destroy()
            self.enter_bttn.destroy()
            self.intro.destroy()

            self.exit_button = tk.Button(self, text = "Exit", command = self.root_destroy) 
            self.exit_button.grid(row = 0, column = 0)

            self.play_again = tk.Button(self, text = "Play Again", command = self.restart)
            self.play_again.grid(row = 0, column = 1)

            self.guess_message["text"] = "Nice Try"
            self.guess_update["text"] = "Guesses: 0"

            self.final_word["text"] = "The word was: " + str(self.word)

            self.canvas = canvas

        canvas.grid(row = 6, column = 0)

    def root_destroy(self):
        root.destroy()

    def restart(self):
        python = sys.executable
        os.execl(python, python, * sys.argv)

root = tk.Tk()
root.geometry("300x200")
root.title("Hangman")

app = Application(root)
root.mainloop() 
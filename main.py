import tkinter as tk
import timeit
import random
import requests


class Game:
    def __init__(self):
        self.x = 0
        self.window_1 = tk.Tk()
        self.window_1.geometry("450x200")
        self.window_1.title("Typespeed Test App")

        response = requests.get('http://random-word-api.herokuapp.com/word?number=200')
        self.words = response.json()

        self.word_selected = random.choice(self.words)
        self.result = 0
        self.words_count = 0
        self.start = 0
        self.end = 0

        self.welcolme_label = tk.Label(text="Welcome to the typespeed test app, "
                               "\npress go to start testing your speed!", font="times 20")
        self.welcolme_label.place(x=10, y=50)

        self.go_button = tk.Button(text="Go", width=12, command=self.go, bg='white')
        self.go_button.place(x=150, y=150)



        self.window_1.mainloop()

    def go(self):
        if self.x == 0:
            self.window_1.destroy()
            self.x = self.x + 1
        self.start = timeit.default_timer()
        self.window_2 = tk.Tk()
        self.window_2.geometry("450x200")

        self.word = tk.Label(self.window_2, text=self.word_selected, font="times 20")
        self.word.place(x=150, y=10)

        self.command_label = tk.Label(self.window_2, text="Start Typing", font="times 20")
        self.command_label.place(x=10, y=50)

        self.entry = tk.Entry(self.window_2)
        self.entry.place(x=280, y=55)

        self.window_2.bind('<Return>', self.change_word)

        self.done_button = tk.Button(self.window_2, text="Done", command=self.check_result, width=12, bg='white')
        self.done_button.place(x=150, y=100)

        self.try_again_button = tk.Button(self.window_2, text="Try Again", command=self.go, width=12, bg='white')
        self.try_again_button.place(x=250, y=100)

        self.window_2.mainloop()

    def check_result(self):
        if self.result >= 60:
            minutes = self.result / 60
            words_per_minute = self.words_count / minutes
            self.wrong_label.destroy()
            result_label = tk.Label(self.window_2, text=f"You typed {round(words_per_minute)} words per minute!", font="times 10")
            result_label.place(x=30, y=150)
        else:
            self.wrong_label.destroy()
            words_per_minute = (self.words_count / self.result) * 60
            result_label = tk.Label(self.window_2, text=f"You typed {round(words_per_minute)} words per minute!", font="times 10")
            result_label.place(x=30, y=150)

    def change_word(self, event):
        if self.entry.get() == self.word_selected:
            self.word_selected = random.choice(self.words)
            self.end = timeit.default_timer()
            self.result = self.end - self.start
            self.words_count += 1
            self.word.configure(text=self.word_selected)
            self.entry.delete(0, 'end')
            self.wrong_label.destroy()
        else:
            self.wrong_label = tk.Label(self.window_2, text="Wrong spelling!", font="times 15")
            self.wrong_label.place(x=100, y=150)


Game().run()

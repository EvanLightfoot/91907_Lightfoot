# AS91907 - Howick College GeoGuesser
# Written By: Evan Lightfoot
# Date: 26/07/2024
# Version: 2
import random as r
import re
from tkinter import *
class Game:
    def __init__(self, points=0, rnd=0, guess=None, correct=None, incorrect=None, loc_num=None):
        self.points = points
        self.rnd = rnd
        self.guess = guess
        self.correct = correct
        self.incorrect = incorrect
        self.loc_num = loc_num
        
    def get_guess(self, root):
        self.guess = guess.get().replace(' ', '')
        validated_guess = re.sub('[^A-Za-z0-9]+', '', self.guess)
        self.guess = validated_guess
        if self.guess == "":
            pass
        else:
            return self.guess, self.get_answer()
            
    def get_answer(self):
        with open("Assets/answer_sheet.txt", 'r') as answers:
            data = answers.readlines()
            line = data[self.loc_num -1].strip().lower()
            words = line.split()
            return words, self.update_game_state(additive, words, count)
        answers.close()
        
    def update_game_state(self, additive, words, count):
        for word in words:
            if word in self.guess:
                self.points += additive
                self.rnd += 1
                count += 1
                points_val = IntVar(value=self.points)
                rnd_val = IntVar(value=self.rnd) 
                try:
                    self.incorrect.destroy()
                except AttributeError:
                    pass
                try: 
                    self.correct.destroy()
                except AttributeError:
                    pass
                self.correct = Label(root, text="Correct!", bg="#00FFFF", fg='green', font=("Calibri", "15", "bold"))
                self.correct.place(x=888, y=887)
                points_label = Label(root, textvariable=points_val, fg='black', bg='white', font=("Calibri", "16", "bold"))
                points_label.place(x=110, y=205)
                rnd_label = Label(root, textvariable=rnd_val, fg='black', bg='white', font=("Calibri", "16", "bold"))
                rnd_label.place(x=110, y=255)
                return self.points, self.rnd, count, self.get_loc(root, loc)
            else:
                try:
                    self.correct.destroy()
                except AttributeError:
                    pass
                try:
                    self.incorrect.destroy()
                except AttributeError:
                    pass
                additive -= 1
                self.incorrect = Label(root, text="Incorrect!", bg="#00FFFF", fg='darkred', font=("Calibri", "15", "bold"))
                self.incorrect.place(x=888, y=887)
                return additive
        
    def reset(self, root):
        additive = 3
        self.points = 0
        self.rnd = 0
        count = 0
        try:
            self.correct.destroy()
        except AttributeError:
            pass
        try:
            self.incorrect.destroy()
        except AttributeError:
            pass
        points_val = IntVar(value=self.points)
        rnd_val = IntVar(value=self.rnd)
        points_label = Label(root, textvariable=points_val, fg='black', bg='white', font=("Calibri", "16", "bold"))
        points_label.place(x=110, y=205)
        rnd_label = Label(root, textvariable=rnd_val, fg='black', bg='white', font=("Calibri", "16", "bold"))
        rnd_label.place(x=110, y=255)
        return self.points, self.rnd, count
        
    def get_loc(self, root, loc):
        try:
            loc_label.destroy()
        except NameError:
            pass
        loc_generate = r.randint(1, 30)
        self.loc_num = loc_generate
        loc_set = f"Loc{self.loc_num}"
        loc_img = PhotoImage(file=f"Assets/{loc_set}.png")
        loc_label = Label(root, height=700, width=1000, image=loc_img, bg='white', highlightbackground="black", highlightthickness=5)
        loc_label.image = loc_img
        loc_label.place(anchor='center', x=960, y=530)
        return self.loc_num
        
instance = Game()
loc = []
count = 0
additive = 3
# Quits the game (closes the window)
def quit(root):
    root.destroy()
    
def skip():
    additive = 3
    return additive, instance.get_loc(root, loc)
           
# G.U.I
root = Tk() # Initialises the window.
root.resizable(False, False) # Locks the window size to prevent re-sizing.
root.state('zoomed') # Makes the window fullscreen.
root.title("Howick College GeoGuesser V2.0")
root.configure(background='#00FFFF') # Cream coloured background.
guess = StringVar()
guess_text_box = Entry(root, textvariable=guess, width=30, highlightbackground="black", highlightthickness="1", font=("Calibiri", "11"))
guess_text_box.place(x=830, y=917)
guess_text_box_label = Label(root, text="Location:", fg="black", bg='#00FFFF', font=("Calibri", "15", "bold"))
guess_text_box_label.place(x=748, y=910)
guess_btn = Button(root, text="Guess", borderwidth="2", width="13", bg='#01F9C6', fg='black', font=("Calibri", "15", "bold"),command=lambda:instance.get_guess(root)) # Guess button, calls the guess function.
guess_btn.place(x=1100, y=900)
quit_btn = Button(root, text="Quit", borderwidth="2", width="13", bg='red', fg='black', font=("Calibri", "15", "bold"),command=lambda:quit(root)) # Quit button, calls the quit function.
quit_btn.place(x=594, y=900)
reset_btn = Button(root, text="Reset", borderwidth="2", width="13", bg='red', fg='black', font=("Calibri", "15", "bold"),command=lambda:instance.reset(root)) # Reset button, calls the reset function.
reset_btn.place(x=454, y=900)
skip_btn = Button(root, text="Skip", borderwidth="2", width="13", bg='red', fg='black', font=("Calibri", "15", "bold"),command=lambda:skip()) # Skip button, calls the get_loc function.
skip_btn.place(x=1240, y=900)
how_to_play_frame = Frame(root, bg='white', width=430, height=714, highlightbackground="black", highlightthickness=5) # Creates a frame (coloured box) for tidyness.
how_to_play_frame.place(x=1480, y=173)
how_to_play_title = Label(root, fg="darkblue", bg='white', text="How to play?", font=("Calibri", "20", "bold", "underline"))
how_to_play_title.place(x=1490, y=178)
how_to_play_text_l1 = Label(root, bg='white', fg="green", text="- Type your guess in the text box 'location' undeneath the image.", font=("Calibri", "11", "bold"))
how_to_play_text_l1.place(x=1490, y=215)
how_to_play_text_l2 = Label(root, bg='white', fg="green", text="- Ensure that you use correct grammer and clear guesses.", font=("Calibri", "11", "bold"))
how_to_play_text_l2.place(x=1490, y=250)
how_to_play_text_l3 = Label(root, bg='white', fg="green", text="- Gather as many points as possible by guessing correctly!", font=("Calibri", "11", "bold"))
how_to_play_text_l3.place(x=1490, y=285)
how_to_play_text_l4 = Label(root, bg='white', fg="green", text="- There are 10 rounds, but there are 30 points to get!", font=("Calibri", "11", "bold"))
how_to_play_text_l4.place(x=1490, y=320)
how_to_play_text_l5 = Label(root, bg='white', fg="green", text="- +3 points if you guess a location first try, +2 on second try!", font=("Calibri", "11", "bold"))
how_to_play_text_l5.place(x=1490, y=355)
how_to_play_text_l6 = Label(root, bg='white', fg="green", text="- Any more guesses give +1, so good luck and have fun!", font=("Calibri", "11", "bold"))
how_to_play_text_l6.place(x=1490, y=390)  
title = Label(root, text="Howick College GeoGuesser", bg='#00FFFF', fg='darkblue', font=("Calibri", "30", "bold", "underline"))
title.place(x=740, y=120)
game_stats_frame = Frame(root, bg='white', width=300, height=150, highlightbackground="black", highlightthickness=5)
game_stats_frame.place(x=2, y=174)
points_text = Label(root, bg='white', text="Points:", fg='black', font=("Calibri", "20", "bold"))
points_text.place(x=20, y=200)
rnd_text = Label(root, bg='white', text="Round:", fg='black', font=("Calibri", "20", "bold"))
rnd_text.place(x=20, y=250)
rnd_text2 = Label(root, bg='white', text="/10", fg='black', font=("Calibri", "16", "bold"))
rnd_text2.place(x=124, y=258)
crest_img = PhotoImage(file="Assets\crest.png") # Imports the Howick College Crest
crest_label = Label(root, height=175, width=200, image=crest_img, bg='white')
crest_label.place(x=1700, y=700)
instance.get_loc(root, loc)
root.mainloop() # Keeps the window open.
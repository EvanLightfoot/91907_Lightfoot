# AS91907 - Howick College GeoGuesser
# Written By: Evan Lightfoot
# Date: 17/06/2024
# Version: 1
from tkinter import *
class Game:
    def __innit__(self, points=0, time=0, game=1, guess=None):
        self.points = points
        self.time = time
        self.game = game
        self.guess = guess

    def get_guess(self, root):
        self.guess = guess.get()
        answers = open("answer_sheet.txt")
        for line in answers:
            line.strip().split('/n')
            if self.guess in line:
                self.points + 1
                self.game + 1
                try:
                    incorrect.destroy()
                    correct = Label(root, text="Correct!", fg='lime', font=("Calibri", "15", "bold")).place(x=770, y=900)
                except NameError:
                    correct = Label(root, text="Correct!", fg='lime', font=("Calibri", "15", "bold")).place(x=770, y=900)
                return self.points, self.game
            else:
                try:
                    correct.destroy()
                    incorrect = Label(root, text="Incorrect!", fg='red', font=("Calibri", "15", "bold")).place(x=770, y=900)
                except NameError:
                    incorrect = Label(root, text="Incorrect!", fg='red', font=("Calibri", "15", "bold")).place(x=770, y=900)
            answers.close()        

# Quits the game (closes the window)  
def quit(root):
    root.destroy()
    
    # Resets the game's status so it can be replayed.
    def reset(self, root):
        self.points = 0
        self.game = 1
        self.time = 0
        return self.points, self.game, self.time

def start_game(self, root):
    game_list = []
    new_game = Game(0,0,1,None)
    game_list.append(new_game)
    new_game.get_guess(root)
               
# G.U.I
root = Tk() # Initialises the window.
root.resizable(False, False) # Locks the window size to prevent re-sizing.
root.state('zoomed') # Makes the window fullscreen.
root.title("Howick College GeoGuesser V1.0")
root.configure(background='#FFFDD0') # Cream coloured background.
guess = StringVar()
guess_text_box = Entry(root, textvariable=guess, width=30, highlightbackground="black", highlightthickness="1", font=("Calibiri", "11")).place(x=830, y=917)
guess_text_box_label = Label(root, text="Location:", fg="black", bg="#FFFDD0",
                                font=("Calibri", "15", "bold")).place(x=748, y=910)
guess_btn = Button(root, text="Guess", borderwidth="2", width="13", bg='lime', fg='black',
                         font=("Calibri", "15", "bold"),command=lambda:start_game(root)).place(x=1100, y=900) # Guess button, calls the guess function.
reset_btn = Button(root, text="Reset", borderwidth="2", width="13", bg='red', fg='black',
                         font=("Calibri", "15", "bold"),command=lambda:reset(self, root)).place(x=600, y=900) # Reset button, calls the reset function.
quit_btn = Button(root, text="Quit", borderwidth="2", width="13", bg='red', fg='black',
                         font=("Calibri", "15", "bold"),command=lambda:quit(root)).place(x=450, y=900) # Quit button, calls the quit function.
how_to_play_frame = Frame(root, bg='white', width=430, height=714, highlightbackground="black", highlightthickness=5).place(x=1480, y=173) # Creates a frame (coloured box) for tidyness.
how_to_play_title = Label(root, fg="darkblue", bg='white', text="How to play?", font=("Calibri", "20", "bold", "underline")).place(x=1490, y=178)
how_to_play_text_l1 = Label(root, bg='white', text="- Type your guess in the text box 'location' undeneath the image.", font=("Calibri", "11", "bold")).place(x=1490, y=215)
how_to_play_text_l2 = Label(root, bg='white', text="- Ensure that you use correct grammer and clear guesses.", font=("Calibri", "11", "bold")).place(x=1490, y=250)
how_to_play_text_l3 = Label(root, bg='white', text="- Gather as many points as possible by guessing correctly!", font=("Calibri", "11", "bold")).place(x=1490, y=285)
how_to_play_text_l4 = Label(root, bg='white', text="- Get your best time! by guessing faster and faster as you play!", font=("Calibri", "11", "bold")).place(x=1490, y=320)              
title = Label(root, text="Howick College GeoGuesser", bg='#FFFDD0', fg='darkblue', font=("Calibri", "30", "bold", "underline")).place(x=740, y=100)
points_text = Label(root, bg='#FFFDD0', text="Points:", fg='darkblue', font=("Calibri", "20", "bold")).place(x=20, y=200)
best_time_text = Label(root, bg='#FFFDD0', text='Best Time:', fg='darkblue', font=("Calibri", "20", "bold")).place(x=20, y=250)
location_img = PhotoImage(file="location.png")
crest_img = PhotoImage(file="crest.png") # Imports the Howick College Crest
crest_label = Label(root, height=175, width=200, image=crest_img, bg='white').place(x=1700, y=700)
location_label = Label(root, height=700, width=1000, image=location_img, bg='white', highlightbackground="black", highlightthickness=5).place(anchor='center', x=960, y=530)
root.mainloop() # Keeps the window open.
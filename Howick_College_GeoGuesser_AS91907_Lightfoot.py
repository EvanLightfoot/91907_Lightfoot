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
        answer = answer.get()
        if self.guess == answer:
            self.points + 1
            self.game + 1
            try:
                incorrect.destroy()
            except NameError:
                correct = Label(root, text="Correct!", fg='lime', font=("Calibri", "15", "bold")).place(x=770, y=900)
        else:
            try:
                correct.destroy()
            except NameError:
                incorrect = Label(root, text="Incorrect!", fg='red', font=("Calibri", "15", "bold")).place(x=770, y=900)
        return self.points, self.game
        
def quit(root):
    root.destroy()
    
    def reset(self, root):
        self.points = 0
        self.game = 1
        self.time = 0
        return self.points, self.game, self.time
               
# G.U.I
root = Tk()
root.resizable(False, False)
root.state('zoomed')
root.title("Howick College GeoGuesser V1.0")
root.configure(background='cyan')
guess = StringVar()
guess_text_box = Entry(root, textvariable=guess, width=34, font=("Calibiri", "11")).place(x=770, y=917)
guess_text_box_label = Label(root, text="Location:", fg="black", bg="cyan",
                                font=("Calibri", "15", "bold")).place(x=750, y=910)
submit_btn = Button(root, text="Guess", borderwidth="5", width="13", bg='lime', fg='black',
                         font=("Calibri", "15", "bold"),command=lambda:get_guess(self, root)).place(x=1050, y=900)
reset_btn = Button(root, text="Reset", borderwidth="5", width="13", bg='lime', fg='black',
                         font=("Calibri", "15", "bold"),command=lambda:reset(self, root)).place(x=600, y=900)
quit_btn = Button(root, text="Quit", borderwidth="5", width="13", bg='lime', fg='black',
                         font=("Calibri", "15", "bold"),command=lambda:quit(root)).place(x=450, y=900)

how_to_play_frame = Frame(root, bg='cyan', width=430, height=714, highlightbackground="black", highlightthickness=5).place(x=1480, y=173)
how_to_play_title = Label(root, fg="darkblue", bg='cyan', text="How to play?", font=("Calibri", "20", "bold", "underline")).place(x=1490, y=178)
how_to_play_text = Label(root, bg='cyan', text="- Type your guess in the text box 'location' undeneath the image.\n\n Ensure the use of correct grammer and clear guesses.\n\n- Gather as many points as possible and try and get your best time!", 
                         font=("Calibri", "11", "bold")).place(x=1490, y=215)
title = Label(root, text="Howick College GeoGuesser", bg='cyan', fg='darkblue',
                         font=("Calibri", "30", "bold", "underline")).place(x=740, y=100)
location = PhotoImage(file="location.png")
location_label = Label(root, height=700, width=1000, image=location, bg='white', highlightbackground="black",
                       highlightthickness=5).place(anchor='center', x=960, y=530)
root.mainloop()
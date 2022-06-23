"""
* Write a python program that asks the user a minimum of 3 riddles.



* You can look at riddles.com if you don't already know any riddles.

* Collect the response of each riddle from the user and compare their
  answers to the correct answer. 


* Use a variable to keep track of the score
* After all the riddles have been asked, tell the user how many they got
  correct
"""
from tkinter import messagebox, simpledialog, Tk

window = Tk()
window.withdraw()

Penny = simpledialog.askstring(title='Riddle 1', prompt="What has a head and a tail, is brown, and has no limbs?")
score = 0
if Penny == 'Penny':
    messagebox.showinfo(title='great!', message="You get one point!")
    score+=1
else:
    messagebox.showinfo(title='Wrong!', message="No one said it would be easy :)")
    score-=1

David = simpledialog.askstring(title='Riddle 2', prompt= "David's father has three sons. Snap, Crackle, & ____")

if David == 'David':
    messagebox.showinfo(title='great!', message="You get one point!")
    score+=1
else:
    messagebox.showinfo(title='Wrong!', message="No one said it would be easy :)")
    score-=1

Footsteps = simpledialog.askstring(title='Riddle 3', prompt= "The more you take, the more you leave behind. What am I?")

if Footsteps == 'Footsteps':
    messagebox.showinfo(title='great!', message="You get one point!")
    score+=1
else:
    messagebox.showinfo(title='Wrong!', message="No one said it would be easy :)")
    score-=1


messagebox.showinfo(title='Results...', message=(score))

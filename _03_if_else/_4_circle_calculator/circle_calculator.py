import tkinter as tk
from tkinter import simpledialog, Tk
import math

window_width = 600
window_height = 600
# Write a Python program that asks the user for the radius of a circle.
# Next, ask the user if they would like to calculate the area or circumference of a circle.
# If they choose area, display the area of the circle using the radius.
# Otherwise, display the circumference of the circle using the radius.


window = Tk()
window.withdraw()

radius = simpledialog.askinteger(title='Make a circle!', prompt="Put in the amount of pixels you want for your circle")
answer = simpledialog.askstring(title='What do you want to calculate?', prompt="Do you want to find the Area or the Circumference?")
Area = math.pi*radius*radius
Circumference = math.pi*radius*2
if answer == "Area":
    canvas.create_circle(75, 200, 400, 450, fill="Area", outline="")
else:

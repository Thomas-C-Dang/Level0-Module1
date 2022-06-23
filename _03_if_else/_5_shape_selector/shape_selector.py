import turtle
import math
from tkinter import messagebox, simpledialog, Tk

# Goal: Write a Python program that asks the user whether they want to
#       draw a triangle, square, or circle and then draw that shape.

if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    
    # Make a new turtle
    Leonardo = turtle.Turtle()
    # Ask the user what shape they want to draw and store it in a variable
    shape = simpledialog.askstring(title='What shape?', prompt="What shape do you wanna draw? Trapezoid, square, or circle?")
    # Draw the shape requested by the user using if-elif-else statements
if shape == "Circle":
    Leonardo.circle(radius=60, steps=60)


if shape == "Square":
    for i in range(4):
        Leonardo.forward(100)
        Leonardo.left(90)
turtle.done()

if shape == "Trapezoid":
    for i in range(3):
        Leonardo.left(45)
        Leonardo.forward(100)

    Leonardo.left(135)
    Leonardo.forward(246)
turtle.done()



    # Call the turtle .done() method
turtle.done()

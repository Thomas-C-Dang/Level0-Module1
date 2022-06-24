"""
* Write a Python program that asks the user for two numbers.

* Then ask the user if the would like to add, subtract, multiply, or divide.

* Use if-else statements to provide the desired math operation on the numbers
  and display the result.
"""

from tkinter import messagebox, simpledialog, Tk
import math

window = Tk()
window.withdraw()

num1 = simpledialog.askinteger(title='enter the first number', prompt="What will the first number be?")
num2 = simpledialog.askinteger(title='enter the second number', prompt="What will the second number be?")
Operation = simpledialog.askstring(title='Operation?', prompt="Do you want to add, subtract, multiply or divide?")
Add = num1 + num2
Subtract = num1 - num2
Multiply = num1 * num2
Divide = num1/num2
if Operation == "Add":
    messagebox.showinfo(title='results', message=(Add))
if Operation == "Subtract":
    messagebox.showinfo(title='results', message=(Subtract))
if Operation == "Multiply":
    messagebox.showinfo(title='results', message=(Multiply))
if Operation == "Divide":
    messagebox.showinfo(title='results', message=(Divide))

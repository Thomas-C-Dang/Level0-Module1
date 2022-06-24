"""
* Write a Python program that asks the user for two numbers.

* Display the sum of the two numbers to the user
"""
from tkinter import messagebox, simpledialog, Tk
import math

window = Tk()
window.withdraw()

num1 = simpledialog.askinteger(title='enter the first number', prompt="What will the first number be?")
num2 = simpledialog.askinteger(title='enter the second number', prompt="What will the second number be?")
results = num1 + num2
messagebox.showinfo(title='results', message=(results))

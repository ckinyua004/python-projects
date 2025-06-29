# Miles to Kms converter using Tkinter
import tkinter as tk
from tkinter import Button, Label, Entry

def calculate_kilometers():
    miles = float(miles_input.get())
    kilometers = miles * 1.60934
    kilometer_result_label.config(text=f"{kilometers:.2f}")

window = tk.Tk()
window.title("Miles to Kms Converter")

miles_input = Entry(width=10)
miles_input.grid(column=1, row=0)
window.config(padx=20, pady=20)

miles_label = Label(text='miles')
miles_label.grid(column=2, row=0)

is_equal = Label(text='is equal to')
is_equal.grid(column=0, row=1)

kilometer_result_label = Label(text = 0)
kilometer_result_label.grid(column=1, row=1)

kilometer_label = Label(text='km')
kilometer_label.grid(column=2, row=1)

calculate_button = Button(text='Calculate', command=calculate_kilometers)
calculate_button.grid(column=1, row=2)

window.mainloop()
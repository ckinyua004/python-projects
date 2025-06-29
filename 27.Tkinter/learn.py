import tkinter

window = tkinter.Tk()
window.title("My First GUI")
window.geometry("400x300")

label = tkinter.Label(window, text="Hello, Tkinter!", font=("Arial", 24))
label.pack(pady=20)

def on_button_click():
    print("Button was clicked!")
button = tkinter.Button(window, text="Click Me", command=on_button_click)
button.pack()
button = tkinter.Button(window, text="Click Me", command=on_button_click).pack()

def greet():
    name = entry.get()
    label.config(text=f"Hello, {name}!")

    
entry = tkinter.Entry(window, font=("Arial", 16))
entry.pack()

greet_button = tkinter.Button(window, text="Greet", command=greet)
greet_button.pack(pady=10)
entry = tkinter.Entry(window, font=("Arial", 16)).pack()

greet_button = tkinter.Button(window, text="Greet", command=greet).pack(pady=10)
window.configure(bg="lightblue")

window.mainloop()
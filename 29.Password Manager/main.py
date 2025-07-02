from tkinter import *
from tkinter import messagebox
import json

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title='Oops', message='Please don’t leave any fields empty!')
    else:
        is_ok = messagebox.askokcancel(
            title=website,
            message=f"These are the details entered:\nEmail: {email}\nPassword: {password}\nWebsite: {website}\nIs it okay to save?"
        )
        if is_ok:
            new_data = {
                website: {
                    "email": email,
                    "password": password
                }
            }

            try:
                with open('data.json', 'r') as data_file:
                    # Read existing data
                    data = json.load(data_file)
            except FileNotFoundError:
                data = {}

            data.update(new_data)

            with open('data.json', 'w') as data_file:
                # Save updated data
                json.dump(data, data_file, indent=4)

            website_entry.delete(0, END)
            password_entry.delete(0, END)


def search_password():
    website = website_entry.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Not Found", message=f"No details for '{website}' found.")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Password Manager')
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file='./29.Password Manager/logo.png')  # Make sure the image path is correct
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text='Website:')
website_label.grid(row=1, column=0)
email_label = Label(text='Email/Username:')
email_label.grid(row=2, column=0)
password_label = Label(text='Password:')
password_label.grid(row=3, column=0)

# Entries
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()

search_button = Button(text='Search', width=13, command=search_password)
search_button.grid(row=1, column=2)


email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, 'example@gmail.com')

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

# Buttons
gen_pass = Button(text='Generate Password')  # Placeholder button
gen_pass.grid(row=3, column=2)

add_button = Button(text='Add', width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()

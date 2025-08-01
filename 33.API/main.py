from tkinter import *
import requests

def get_quote():
    """Fetch a random Kanye West quote from the API and update the canvas text."""
    try:
        response = requests.get('https://api.kanye.rest/')
        response.raise_for_status()
        data = response.json()
        quote = data['quote']
        canvas.itemconfig(quote_text, text=quote)
    except requests.RequestException as e:
        print(f"Error fetching quote: {e}")
        canvas.itemconfig(quote_text, text="Failed to fetch quote")

window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="./33.API/background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Kanye Quote Goes HERE", width=250, font=("Arial", 20, "italic"), fill="black")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file="./33.API/kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)



window.mainloop()
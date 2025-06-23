import pygame
import tkinter as tk
from tkinter import ttk

# Initialize Pygame mixer
pygame.mixer.init()

# Load a sound effect
sound_effect = pygame.mixer.Sound('thrust-sound-effect.wav')  # Provide path to your file

# Function to control the volume of the sound
def update_thrust(value):
    volume = int(value) / 100
    sound_effect.set_volume(volume)
    thrust_label.config(text=f"Thrust Level: {value}%")
    
    # Play the sound when the slider is active
    if volume > 0:
        if not pygame.mixer.get_busy():
            sound_effect.play(-1)  # Looping sound
    else:
        sound_effect.stop()

# Create a simple GUI with tkinter
root = tk.Tk()
root.title("Thrust Slider")

# Create a label
thrust_label = ttk.Label(root, text="Adjust the slider for thrust effect!", font=("Helvetica", 14))
thrust_label.pack(pady=20)

# Create a slider
thrust_slider = ttk.Scale(root, from_=0, to=100, orient="horizontal", command=update_thrust)
thrust_slider.set(0)
thrust_slider.pack(pady=10)

# Run the Tkinter GUI
root.mainloop()

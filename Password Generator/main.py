import random
import string
import tkinter as tk
from tkinter import Button, Label

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

# Create the main window
window = tk.Tk()
window.title("Password Generator")

# Set the window size
window.geometry("400x300")

# Create and configure widgets
generate_button = Button(window, text="Generate Password", command=lambda: password_label.config(text=generate_password()))
generate_button.pack(pady=20, padx=20)

password_label = Label(window, text="Generated Password: ", font=("Helvetica", 14))
password_label.pack(pady=20)

# Start the Tkinter event loop
window.mainloop()

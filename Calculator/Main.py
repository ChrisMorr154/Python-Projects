import tkinter as tk

# Function to update the display
def button_click(symbol):
    current = display_var.get()
    display_var.set(current + str(symbol))

# Function to clear the display
def clear_display():
    display_var.set("")

# Function to evaluate the expression and update the display
def calculate():
    try:
        result = eval(display_var.get())
        display_var.set(result)
    except Exception as e:
        display_var.set("Error")

# Create the main window
window = tk.Tk()
window.title("Simple Calculator")

# Set the window size
window.geometry("400x600")

# Entry widget for the display
display_var = tk.StringVar()
display_entry = tk.Entry(window, textvariable=display_var, font=("Helvetica", 24), justify="right")
display_entry.grid(row=0, column=0, columnspan=4)

# Buttons
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row_val = 1
col_val = 0

for button in buttons:
    tk.Button(window, text=button, padx=20, pady=20, font=("Helvetica", 18),
              command=lambda symbol=button: button_click(symbol) if symbol != '=' else calculate()).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Clear button
tk.Button(window, text="C", padx=20, pady=20, font=("Helvetica", 18), command=clear_display).grid(row=row_val, column=col_val, columnspan=4)

# Start the Tkinter event loop
window.mainloop()
import tkinter as tk

# Define pizza data
pizza_types = ['Margherita', 'Pepperoni', 'Vegetarian']
pizza_sizes = ['Small', 'Medium', 'Large']
pizza_prices = [
    [8.99, 10.99, 12.99],
    [9.99, 11.99, 13.99],
    [7.99, 9.99, 11.99]
]

def submit_order():
    pizza_type = pizza_type_var.get()
    pizza_size = pizza_size_var.get()
    quantity = int(quantity_var.get())

    # Check if selected pizza type and size are valid
    if pizza_type in pizza_types and pizza_size in pizza_sizes:
        # Get the price from the pizza_prices list
        price = pizza_prices[pizza_types.index(pizza_type)][pizza_sizes.index(pizza_size)]
        total_cost = price * quantity
        result_label.config(text=f"Total cost: ${total_cost:.2f}")
    else:
        result_label.config(text="Invalid pizza type or size")

app = tk.Tk()
app.title("Pizza Order App")

# Initialize variables
pizza_type_var = tk.StringVar()
pizza_size_var = tk.StringVar()
quantity_var = tk.StringVar()

# Create GUI elements
tk.Label(app, text="Choose a pizza type:").grid(row=0, column=0)
tk.OptionMenu(app, pizza_type_var, *pizza_types).grid(row=0, column=1)
tk.Label(app, text="Choose a pizza size:").grid(row=1, column=0)
tk.OptionMenu(app, pizza_size_var, *pizza_sizes).grid(row=1, column=1)
tk.Label(app, text="Enter quantity:").grid(row=2, column=0)
tk.Entry(app, textvariable=quantity_var).grid(row=2, column=1)
tk.Button(app, text="Submit Order", command=submit_order).grid(row=3, column=0, columnspan=2)
result_label = tk.Label(app, text="")
result_label.grid(row=4, column=0, columnspan=2)

app.mainloop()

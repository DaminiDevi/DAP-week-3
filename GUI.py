import tkinter as tk

# Function to update entry field
def press(value):
    entry_var.set(entry_var.get() + str(value))

# Function to evaluate expression
def calculate():
    try:
        result = eval(entry_var.get())  # Evaluates the expression
        entry_var.set(result)  # Displays result
    except:
        entry_var.set("Error")  # Error handling

# Function to clear the entry
def clear():
    entry_var.set("")

# GUI setup
root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")

# Entry widget
entry_var = tk.StringVar()
entry = tk.Entry(root, textvariable=entry_var, font=("Arial", 20), bd=10, relief="ridge", justify="right")
entry.pack(fill="both", padx=10, pady=10)

# Button layout
buttons = [
    ('7', '8', '9', '/'),
    ('4', '5', '6', '*'),
    ('1', '2', '3', '-'),
    ('C', '0', '=', '+')
]

# Button grid
for row in buttons:
    frame = tk.Frame(root)
    frame.pack(expand=True, fill="both")
    for char in row:
        if char == "=":
            btn = tk.Button(frame, text=char, font=("Arial", 18), command=calculate, height=2, width=5)
        elif char == "C":
            btn = tk.Button(frame, text=char, font=("Arial", 18), command=clear, height=2, width=5)
        else:
            btn = tk.Button(frame, text=char, font=("Arial", 18), command=lambda ch=char: press(ch), height=2, width=5)
        btn.pack(side="left", expand=True, fill="both")

root.mainloop()

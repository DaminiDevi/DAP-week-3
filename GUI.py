import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")
        self.root.geometry("300x400")
        
        self.expression = ""
        
        # Entry widget for displaying the expression
        self.entry = tk.Entry(root, font=("Arial", 20), bd=10, relief="ridge", justify="right")
        self.entry.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=8)

        # Buttons for calculator
        buttons = [
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
            ("C", 4, 0), ("0", 4, 1), ("=", 4, 2), ("+", 4, 3)
        ]

        for text, row, col in buttons:
            self.create_button(text, row, col)

    def create_button(self, text, row, col):
        btn = tk.Button(self.root, text=text, font=("Arial", 18), padx=20, pady=20, command=lambda: self.on_button_click(text))
        btn.grid(row=row, column=col, sticky="nsew")

    def on_button_click(self, char):
        if char == "=":
            try:
                self.expression = str(eval(self.expression))  # Evaluate the expression
            except:
                self.expression = "Error"  # Handle errors
        elif char == "C":
            self.expression = ""  # Clear the entry field
        else:
            self.expression += char  # Append the pressed button to the expression
        
        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, self.expression)

# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    Calculator(root)
    root.mainloop()

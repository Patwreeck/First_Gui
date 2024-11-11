import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("PATWRECK CALCULATOR")
        self.root.geometry("400x600")
        self.root.configure(bg="#f2f2f2")

        self.expression = ""

        # Entry widget to display the expression
        self.entry = tk.Entry(root, font=('Arial', 32), bd=10, insertwidth=4, width=14, borderwidth=4, justify='right')
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        # Creating buttons
        self.create_buttons()

    def create_buttons(self):
        button_style = {
            'padx': 20,
            'pady': 20,
            'font': ('Arial', 18),
            'relief': 'raised',
            'borderwidth': 2,
            'highlightbackground': '#f2f2f2'
        }

        buttons = [
            ('C', 1, 0, '#ff3b30'), ('/', 1, 1, '#ff9500'), ('*', 1, 2, '#ffcc00'), ('-', 1, 3, '#007aff'),
            ('7', 2, 0, '#808080'), ('8', 2, 1, '#808080'), ('9', 2, 2, '#808080'), ('+', 2, 3, '#007aff'),
            ('4', 3, 0, '#808080'), ('5', 3, 1, '#808080'), ('6', 3, 2, '#808080'), ('=', 3, 3, '#007aff'),
            ('1', 4, 0, '#808080'), ('2', 4, 1, '#808080'), ('3', 4, 2, '#808080'), ('0', 5, 1, '#808080'),
            ('.', 5, 0, '#808080'),
        ]

        for (text, row, col, color) in buttons:
            button = tk.Button(self.root, text=text, command=lambda b=text: self.on_button_click(b),
                               bg=color, fg='#ffffff', **button_style)
            if text == "=":
                button.grid(row=row, column=col, rowspan=2, sticky='nsew')
            elif text == "0":
                button.grid(row=row, column=col, columnspan=3, sticky='nsew')
            else:
                button.grid(row=row, column=col, sticky='nsew')


        # Configure grid weights for responsive layout
        for i in range(6):
            self.root.grid_rowconfigure(i, weight=1)
            self.root.grid_columnconfigure(i, weight=1)

    def on_button_click(self, button):
        if button == 'C':
            self.clear()
        elif button == '=':
            self.calculate()
        else:
            self.expression += button
            self.update_entry()

    def calculate(self):
        try:
            result = str(eval(self.expression))
            self.entry.delete(0, tk.END)
            self.entry.insert(0, result)
            self.expression = result
        except Exception as e:
            self.entry.delete(0, tk.END)
            self.entry.insert(0, "Error")
            self.expression = ""

    def clear(self):
        self.expression = ""
        self.update_entry()

    def update_entry(self):
        self.entry.delete(0, tk.END)
        self.entry.insert(0, self.expression)

if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()
#import tkinter  as tk
from tkinter import *
import tkinter  as tk

class SimpleCalculator(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Simple Calculator")

        self.tf = tk.Entry(self, width=16, font=('Arial', 14))
        self.tf.grid(row=0, column=0, columnspan=4)

        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            'C', '0', '=', '+'
        ]

        row_val = 1
        col_val = 0

        for button in buttons:
            tk.Button(self, text=button, padx=10, pady=10, font=('Arial', 14),
                      command=lambda btn=button: self.button_click(btn)).grid(row=row_val, column=col_val)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

    def button_click(self, value):
        current_text = self.tf.get()
        if value == 'C':
            self.tf.delete(0, tk.END)
        elif value == '=':
            try:
                result = eval(current_text)
                self.tf.delete(0, tk.END)
                self.tf.insert(0, result)
            except Exception as e:
                self.tf.delete(0, tk.END)
                self.tf.insert(0, "Error")
        else:
            self.tf.insert(tk.END, value)

if __name__ == '__main__':
    calc = SimpleCalculator()
    calc.mainloop()
import tkinter as tk

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        root.title("Simple Calculator")

        self.result_var = tk.StringVar()

        self.entry = tk.Entry(root, textvariable=self.result_var, font=('Arial', 20), justify='right')
        self.entry.grid(row=0, column=0, columnspan=4)
        
        button_texts = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', 'C', '=', '+'
        ]

        row, col = 1, 0
        for text in button_texts:
            tk.Button(root, text=text, width=6, height=2, command=lambda t=text: self.button_click(t)).grid(row=row, column=col)
            col += 1
            if col > 3:
                col = 0
                row += 1

    def button_click(self, text):
        if text == '=':
            try:
                result = str(eval(self.result_var.get()))
                self.result_var.set(result)
            except:
                self.result_var.set("Error")
        elif text == 'C':
            self.result_var.set('')
        else:
            current_text = self.result_var.get()
            self.result_var.set(current_text + text)

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()

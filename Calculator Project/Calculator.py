import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        
        self.expression = ""
        self.current_text = tk.StringVar()  # Variable to hold the current input/display value

        # Creating the display entry widget
        self.display = tk.Entry(root, font=('Arial', 20, 'bold'), textvariable=self.current_text, bd=30, insertwidth=4, bg="powder blue", justify='right')
        self.display.grid(row=0, column=0, columnspan=4)

        # Creating buttons for calculator operations and digits
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]

        # Grid positions for the buttons
        row_val = 1
        col_val = 0

        # Creating buttons in a grid layout
        for button_text in buttons:
            self.create_button(button_text, row_val, col_val)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

        # Creating a clear button
        clear_button = tk.Button(root, text='C', padx=20, pady=20, bd=8, fg="black", font=('Arial', 20, 'bold'),
                                 command=self.clear_display)
        clear_button.grid(row=row_val, column=0, columnspan=4)

    def create_button(self, text, row, col):
        """
        Create a calculator button with specified text and grid position.
        :param text: Text to display on the button
        :param row: Row position in the grid
        :param col: Column position in the grid
        """
        return tk.Button(self.root, text=text, padx=20, pady=20, bd=8, fg="black", font=('Arial', 20, 'bold'),
                         command=lambda: self.button_click(text)).grid(row=row, column=col)

    
    
       # Handle button clicks and update the calculator display
        
    def button_click(self, value):
        if value == "=":
            result = self.evaluate_expression()
            self.current_text.set(result)
        elif value == "C":
            self.clear_display()
        else:
            self.expression += value
            self.current_text.set(self.expression)

            
    def evaluate_expression(self):
        try:
            result = str(eval(self.expression))
            self.expression = result
            return result
        except ZeroDivisionError:
            self.expression = ""
            return "Error: Division by zero"
        except:
            self.expression = ""
            return "Error"        

    def clear_display(self):
        """
        Clear the calculator display and reset the expression.
        """
        self.expression = ""
        self.current_text.set("")

if __name__ == "__main__":
    root = tk.Tk()
    Calculator(root)
    root.mainloop()
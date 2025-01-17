from tkinter import *

# Create the main window
window = Tk()
window.title("The Calculator")
window.configure(bg="#6247aa")

expression = ""
operator_used = False
open_parentheses = 0

# Add a character to the current expression
def stepOne(character):
    global expression, operator_used, open_parentheses
    if character in "+-*/" and operator_used:
        return
    if character in "+-*/":
        operator_used = True
    elif character == "(":
        open_parentheses += 1
    elif character == ")":
        if open_parentheses > 0:
            open_parentheses -= 1
        else:
            return
    else:
        operator_used = False
    expression += str(character)
    input_text.set(expression)

# Clear the expression
def stepTwo():
    global expression, operator_used, open_parentheses
    expression = ""
    operator_used = False
    open_parentheses = 0
    input_text.set(expression)

# Backspace button
def stepThree():
    global expression, operator_used, open_parentheses
    if expression:
        if expression[-1] in "+-*/":
            operator_used = False
        elif expression[-1] == "(":
            open_parentheses -= 1
        elif expression[-1] == ")":
            open_parentheses += 1
        expression = expression[:-1]
        input_text.set(expression)

# Calculate the expression
def stepFour():
    global expression, operator_used, open_parentheses
    try:
        if open_parentheses != 0:
            raise ValueError("Error")
        result = str(eval(expression))
        input_text.set(result)
        expression = result
        operator_used = False
    except:
        input_text.set("Error")
        expression = ""

# Configure the input field
input_text = StringVar()
input_field = Entry(window, textvariable=input_text, font=("Lato", 20), justify="right", bd=0, bg="#6247aa", fg="white")
input_field.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=20, sticky="nsew")

# Button configuration
buttons = [
    ('C', 1, 0, "#7251b5"), ('⌫', 1, 1, "#815ac0"), ('(', 1, 2, "#815ac0"), (')', 1, 3, "#815ac0"),
    ('7', 2, 0, "#9163cb"), ('8', 2, 1, "#9163cb"), ('9', 2, 2, "#9163cb"), ('/', 2, 3, "#815ac0"),
    ('4', 3, 0, "#9163cb"), ('5', 3, 1, "#9163cb"), ('6', 3, 2, "#9163cb"), ('*', 3, 3, "#815ac0"),
    ('1', 4, 0, "#9163cb"), ('2', 4, 1, "#9163cb"), ('3', 4, 2, "#9163cb"), ('-', 4, 3, "#815ac0"),
    ('0', 5, 0, "#9163cb"), ('.', 5, 1, "#9163cb"), ('=', 5, 2, "#7251b5"), ('+', 5, 3, "#815ac0")
]

for (text, row, col, color, *span) in buttons:
    Button(
        window,
        text=text,
        width=5,
        height=2,
        bg=color,
        fg="white",
        font=("Lato", 18, "bold"),
        bd=0,
        command=(
            lambda t=text: stepOne(t) if t not in {'C', '=', '⌫'} else (
                stepTwo() if t == 'C' else (stepFour() if t == '=' else stepThree())
            )
        )
    ).grid(row=row, column=col, columnspan=span[0] if span else 1, sticky="nsew")

# Adjust the grid weights for responsive design
for i in range(7):
    window.rowconfigure(i, weight=1)
    window.columnconfigure(i, weight=1)

window.mainloop()

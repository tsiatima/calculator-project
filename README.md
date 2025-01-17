# The Calculator

## Description
This is a simple graphical calculator built using Python's Tkinter library. It provides basic arithmetic operations and supports parentheses for more complex calculations. The calculator features a modern design with customizable colors and responsive layout.

## Features
- Supports basic arithmetic operations: addition, subtraction, multiplication, and division.
- Includes buttons for parentheses `(` and `)` to handle complex expressions.
- Backspace functionality to remove the last entered character.
- Clear button (`C`) to reset the current expression.
- Displays error messages for invalid input or unbalanced parentheses.
- Modern design with responsive layout and custom color scheme.

## Requirements
- Python 3.6 or later
- Tkinter (usually included with Python installations)

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/tsiatima/the-calculator.git
   ```
2. Navigate to the project directory:
   ```bash
   cd the-calculator
   ```
3. Run the script:
   ```bash
   python calculator.py
   ```

## How to Use
1. Launch the calculator by running the script.
2. Use the on-screen buttons to input numbers and operations:
   - Numbers: `0-9`
   - Operations: `+`, `-`, `*`, `/`
   - Parentheses: `(`, `)`
   - Clear: `C`
   - Backspace: `⌫`
   - Decimal point: `.`
3. Press the `=` button to calculate the result of the expression.
4. If an error occurs (e.g., unbalanced parentheses or invalid input), the display will show `Error`.

## Code Overview
The code consists of the following key components:

### 1. Main Window
The main window is created using the Tkinter `Tk` class and configured with a custom background color and responsive grid layout.

### 2. Input Field
An input field (`Entry`) displays the current expression or result. It is updated dynamically as buttons are pressed.

### 3. Buttons
Buttons are created dynamically with custom labels, colors, and commands. Each button is mapped to a specific function:
- `stepOne(character)`: Adds a character to the current expression.
- `stepTwo()`: Clears the current expression.
- `stepThree()`: Deletes the last entered character.
- `stepFour()`: Evaluates the expression and displays the result.

### 4. Responsive Design
The grid layout dynamically adjusts to fit the window size, ensuring a consistent user experience across different screen sizes.

## Customization
- **Colors:** Button and background colors can be customized by modifying the `bg` and `fg` parameters in the button configuration.
- **Font:** The font style and size can be updated by changing the `font` parameter.

## Example Output
```
Expression: (7+8)*2
Result: 30
```

## License
This project is licensed under the MIT License. Feel free to use and modify it as needed.

## Contributing
Contributions are welcome! If you encounter any issues or have feature requests, please open an issue or submit a pull request.

## Contact
For questions or feedback, contact me or open an issue on the GitHub repository.


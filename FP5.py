import random

# ANSI color codes
colors = {
    "red": "\033[31m",
    "green": "\033[32m",
    "yellow": "\033[33m",
    "blue": "\033[34m",
    "brown": "\033[33;5;94m",  # Brown variant
    "reset": "\033[0m"  # Reset color
}

def redText(text):
    return f"{colors['red']}{text}{colors['reset']}"

def greenText(text):
    return f"{colors['green']}{text}{colors['reset']}"

def yellowText(text):
    return f"{colors['yellow']}{text}{colors['reset']}"

def blueText(text):
    return f"{colors['blue']}{text}{colors['reset']}"

def brownText(text):
    return f"{colors['brown']}{text}{colors['reset']}"

def randomColorText(text):
    color_func = random.choice([redText, greenText, yellowText, blueText, brownText])
    return color_func(text)

def main():
    # Call each function and print example texts
    print(redText("This is red text."))
    print(greenText("This is green text."))
    print(yellowText("This is yellow text."))
    print(blueText("This is blue text."))
    print(brownText("This is brown text."))
    
    while True:
        # User input for color choice
        user_color = input("Choose a color (red, green, yellow, blue, brown) or 'random' for random color (or 'exit' to quit): ").strip().lower()
        
        if user_color == "exit":
            print("Goodbye!")
            break
        
        text_input = input("Enter the text you want to display: ")
        
        if user_color in colors:
            # Call the appropriate color function
            if user_color == "random":
                colored_text = randomColorText(text_input)
            else:
                color_function = globals()[f"{user_color}Text"]
                colored_text = color_function(text_input)
            
            print(colored_text)
        else:
            print("Invalid color choice. Please try again.")

# Start the program
main()
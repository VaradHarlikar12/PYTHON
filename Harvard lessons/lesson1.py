print("Hello")                         # Prints something on the screen
name = input("Name: ")                 # Takes input from the user
print(name)                            # Prints the variable
name = "Varad"                         # Stores a string in a variable
age = 20                               # Stores an integer
price = 99.99                          # Stores a decimal (float)
print("Hello,", name)                  # Prints multiple values
print("Hello", end=" ")                # Prevents print from moving to a new line
print("Hello\nWorld")                  # \n creates a new line
print("He said \"Hi\"")                # \" prints quotation marks
print(f"Hello, {name}")                # f-string inserts a variable into a string
name = name.strip()                    # Removes spaces from beginning/end
name = name.capitalize()               # Capitalizes first letter
name = name.title()                    # Capitalizes first letter of each word
name = name.upper()                    # Converts string to uppercase
name = name.lower()                    # Converts string to lowercase
first, last = name.split(" ")          # Splits a string into two variables
x = int(input("x: "))                  # Gets input and converts it to integer
x = float(input("x: "))                # Gets input and converts it to decimal
x + y                                  # Addition
x - y                                  # Subtraction
x * y                                  # Multiplication
x / y                                  # Division
x // y                                 # Floor division
x % y                                  # Remainder
x ** y                                 # Power/exponent
round(x)                               # Rounds a number
round(x, 2)                            # Rounds to 2 decimal places
print(f"{x:.2f}")                      # Displays number with 2 decimal places

def hello():                           # Creates a function
    print("Hello")                     # Code inside the function

hello()                                # Calls/runs the function

def hello(name):                       # Function with a parameter
    print("Hello,", name)              # Uses the parameter

hello("Varad")                         # Calls function and gives it an argument

def hello(name="World"):               # Function with a default parameter
    print("Hello,", name)              # Uses default if no argument is given

def square(x):                         # Creates a function to square a number
    return x * x                       # Returns the result

answer = square(5)                     # Stores returned value
print(answer)                          # Prints 25

def main():                            # Creates the main function
    name = input("Name: ")             # Gets user's name

main()                                 # Starts the main function

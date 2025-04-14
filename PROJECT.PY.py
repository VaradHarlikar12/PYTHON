#number of uppeprcase and lowercase

import random
import string

def password_generator():
    letters = list(string.ascii_lowercase)
    letters2=list(string.ascii_uppercase)
    numbers = list(string.digits)
    symbols = list(string.punctuation)

    print("Welcome to Password Generator")
    pass_len=int(input("Enter an password length:"))
    n_letters = int(input("How Many number of lowercase letters:"))
    n_letter2 = int(input("How Many number of uppercase letters:"))
    n_numbers = int(input("How Many number of NUMBERS:"))
    n_symbols = int(input("How Many number of SYMBOLS:"))                                                            

    password_list = []
    # Check if total characters match the desired password length
    total_chars = n_letters + n_letter2 + n_numbers + n_symbols
    #Error if total>length given by user
    if total_chars > pass_len:
        print("Error: The total number of characters does not match the required password length.")
        return
    # Stop execution if the input is incorrect
    # made it list so that we can shuffle them
    # (added +1 so that it can print from 1 to given no +1 as it will count one less as per the rules)

    # FOR LOOP for letters
    for i in range(1, n_letters + 1):
        char = random.choice(letters)
        password_list += char

    # FOR LOOP for letters
    for i in range(1, n_letter2 + 1):
        char = random.choice(letters2)
        password_list += char

    # FOR LOOP for symbol
    for i in range(1, n_symbols + 1):
        char = random.choice(symbols)
        password_list += char

    # FOR LOOP for numbers
    for i in range(1, n_numbers + 1):
        char = random.choice(numbers)
        password_list += char
    # SHUFFLING THE LIST
    random.shuffle(password_list)
    # MAKING/CONVERTING LIST INTO STRING
    # The "" (empty string) acts as a separator, meaning the characters are joined with nothing in between
    password = "".join(password_list)
    print(f"Your generated password is: {password} ")  # Display password
    #print(password_list)


    # for char in password_list:
    #    password+=char
    # print(password)

password_generator()

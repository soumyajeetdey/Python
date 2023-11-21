###############################################################################

# write a program to capture any string from the keyboard and perform the below

# if the string is defined in uppercase......   convert the string to lower and display it

# if the string is defined in lowercase ...... convert the string to upper and displat it.

###############################################################################

# Input: Ask the user for a string
user_input = input("Enter a string: ")

# Check if the input is in uppercase
if user_input.isupper():
    # If it's in uppercase, convert it to lowercase
    converted_string = user_input.lower()
    print(f"The converted string is: {converted_string}")
elif user_input.islower():
    # If it's in lowercase, convert it to uppercase
    converted_string = user_input.upper()
    print(f"The converted string is: {converted_string}")
else:
    # If it's mixed case or contains non-alphabetic characters, leave it as is
    print("The string remains unchanged:", user_input)
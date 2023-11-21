# write a program to read filename as input from the keyboard and display the below output

import os

# Input: Ask the user for a filename
filename = input("Enter any filename: ")

# Split the filename into the base name and extension
base_name, extension = os.path.splitext(filename)

# Display the results
print(f"Filename: {base_name}")
print(f"Extension: {extension.lstrip('.')}")
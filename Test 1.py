# write a progam to capture filename from the keyboard and display the type of the file

import os
    
# Input: Ask the user for a filename
filename = input("Enter the filename: ")

# Extract the file extension
file_extension = os.path.splitext(filename)[1]

# Dictionary mapping common file extensions to their types
file_type_mapping = {
    ".txt": "Text File",
    ".jpg": "JPEG Image",
    ".png": "PNG Image",
    ".pdf": "PDF Document",
    ".mp3": "MP3 Audio",
    ".mp4": "MP4 Video",
    ".py": "Python Script",
    # Add more file types and extensions as needed
}

# Determine the file type based on the extension
file_type = file_type_mapping.get(file_extension, "Unknown File Type")

# Display the result
print(f"The file '{filename}' is a {file_type}")

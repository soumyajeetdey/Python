'''
###################################################################################

write a program to display the below information

1) current working directory   
2) login name
3) current process id
4) current python version
5) all the libraries available in python
6) all the environment variables
7) operating system name
8) platform name
9)current date and time
10)statistics of adult.csv file   ( display accessed tile , modified time, filesize )
11)create empty file with today's timestamp	  ( Eg: 21_Sep_2023.csv )


######################################################################
'''

import os
import platform
import getpass
import sys
import datetime
import csv
import time

# 1) Current Working Directory
current_directory = os.getcwd()
print("1) Current Working Directory:", current_directory)

# 2) Login Name
login_name = getpass.getuser()
print("2) Login Name:", login_name)

# 3) Current Process ID
process_id = os.getpid()
print("3) Current Process ID:", process_id)

# 4) Current Python Version
python_version = sys.version
print("4) Current Python Version:", python_version)

# 5) All Installed Libraries in Python
installed_libraries = [module for module in sys.modules if module]
print("5) All Libraries Available in Python:")
for lib in installed_libraries:
    print(lib)

# 6) All Environment Variables
environment_variables = os.environ
print("6) All Environment Variables:")
for key, value in environment_variables.items():
    print(f"{key}: {value}")

# 7) Operating System Name
os_name = platform.system()
print("7) Operating System Name:", os_name)

# 8) Platform Name
platform_name = platform.platform()
print("8) Platform Name:", platform_name)

# 9) Current Date and Time
current_datetime = datetime.datetime.now()
print("9) Current Date and Time:", current_datetime)

# 10) Statistics of adult.csv File
file_path = "adult.csv"  # Replace with the actual path to your CSV file
if os.path.exists(file_path):
    file_stats = os.stat(file_path)
    accessed_time = time.ctime(file_stats.st_atime)
    modified_time = time.ctime(file_stats.st_mtime)
    file_size = file_stats.st_size
    print("10) Statistics of adult.csv File:")
    print("    Accessed Time:", accessed_time)
    print("    Modified Time:", modified_time)
    print("    File Size:", file_size, "bytes")
else:
    print("10) adult.csv file not found.")

# 11) Create Empty File with Today's Timestamp
timestamp = datetime.datetime.now().strftime("%d_%b_%Y")
empty_file_name = f"{timestamp}.csv"
with open(empty_file_name, "w") as empty_file:
    pass
print(f"11) Created empty file: {empty_file_name}")

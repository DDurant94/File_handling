'''
1. Exploring Python's OS Module
Objective:
The goal of this assignment is to deepen your understanding of the OS module in Python. 
You will engage in tasks that involve file and directory operations, path manipulations, 
and practical applications of these operations in real-world scenarios.

Task 1: Directory Inspector:

Problem Statement:
Create a Python script that lists all files and subdirectories in a given directory. 
Your script should prompt the user for the directory path and then display the contents.

Code Example:
import os

def list_directory_contents(path):
    # List and print all files and subdirectories in the given path
Expected Outcome:
The script should correctly list all files and subdirectories in the specified directory. 
Handle exceptions for invalid paths or inaccessible directories.


Task 2: File Size Reporter:
Problem Statement:
Write a Python program that reports the sizes of all files in a specific directory. 
The program should ask the user for a directory path and then print each file's name and size within that directory.

Code Example:
def report_file_sizes(directory):
    # Iterate through files in the directory and print their names and sizes
Expected Outcome:
Your program should display the name and size (in bytes) of each file in the given directory. 
Ensure that the program only reports on files, not directories, and handles any errors gracefully.
Task 3: File Extension Counter:

Problem Statement:
Develop a Python script that counts the number of files of each extension type in a directory. 
For instance, in a directory with five '.txt' files and three '.py' files, the script should report "TXT: 5" and "PY: 3".

Code Example:
def count_file_extensions(directory):
    # Count and print the number of files of each extension type in the directory
Expected Outcome:
The script should accurately count and display the number of files for each extension type in the specified directory. 
Handle different cases of file extensions (e.g., '.TXT' and '.txt' should be considered the same).
'''
# Task one - Task three
import os
import re

def sorting_files(file):
  categories_to_sort = {"Text File":r"\b(\.TXT|\.txt)\b",
                        "Image File":r"\b(\.JPG|\.jpg)\b",
                        }
  for category,sorting_code in  categories_to_sort.items():
    #take our regex sort to see if we have a match and if we do we return that category 
    if re.search(sorting_code,file,re.IGNORECASE):
      return category
  return "Directories"


def list_directory_contents(path):
  file_list = []
  try:
    directory_list = os.listdir(path)
    for file in directory_list:
       file_list.append(file)
    return file_list
  except FileNotFoundError as e:
     print(f"Error: {e} That file doesn't exist")


def make_directory(directory):
  try:
      os.makedirs(directory, exist_ok= True)
      print(f"Directory '{directory}' was created")
  except FileExistsError as e:
    print(f"Error: {e} choose a different name")


def report_file_sizes(path):
  try:
    # Could use os.stat() to get all the stats about the file we are choosing
    file_size = os.path.getsize(path)
    print(f"The size of '{path}' is {file_size} bytes")
  except PermissionError:
     print("This file Doesn't exist choose another file")
  except FileNotFoundError as e:
     print(f"Error: {e} That file doesn't exist")


def count_file_extensions(path):
   try:
      organized_files = {"Text File":[], "Image File":[], "Directories":[]}
      list_of_files = list_directory_contents(path)
      for file in list_of_files:
        category_sorted = sorting_files(file)
        organized_files[category_sorted].append(file)
      print(f"File Count in Directory '{path}': Text Files: {len(organized_files['Text File'])}, Image Files: {len(organized_files['Image File'])}, Directories: {len(organized_files['Directories'])}")

         
   except:
      pass


def main():
  how_to = "[Directory Name]/[Sub-Directory Name]"
  print("Welcome to the Directory Maker")
  while True:
    print("\nMain Menu:\n1. Make a Directory\n2. View Directory\n3. File Size\n4. File Counter\n5. Exit")
    user_menu_input = input("Please select one of our menu options: ")
    if user_menu_input == "1":
        print(f"Note:\nTo make Sub-Directories {how_to}:\n")
        directory = input("Name directory you want to make: ")
        make_directory(directory)
    elif user_menu_input == "2":
        print(f"Note:\nTo open Sub-Directories {how_to}:\n")
        path = input("What Directory do you want to open: ")
        print(list_directory_contents(path))
    elif user_menu_input == "3":
        print(f"Note:\nTo get the size of a Directories or file {how_to}/File Name]:\n")
        path = input("What file or directory would you like to get to get a size of in bytes: ")
        report_file_sizes(path)
    elif user_menu_input == "4":
        print(f"{how_to}")
        path = input("What Directory would you like to use: ")
        count_file_extensions(path)
    elif user_menu_input == "5":
      print("Thank you for using our program!")
      break
    else:
      print("Invalid input")

main()
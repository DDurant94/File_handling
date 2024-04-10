'''
2. Regex-Powered Text Data Processing
Objective:
The purpose of this assignment is to harness the power of regular expressions (regex) in Python for advanced text data processing. 
You will apply regex to extract, manipulate, and analyze data from text files, combining it with efficient file handling techniques.

Task 1: Email Extractor:

Problem Statement:
Write a Python script to extract all email addresses from a given text file (contacts.txt). The file contains a mix of text and email addresses.

File Example:
Contact List:

John Doe - john.doe@example.com
Jane Smith - jane.smith@gmail.com

For inquiries, please contact info@example.com
Code Example:
import re

def extract_emails(filename):
    # Read the file and use regex to find and return all email addresses
Expected Outcome:
The script should output a list of all unique email addresses found in the file. Utilize regex to accurately 
identify email addresses amidst other text.
'''

#question_two\\contacts.txt is the folder that the information for this is stored


# make a regex to find emails and extract them from text
# be able to read the file as well 
# extra make it to where i can edit the file return it 
import re

def read_contacts(filename):
    try:
        with open(filename, 'r') as file:
            file_contents = file.readlines()
            file_rewrite = []
            for line in file_contents:
                rework = line.strip().split('-')
                file_rewrite.append(rework)
            return file_rewrite
    except FileNotFoundError:
        print("File not found")


def extract_emails(contacts):
    found_emails = []
    email_pattern = r"(\b\w+\@{1}\w+\.{1}\w{2,3}\b)"
    for data in contacts:
        for info in data:
            email_search = re.search(email_pattern,info)
            if email_search:
                found_emails.append(info)
    return found_emails

def view_file(contacts):
    for info in contacts:
        print(f"Name: {info[0]} Email: {info[1]}")      



def main():
  contacts_list = read_contacts('question_two\\contacts.txt')
  print("Welcome:")
  while True:
    print("\nMain Menu:\n1. Extract Emails\n2. View File\n3. Exit")
    user_menu_input = input("Please select one of our menu options: ")
    if user_menu_input == "1":
        print(extract_emails(contacts_list))
    elif user_menu_input == "2":
        view_file(contacts_list)
    elif user_menu_input == "3":
        print("Thank you for using our program!")
        break
    else:
      print("Invalid input")

main()
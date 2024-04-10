'''
3. Advanced Python Data Processing and Analysis Challenge
Objective:
This assignment is aimed at challenging your skills in advanced data processing and analysis using Python. 
It encompasses a broad range of topics, including file handling, regular expressions, data structures, and 
complex problem-solving, at a medium-hard difficulty level.

Task 1: Travel Blog Sentiment Analysis:

Problem Statement:
Perform sentiment analysis on a collection of travel blog entries stored in travel_blogs.txt. Identify and 
count the occurrences of positive words (e.g., "amazing", "enjoy", "beautiful") and negative words (e.g., "bad", "disappointing", "poor").
- Dataset Example:
Travel Blog Entries:


Code Example:
def analyze_blog_sentiments(blog_file):
    # Implement sentiment analysis logic on the blog file
Expected Outcome:
A summary report indicating the number of positive and negative words in the travel blogs, 
demonstrating the ability to process text data and apply basic sentiment analysis.

Task 2: Historical Weather Data Compiler

Problem Statement:
Compile and analyze historical weather data from multiple files (weather_2020.txt, weather_2021.txt, etc.). 
Each file contains daily temperature data. Calculate the average temperature for each year and identify the year with the highest average.

- Dataset Example:
File: weather_2020.txt

File: weather_2021.txt



Code Example:
def compile_weather_data(file_list):
    # Aggregate temperature data and calculate the yearly averages
Expected Outcome:
An aggregated view of average temperatures for each year and identification of the year with the highest average temperature, 
showcasing data aggregation and analysis skills
'''

# Task one
import re
import os
def read_file(filename):
    try:
        with open(filename, 'r') as file:
            working_file = file.readlines()
            return working_file
    except FileNotFoundError:
        print("File not found")


def search_keys(review):
    keys = {"Positive": r"amazing|wonderful|fantastic|enlightening",
           "Negative": r"bad|terrible|lackluster|poor|disappointing"
           }
    for category, code in keys.items():
        sorting_reviews = re.search(code,review)
        if sorting_reviews:
            return category
    return "Neutral"


def review_count(file):
    reviews = {"Positive": [], "Negative": [], "Neutral": []}
    for review in file:
        matching = search_keys(review)
        reviews[matching].append(review)
        
    for category, feedback in reviews.items():
       print(f"{category} Reviews: {len(feedback)}")


def main():
  file_list = read_file('question_three\\reviews.txt')
  print("Welcome:")
  while True:
    print("\nMain Menu:\n1. Review Count\n2. Exit")
    user_menu_input = input("Please select one of our menu options: ")
    if user_menu_input == "1":
        review_count(file_list)
    elif user_menu_input == "2":
        print("Thank you for using our program!")
        break
    else:
      print("Invalid input")

main()



# Task two

def read_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            working_file = file.readlines()
            dates_temps = {}
            for dates in working_file:
               rework = dates.strip().split(',')
               dates_temps[rework[0]] = rework[1]
            return dates_temps     
    except FileNotFoundError:
        print("We do not have records for that year")


def average_temp(yearly_temps,date):
    try:
        temps_list = []
        for year, temps in yearly_temps.items():
            numbers = temps.replace('°C','')
            temps_list.append(int(numbers))
        total_temp = 0
        for num in temps_list:
            total_temp += num
        average = total_temp/len(temps_list)
        print(f"The average temperature for {date} was {average:.2f}°C")
    except AttributeError:
        print("Please enter in a different date")
       

def highest_temp(yearly_temps,date):
    try:
        temps_list = []
        for year, temps in yearly_temps.items():
            numbers = temps.replace('°C','')
            temps_list.append(int(numbers))
        temps_list.sort()
        print(f"The highest temperature for {date} was {temps_list[-1]}°C and the lowest temperature was {temps_list[0]}°C")
    except AttributeError:
        print("Please enter in a different date")


def main():
  print("Welcome:")
  while True:
    print(f"\nMain Menu:\n1. Average Temperature\n2. Highest/Lowest Temperature\n3. Exit")
    user_menu_input = input("Please select one of our menu options: ")
    if user_menu_input == "3":
        print("Thank you for using our program!")
        break
    elif user_menu_input == "1":
        user = input("What year do you want to use: ")
        file_list = read_file(f'question_three\\weather_files\\weather_{user}.txt')
        average_temp(file_list,user)
    elif user_menu_input == "2":
        user = input("What year do you want to use: ")
        file_list = read_file(f'question_three\\weather_files\\weather_{user}.txt')
        highest_temp(file_list,user)
       
    else:
      print("Invalid input")

main()
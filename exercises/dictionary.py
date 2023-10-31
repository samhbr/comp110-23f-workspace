""""EX06 - Dictionary Functions!"""
__author__ = "730563340"

def invert(inv_dict: dict[str, str]) -> dict[str, str]:
   empty_dict: dict[str, str] = {}
   for elem in inv_dict: 
        for inv_dict[elem] in empty_dict: #for raising key error 
            raise KeyError("More than one of the same key!")
        empty_dict[inv_dict[elem]] = elem
        return empty_dict

def favorite_color(color_dict: dict[str, str]) -> str: 
    color_count: dict = {}  # Create a dictionary to store the counts of each color
    most_popular_color = ""  # Initialize a variable to store the most popular color
    max_count: int = 0  # Initialize a variable to store the maximum count
    for color in color_dict:
        if color in color_count:
            color_count[color] += 1 
        else: 
            color_count[color] = 1 
        if color_count[color] > max_count: 
            max_count = color_count[color] 
            most_popular_color = color      
        return most_popular_color
            

def count(count_list: list[str]) -> dict[str, int]:
    count_dict: dict[str, int] = {}
    for item in count_list:
        if item in count_dict: 
            count_dict[item] += 1 
        else: 
            count_dict[item] = 1 
    return count_dict 

# Check to see if that item has already been established as a key in your dictionary.

def alphabetizer(alph_list: list[str]) -> dict[str, list[str]]: 
    word_dict = {} 
    for word in alph_list:
        initial_letter = word[0].lower()
        if initial_letter in word_dict:
            word_dict[initial_letter].append(word)
        else:
            word_dict[initial_letter] = [word]
    return word_dict



def update_attendance(attendance_list: dict[str, list[str]]):
    day = input("Enter the day of the week: ")
    student = input("Enter the student's name: ")
    if day in attendance_list:
        attendance_list[day].append(student)
    else:
        attendance_list[day] = [student]
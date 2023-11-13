"""EX06 - Dictionary Functions!"""
__author__ = "730563340"


def invert(inv_dict: dict[str, str]) -> dict[str, str]:
    """Inverts a dictionary where keys become values and values become keys."""
    empty_dict: dict[str, str] = {}
    for elem in inv_dict: 
        value = inv_dict[elem]
        if value in empty_dict: 
            raise KeyError("More than one of the same key!")
        empty_dict[value] = elem
    return empty_dict


def favorite_color(color_dict: dict[str, str]) -> str:
    """Finds the most popular color in a dictionary of colors."""
    color_count: dict[str, int] = {}  # Create a dictionary to store the counts of each color
    most_popular_color = ""  # Initialize a variable to store the most popular color
    max_count: int = 0  # Initialize a variable to store the maximum count
    for color in color_dict.values():
        if color in color_count:
            color_count[color] += 1 
        else: 
            color_count[color] = 1 

        if color_count[color] > max_count: 
            max_count = color_count[color] 
            most_popular_color = color    

    return most_popular_color
            

def count(count_list: list[str]) -> dict[str, int]:
    """Counts the occurrences of elements in a list and returns a dictionary with the counts."""
    count_dict: dict[str, int] = {}
    for item in count_list:
        if item in count_dict: 
            count_dict[item] += 1 
        else: 
            count_dict[item] = 1 
    return count_dict 


def alphabetizer(alph_list: list[str]) -> dict[str, list[str]]:
    """Sorts a list of words into a dictionary based on their initial letters."""
    word_dict: dict[str, list[str]] = {}
    for word in alph_list:
        if len(word) > 0:
            initial_letter = word[0].lower()

            if initial_letter in word_dict:
                word_dict[initial_letter].append(word)
            else:
                word_dict[initial_letter] = [word]

    return word_dict


def update_attendance(attendance_list: dict[str, list[str]], day: str, student: str) -> dict[str, list[str]]:
    """Updates an attendance dictionary with student attendance information."""
    if day in attendance_list:
        if student in attendance_list[day]: 
            return attendance_list 
        else: 
            attendance_list[day].append(student)  # Append student to the list
    else:
        attendance_list[day] = [student]
    return attendance_list

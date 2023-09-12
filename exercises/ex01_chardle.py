"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730563340"

# Prompt the user for a 5-character word 
user_word= input("Enter a 5-character word: ")

# Check that the word input has exactly 5 characters
if len(user_word) != 5:
    print("Error: Word must contain 5 characters")
    exit()  # Exit the program

# Prompt the user for a single character
user_character = input("Enter a single character: ")

# Check that the character input has exactly 1 character
if len(user_character) != 1:
    print("Error: Character must be a single character.")
    exit()  # Exit the program

# Print the diagnostic message
print(f"Searching for {user_character} in {user_word}")

# Check each index of the word string
for index, letter in enumerate(user_word):
    if letter == user_character:
        print(f"{user_character} found at index {index}")

# Count the number of matching characters
match_count = 0

# Check each index of the word string
for index, letter in enumerate(user_word):
    if letter == user_character:
        match_count += 1

        # Print the appropriate message based on the count
if match_count == 0:
    print(f"No instances of {user_character} found in {user_word}")
elif match_count == 1:
    print(f"1 instance of {user_character} found in {user_word}")
else:
    print(f"{match_count} instances of {user_character} found in {user_word}")
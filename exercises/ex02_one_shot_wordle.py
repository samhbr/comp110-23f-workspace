"""EX02 - One-Shot Wordle - Loops!"""

__author__ = "730563340"

my_secret_word: str = "python"
users_guess: str = input(f"What is your {len(my_secret_word)}-letter guess? ")

# Check the length of the user's guess
while (len(users_guess) != len(my_secret_word)):
    users_guess = input(f"That was not {len(my_secret_word)} letters! Try again: ")

index_of_guess: int = 0

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
resulting_string: str = ""

# Use the while loop to compare the user's guess to the secret word

while index_of_guess < len(my_secret_word):
    # Add green box if letter is found at the proper index
    if users_guess[index_of_guess] == my_secret_word[index_of_guess]:
        resulting_string += GREEN_BOX
    else:
        # Add a yellow box if the letter exists in a different place in the word
        matching_letter_found: bool = False
        alternate_index: int = 0
        while (matching_letter_found is False) and (alternate_index < len(my_secret_word)):
            if (users_guess[index_of_guess] == my_secret_word[alternate_index]):
                matching_letter_found = True
            else:
                alternate_index += 1
        if (matching_letter_found is True):
            resulting_string += YELLOW_BOX
    # Add a white box if the letter is not found in the secret word
    if (users_guess[index_of_guess] != my_secret_word[index_of_guess]) and (matching_letter_found is False):
        resulting_string += WHITE_BOX
    # The while loop runs again
    index_of_guess += 1

# Print the output
print(resulting_string)
if users_guess == my_secret_word:
    print("Woo! You got it!")
else:
    print("Not quite! Play again soon")

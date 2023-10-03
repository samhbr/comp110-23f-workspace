"""EX03 – A structured worldle similar to the NYT game!"""

__author__ = "730563340"

def contains_char(secret_string: str, guess_string: str) -> bool:
    """Compares each position or character index in the guessed word with the corresponding position in the true word."""
    assert len(guess_string) == 1
    char_present = False
    index = 0
    # Checks if the letter in the guess is at each position in the secret word.
    while index < len(secret_string):
        if guess_string == secret_string[index]:
            char_present = True
        index = index + 1
    # Returns the outcome of searching for the character to the function.
    if char_present is False: 
        return False 
    else: 
        return True

def emojified(guess_string: str, secret_string: str) -> str: 
    """Create a code for the emoji results of a guess versus the secret word."""
    WHITE_BOX = "\U00002B1C"
    GREEN_BOX = "\U0001F7E9"
    YELLOW_BOX = "\U0001F7E8"
    assert len(guess_string) == len(secret_string)
    emoji_result = ""
    secret_index = 0
    while secret_index < len(secret_string):
        if guess_string[secret_index] == secret_string[secret_index]:
            emoji_result += GREEN_BOX
        else:
            if contains_char(secret_string, guess_string[secret_index]):
                emoji_result += YELLOW_BOX
            else: 
                emoji_result += WHITE_BOX
        secret_index = secret_index + 1  
    return emoji_result

def input_guess(len_of_wordle: int) -> str: 
    """Lets the user know if the chosen word is the length of the secret word."""
    users_guess = input(f"Enter a {len_of_wordle} character word: ")
    while len(users_guess) != len_of_wordle: 
        users_guess = input(f"That wasn't {len_of_wordle} chars! Try again: ")
    return users_guess

def main() -> None: 
    """The entrypoint of the program and main game loop"""
    secret_word = "codes"
    turns = 1
    win = False
    while turns < 7 and win is False: 
        print(f"=== Turn {turns}/6 ===")
        guess_of_wordle = input_guess(len(secret_word))
        print(emojified(guess_of_wordle, secret_word))
        if guess_of_wordle == secret_word: 
            win = True
            print(f"You won in {turns}/6 turns!")
        turns += 1
    if win is False: 
        print("X/6 - Sorry, try again tomorrow!")

if __name__ == "__main":
    main()

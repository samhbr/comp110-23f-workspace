"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730563340"

users_word = input("Enter a 5-character word:")
if len(users_word) != 5:
    print("Error: Word must contain 5 characters")
    exit()  
character = input("Enter a single character")
if len(character) != 1:
    print("Error: Character must be a single character.")
    exit()  
    
print("Searching for"+ character + "in" + users_word )

if (character == users_word[0]):
    print(character + "found at index 0")
if (character == users_word[1]):
    print(character + "found at index 1")
if (character == users_word[2]):
    print(character + "found at index 2")
if (character == users_word[3]):
    print(character + "found at index 3")
if (character == users_word[4]):
    print(character + "found at index 4")

word_count: int = 0 
if character == users_word[0]:
    word_count = word_count + 1
if character == users_word[1]:
    word_count = word_count + 1
if character == users_word[2]:
    word_count = word_count + 1
if character == users_word[3]:
    word_count = word_count + 1
if character == users_word[4]:
    word_count = word_count + 1

if word_count == 0:
    print("No instances of {character} found in {users_word}")
if word_count == 1:
    print("1 instance of {character} found in {users_word}") 
if word_count > 1:
    print(str(word_count)) + "instances of" + {character} + "found in" + {users_word}
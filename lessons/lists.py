"""Lists!"""

# This is a Python script to practice working with lists

# Initialize an empty grocery list
grocery_list: list[str] = list()

# Add items to the grocery list
grocery_list.append("bananas")
grocery_list.append("milk")
grocery_list.append("bread")
grocery_list[1] = "cereal"

grocery_list.pop(2)
# Print the item at index 1 (remember that Python lists are zero-based)
print(grocery_list)
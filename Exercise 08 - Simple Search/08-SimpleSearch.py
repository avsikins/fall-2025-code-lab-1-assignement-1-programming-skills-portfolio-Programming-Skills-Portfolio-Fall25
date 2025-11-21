# Exercise 08: Simple Search
# This program searches for a name in a predefined list of names.

name_list = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]

search_name = input("Enter a name to search for: ")

if search_name.lower() in (name.lower() for name in name_list): # Case-insensitive search
    print(f"{search_name} found in the list.")
else:
    print(f"{search_name} not found in the list.")
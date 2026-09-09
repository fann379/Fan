# For each of these string methods, run the code and work out what they do!
# add a comment using # to each one to explain what it does

user_string = input("Enter a string: ")

print(f"\nOriginal String: {user_string}")
# Converts letters to lowercase.
print(f"Modified String 1: {user_string.lower()}")
# Converts letters to uppercase.
print(f"Modified String 2: {user_string.upper()}")
# Removes whitespace from both ends.
print(f"Modified String 3: {user_string.strip()}")
# Replaces every lowercase a with @.
print(f"Modified String 4: {user_string.replace('a', '@')}")
# Capitalizes the first character and lowercases the rest.
print(f"Modified String 5: {user_string.capitalize()}")
# Reverses the string using a slice.
print(f"Modified String 6: {user_string[::-1]}")
# Capitalizes the start of each word and lowercases other letters.
print(f"Modified String 7: {user_string.title()}")
# Counts all characters, including spaces.
print(f"Modified String 8: {len(user_string)}")
# Returns the first index of lowercase a, or -1 if absent.
print(f"Modified String 9: {user_string.find('a')}")
# Counts occurrences of lowercase a.
print(f"Modified String 10: {user_string.count('a')}")
# Checks whether the string begins with Hello (case-sensitive).
print(f"Modified String 11: {user_string.startswith('Hello')}")
# Checks whether the string ends with !.
print(f"Modified String 12: {user_string.endswith('!')}")
# Checks for a nonempty string of only letters or numeric characters.
print(f"Modified String 13: {user_string.isalnum()}")
# Checks for a nonempty string of only letters.
print(f"Modified String 14: {user_string.isalpha()}")
# Checks for a nonempty string of only digit characters.
print(f"Modified String 15: {user_string.isdigit()}")



######
# if you finish, you can look at some more: https://www.w3schools.com/python/python_ref_string.asp
# and add some extras to this selection!
# You can also combine these functions - have a play around and see what you can do!
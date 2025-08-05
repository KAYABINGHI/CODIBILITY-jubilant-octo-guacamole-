# Given a string, find the first character that does not repeat anywhere in the string; Return None if all characters repeat.

# Input: "Hello"
# Output: "H"

# Input: "Swiss"
# Output: "w"   

def first_non_repeating_char(q):
    
    char_count = {}

    for char in q:

        char_lower = char.lower()
        if char_lower in char_count:
            char_count[char_lower] += 1
        else:
            char_count[char_lower] = 1


    for char in q:
        if char_count[char.lower()] == 1:
            return char  

    
    return None

print(first_non_repeating_char("Hello"))  # Output: H
print(first_non_repeating_char("Swiss"))  # Output: w
print(first_non_repeating_char("aabbcc")) # Output: None

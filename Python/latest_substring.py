

def length_of_longest_substring(s):
    # This function finds the length of the longest substring without repeating characters

    # We use a set to keep track of characters in the current substring (window)
    seen = set()

  
    left = 0  # Start of the window
    max_length = 0  # Longest length found

    # Loop through each character in the string using the right pointer
    for right in range(len(s)):
        # If the character is already in the set, move the left pointer
        # and remove characters until there are no repeats
        while s[right] in seen:
            seen.remove(s[left])  # Remove the character at the left
            left += 1  # Move the left pointer to the right

        
        seen.add(s[right])

        # Update the max_length if we found a longer unique substring
        current_length = right - left + 1
        max_length = max(max_length, current_length)

    return max_length

# print(length_of_longest_substring("bbbbb"))   # Output: 1
print(length_of_longest_substring("pwwkew"))  # Output: 3

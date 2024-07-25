""" This module contains the solution to the permutation check problem. """
def urlify(s, length):
    """
    Function to replace all spaces in a string with '%20'.
    Args:
        s: A string with spaces to be replaced.
        length: The actual length of the string.
    Returns:
        The string with spaces replaced by '%20'.
    """
    # Create a list of characters with the length of the string
    result=['%20']* length
    # print statements added to enhance learning
    print(result) 
    # Initialize the index to 0
    i = 0
    # Loop through the string
    for char in s:
        if char != " ": # If the character is not a space
            result[i] = char # Replace the character at the current index with the character
        print(f'Step {i}:', result) # print the result at each step
        i += 1 # Move to the next index
    return "".join(result) # Convert the list to a string and return the result


"""
Alternative solution to the URLify problem.
For building Reasioning in problem solving.
"""
def urlify_concept2(s, trueLength):
    """
    Function to replace all spaces in a string with '%20' in place.
    This implementation caters for the considered edge cases.
    Args:
        s: A string with spaces to be replaced.
        trueLength: The actual length of the string.
    Returns:
        The string with spaces replaced by '%20'.
    """
    # Count the number of spaces in the string
    space_count =  sum(1 for i in range(trueLength) if s[i] == ' ')
    # Calculate the new length of the string.
    # Assuming the trueLength is  19 and the number of spaces is 2
    # The new length will be 19 + 2(2) = 23
    # The 2 cater for the two extra characters '%20' that will replace the space
    # The extra 2 are for "20" which adds with the existing space to make room for 3 characters
    new_length = trueLength + space_count * 2

    # Convert the string to a list of characters
    # This is because strings are immutable in python
    char_array =  list(s)

    # Initialize the index to the new length - 1
    # This is because we are going to replace the spaces from the end of the string
    # In this case the index will be 19 - 1 = 18
    index = new_length - 1

    # Loop through the string from the end

    for i in range(trueLength - 1, -1, -1):
        # If the current character is a space, replace it with '%20'
        # and move the index 3 steps back
        if char_array[i] == ' ':
           char_array[index - 1] = '0' # Repalce index - 1 with '0'
           char_array[index - 2] = '2' # Repalce index - 2 with '2'
           char_array[index - 3] = '%' # Repalce index - 3 with '%'
           index -= 3 # Move the index 3 steps back
        else:
            char_array[index - 1] = char_array[i] # Replace the current character with the character at index - 1
            index -= 1 # Move the index 1 step back
    return ''.join(char_array[:new_length]) # Convert the list to a string and return the result
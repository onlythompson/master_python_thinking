"""This module contains the solution to the unique characters problem as stated in the book Cracking the Code Interview By Gayle Laakmann McDowell."""
def isUniqueCharacters(s:str)->bool:
    """
    Function to determine if a string has all unique characters.
    Args:
        s: A string to be checked for unique characters.
    Returns:
        A boolean value indicating if the string has all unique characters.
    """
    """
    Background Knowledge on the solution:
    The ASCII character set has 128 characters. If the string has more than 128 characters, then it must have repeated characters.
    The solution to this problem is to create an array of boolean values, where the flag at index i indicates whether character i in the alphabet is contained in the string. The second time you see this character you can immediately return false.
    1. We can also use a bit vector to reduce the space usage.
    2. If we are only allowed to use lowercase alphabets, we can use a bit vector of size 32.

    Note: 
    The Time Complexity of this solution is O(n), where n is the length of the string.
    The Space Complexity (Total) of this solution is O(n).
    The Auxiliary Space Complexity (Temporary Memory used) of this solution is O(1), since the size of the array is fixed in this case 128.

    """
    # The len function returns the length of the string or an array.
    # Most precisely it returns the length of an iterable object in python
    # Personally , I like to represent this as n, where n is the length of the string.
    n = len(s)
    #Recall that the ASCII character set has 128 characters.
    if n > 128: # If the string has more than 128 characters, then it must have repeated characters.
        return False # No need to check further.
    
    #create an array of boolean values, where the flag at index i indicates whether character i in the alphabet is contained in the string.
    #The ord() function returns an integer representing the Unicode character.
    char_set = [False for _ in range(128)]
    for c in s: # Loop through the string.
        if char_set[ord(c)]: # If the character is already in the string, return False.
            return False # No need to check further.
        char_set[ord(c)] = True # Set the flag at index i to True.
    return True  # Return True if the string has all unique characters.


def isUniqueCharactersOptimized(s:str)->bool:
    """
    Similar to the isUniqueCharacters function, but optimized.
    Assuming we are not allowed to used additional data structures, How would you solve this problem?
    Bit Manipulation is a common approach to solving this problem.
    We can use a bit vector to reduce the space usage.

    Foundation Knowledge:
    1. A bit vector is an array of bits.
    2. A bit vector is used to represent bit arrays.
    3. A bit vector is a compact way to represent sets of integers.
    4. A bit vector is used to implement a simple set data structure.
    5. A bit vector is used to implement a simple bloom filter.
    6. A bit vector is used to implement a simple hash table.
    7. A bit vector is used to implement a simple bitmap.
    
    Masking and Shifting:
    1. Masking is the process of selecting bits from a bit vector.
    2. Shifting is the process of moving bits to the left or right.
    3. Shifting is used to set or clear bits. (1 << val) sets the bit at index val to 1.
    4. Shifting is used to extract bits. (val & (1 << i)) extracts the bit at index i.
    5. Shifting is used to toggle bits. (1 << val) toggles the bit at index val.
    """
    _vector = 0 # Initialize a bit vector to 0.
    for c in s: # Loop through the string.
        val = ord(c) - ord('a') # Get the ASCII value of the character and subtract the ASCII value of 'a'.
        if (_vector & (1 << val)) > 0: # If the character is already in the string, return False.
            return False # No need to check further.
        _vector |= (1 << val) # Set the bit at index val to 1.
    return True # Return True if the string has all unique characters.
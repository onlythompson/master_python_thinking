""" This module contains the solution to the anagrams problem. """

#Brute force solution
from itertools import permutations
from typing import List



def custom_permutations(s:str) -> List[str]:
    """
    Function to generate all possible permutations of a string.
    Args:
        s: A string to be permuted.
    Returns:
        A list of all possible permutations of the string.
    """
    # The permutations function returns all possible permutations of the specified iterable object.
    result = [] # Initialize an empty list to store the permutations.
    for char in s: # Loop through the string.
        if result: # If the result is not empty.
            new_result = [] # Initialize an empty list to store the new permutations.
            for perm in result: # Loop through the permutations.
                k = len(perm) # Get the length of the permutation.
                for i in range(k+1):
                    xters_before = perm[:i] # Get the characters before the current character.
                    xters_after = perm[i:] # Get the characters after the current character.
                    new_result.append(xters_before + char + xters_after)# Append the new permutation to the new_result list.
            result = new_result # Update the result list.
        else:
            result = [char]

    return result


print(custom_permutations("abc"))

def anagram_bruteforce(s:str, t:str):
    """
    Function to determine if two strings are anagrams.
    Args:
        s: A string to be checked for anagrams.
        t: A string to be checked for anagrams.
    Returns:
        A boolean value indicating if the two strings are anagrams.
    """
   # Generate a list of all possible permutations of the string s.
   # The permutations function returns all possible permutations of the specified iterable object.
   # The permutations here function is from the itertools module, similar to the custom_permutations function above.
    for p in permutations(s):
       # If the permutation is equal to the string t, then return True.
       if ''.join(p) == t:
           return True
    return False

#Sorting Snare: Tempting Trap
def anagram_sorting_snare(s:str, t:str):
    """
    Function to determine if two strings are anagrams.
    Args:
        s: A string to be checked for anagrams.
        t: A string to be checked for anagrams.
    Returns:
        A boolean value indicating if the two strings are anagrams.
    """
    # The len function returns the length of the string or an array.
    # Most precisely it returns the length of an iterable object in python
    # Recall what n and m are in our introduction to array? , let's use these to capture the length of the string inputs.
    n = len(s)
    m = len(t)
    # If the length of the two strings are not equal, then they can't be anagrams.
    if n != m:
        return False
    # The sorted function returns a sorted list of the specified iterable object.
    # The join function concatenates the elements of the list into a string.
    return ''.join(sorted(s)) == ''.join(sorted(t))

#Optimized Solution
from collections import Counter
def anagram_optimized(s:str, t:str):
    freq_s = Counter(s) # Count the frequency of each character in the string s.
    for c in t: # Loop through the characters in the string t.
        if c not in freq_s:
            return False
        else:
            freq_s[c] -= 1 # Decrement the frequency of the character.
            if freq_s[c] == -1: # If the frequency is less than 0, return False.
                return False
    return True
        
#More simplified optimized solution
def anagram_optimized2(s:str, t:str):
    return Counter(s) == Counter(t)

"""
How to Optimize the Solution without using another data structure?
We can sum the ord() values of the characters in the two strings and compare them.
If the sum of the ord() values of the characters in the two strings are equal, then the two strings are anagrams.
"""

# Optimized Solution without using another data structure
def anagram_optimized_without_another_ds(s:str, t:str):
    """
    Function to determine if two strings are anagrams.
    Args:
        s: A string to be checked for anagrams.
        t: A string to be checked for anagrams.
    Returns:
        A boolean value indicating if the two strings are anagrams.
    """
    # The len function returns the length of the string or an array.
    # Most precisely it returns the length of an iterable object in python
    # Recall what n and m are in our introduction to array? , let's use these to capture the length of the string inputs.
    n = len(s)
    m = len(t)
    # If the length of the two strings are not equal, then they can't be anagrams.
    if n != m:
        return False
    # The ord() function returns an integer representing the Unicode character.
    # The reduce function applies a function of two arguments cumulatively to the items of an iterable, in succession from left to right, so as to reduce the iterable to a single value.
    # The lambda function is an anonymous function.
    # The xor operator returns 1 if the bits are different, and 0 if the bits are the same.
    # The map function applies a function to all the items in an input_list.
    # The sum function returns the sum of all the elements in the list.
    return sum(map(lambda x, y: ord(x) ^ ord(y), s, t))
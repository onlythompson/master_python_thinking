""" This module contains the solution to the largest element problem """
def largest_element(arr: list[int]) -> int:
    """
    Function to find the largest element in an array.
    Args:
        arr: A list of integers.
    Returns:
        The largest element in the array.
    """
    # The len function returns the length of the list or an array.
    # Most precisely it returns the length of an iterable object in python
    # Personally , I like to represent this as n, where n is the length of the list.
    n = len(arr)
    # Initialize the largest element to the first element in the array.
    largest = arr[0] # Set the largest element to the first element(at index 0) in the array.
    for i in range(1, n): # Loop through the array started from the second element.
        if arr[i] > largest: # If the current element is greater than the largest element.
            largest = arr[i] # Set the largest element to the current element.
    return largest # Return the largest element in the array.
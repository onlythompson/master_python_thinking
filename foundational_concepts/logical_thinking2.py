# Task 11: Print a pattern of binary numbers starting with 1 or 0 alternately in each row.
def task11(n):
    """
    This function prints a pattern where each row starts with a binary number (1 or 0) and alternates.
    The starting number for each row changes based on whether the row number is odd or even.
    """
    for i in range(1, n + 1):  # Loop through each row
        # Determine the starting number for the row: 1 for odd rows, 0 for even rows
        start = 1 if i % 2 != 0 else 0
        for j in range(i):  # Loop through each column in the row
            print(start, end=" ")  # Print the current number
            start = 1 - start  # Toggle the number for the next column
        print()  # Move to a new line after finishing a row

# Task 12: Print a diamond pattern with numbers increasing then decreasing, separated by dashes.
def task12(n):
    """
    This function prints a diamond pattern where numbers increase to the middle of the row,
    then decrease, with dashes filling the spaces between the numbers.
    """
    for i in range(1, n):  # Loop through the upper half of the diamond
        for j in range(1, i + 1):  # Print increasing numbers
            print(j, end=" ")
        for j in range((2*(n-i))-2):  # Print dashes in the middle
            print("-", end=" ")
        for j in range(i, 0, -1):  # Print decreasing numbers
            print(j, end=" ")
        print()  # New line after each row

# Task 13: Print numbers in a right-angled triangle pattern, increasing with each row.
def task13(n):
    """
    This function prints a right-angled triangle pattern where each row contains consecutive numbers
    starting from 1 and increasing with each row.
    """
    counter = 1  # Initialize counter to keep track of the numbers to print
    for i in range(n):  # Loop through each row
        for j in range(i + 1):  # Loop through each column in the row
            print(counter, end=" ")  # Print the current number
            counter += 1  # Increment the counter for the next number
        print()  # Move to a new line after finishing a row

# Task 14: Print a right-angled triangle pattern with letters of the alphabet.
def task14(n):
    """
    This function prints a right-angled triangle pattern where each row contains consecutive letters
    of the alphabet starting from 'A'.
    """
    for i in range(n):  # Loop through each row
        xter = 'A'  # Initialize the character to start with 'A'
        _num = ord(xter)  # Convert the character to its ASCII value
        for j in range(i + 1):  # Loop through each column in the row
            print(chr(_num), end=" ")  # Print the current character
            _num += 1  # Increment the ASCII value for the next character
        print()  # Move to a new line after finishing a row

# Task 15: Print a reversed right-angled triangle pattern with letters of the alphabet.
def task15(n):
    """
    This function prints a reversed right-angled triangle pattern where each row contains consecutive letters
    of the alphabet starting from 'A', with the triangle inverted.
    """
    for i in range(n, -1, -1):  # Loop through each row in reverse order
        xter = 'A'  # Initialize the character to start with 'A'
        _num = ord(xter)  # Convert the character to its ASCII value
        for j in range(i):  # Loop through each column in the row
            print(chr(_num), end=" ")  # Print the current character
            _num += 1  # Increment the ASCII value for the next character
        print()  # Move to a new line after finishing a row

# Task 16: Print a right-angled triangle pattern with the same letter in each row, changing with each row.
def task16(n):
    """
    This function prints a right-angled triangle pattern where each row contains the same letter,
    and the letter changes with each new row, starting from 'A'.
    """
    xter = 'A'  # Initialize the character to start with 'A'
    _num = ord(xter)  # Convert the character to its ASCII value
    for i in range(n):  # Loop through each row
        for j in range(i + 1):  # Loop through each column in the row
            print(chr(_num), end=" ")  # Print the current character
        _num += 1  # Increment the ASCII value for the next character for the new row
        print()  # Move to a new line after finishing a row

# Task 17: Print a diamond pattern with letters, changing in the middle of each row.
def task17(n):
    """
    This function prints a diamond pattern where each row contains letters that increase to the middle
    of the row, then reset and increase again, with dashes filling the spaces on either side.
    """
    for i in range(n):  # Loop through each row
        xter = 'A'  # Initialize the character to start with 'A'
        _num = ord(xter)  # Convert the character to its ASCII value for increasing sequence
        _num2 = ord(xter)  # Convert the character to its ASCII value for resetting sequence
        for j in range((n - i)-1):  # Print leading dashes
            print("-", end=" ")
        for j in range((2*i) + 1):  # Print letters in the row
            if j <= (((2*i) + 1)//2):  # Increase letters to the middle
                print(chr(_num), end=" ")
                _num += 1
            else:  # Reset and increase letters after the middle
                print(chr(_num2), end=" ")
                _num2 += 1
        for j in range((n - i)-1):  # Print trailing dashes
            print("-", end=" ")
        print()  # Move to a new line after finishing a row

# Task 18: Print a right-angled triangle pattern with letters decreasing from 'Z' backwards.
def task18(n):
    """
    This function prints a right-angled triangle pattern where each row starts with a letter
    that is one less than the starting letter of the previous row, beginning from 'Z'.
    """
    xter = 'A'  # Initialize the character to start with 'A'
    for i in range(n):  # Loop through each row
        _num = ord(xter) + n - 1  # Calculate the starting ASCII value for the row
        _num -= i  # Adjust the ASCII value based on the row number
        for j in range(i + 1):  # Loop through each column in the row
            print(chr(_num), end=" ")  # Print the current character
            _num += 1  # Increment the ASCII value for the next character
        print()  # Move to a new line after finishing a row

# Task 19: Print a symmetric pattern with stars and dashes, both upwards and downwards.
def task19SymmetryUp(n):
    """
    This function prints the upper half of a symmetric pattern with stars and dashes.
    """
    for i in range(n):  # Loop through each row for the upper half
        for j in range(n - i):  # Print leading stars
            print("*", end=" ")
        for j in range(2*i):  # Print dashes in the middle
            print("-", end=" ")
        for j in range(n - i):  # Print trailing stars
            print("*", end=" ")
        print()  # Move to a new line after finishing a row

def task19SymmetryDown(n):
    """
    This function prints the lower half of a symmetric pattern with stars and dashes.
    """
    for i in range(n):  # Loop through each row for the lower half
        for j in range(i+1):  # Print leading stars
            print("*", end=" ")
        for j in range(2*(n-i-1)):  # Print dashes in the middle
            print("-", end=" ")
        for j in range(i+1):  # Print trailing stars
            print("*", end=" ")
        print()  # Move to a new line after finishing a row

def task19(n):
    """
    This function combines task19SymmetryUp and task19SymmetryDown to print a complete symmetric pattern
    with stars and dashes.
    """
    task19SymmetryUp(n)  # Print the upper half
    task19SymmetryDown(n)  # Print the lower half

# Task 20: Print a diamond pattern with stars and dashes.
def task20(n):
    """
    This function prints a diamond pattern with stars and dashes, where the number of stars increases
    then decreases, and the number of dashes fills the remaining space on each row.
    """
    for i in range(1, (n * 2)):  # Loop through each row for the entire diamond
        if i <= (n * 2)//2:  # For the upper half of the diamond
            for j in range(i):  # Print leading stars
                print("*", end=" ")
            for j in range(2*(n-i)):  # Print dashes in the middle
                print("-", end=" ")
            for j in range(i):  # Print trailing stars
                print("*", end=" ")
        else:  # For the lower half of the diamond
            for j in range((n*2) - i):  # Print leading stars
                print("*", end=" ")
            for j in range(2*(i - n)):  # Print dashes in the middle
                print("-", end=" ")
            for j in range((n*2) - i):  # Print trailing stars
                print("*", end=" ")
        print()  # Move to a new line after finishing a row

# Task 21: Print a square frame with stars.
def task21(n):
    """
    This function prints a square frame where the border is made of stars, and the inside is empty.
    """
    for i in range(n):  # Loop through each row
        for j in range(n):  # Loop through each column
            if i == 0 or j == 0 or i == n - 1 or j == n - 1:  # Print stars for the border
                print("*", end=" ")
            else:  # Leave the inside empty
                print(" ", end=" ")
        print()  # Move to a new line after finishing a row
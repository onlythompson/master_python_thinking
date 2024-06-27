# Define a function to print a square pattern of '*' characters.
def task1(n):
    # Loop over each row.
    for i in range(n):
        # Loop over each column in the current row.
        for j in range(n):
            # Print '*' without moving to a new line.
            print("*", end=" ")
        # Move to a new line after printing each row.
        print()
        
# Define a function to print a right-angled triangle pattern of '*' characters.
def task2(n):
    # Loop over each row.
    for i in range(n):
        # Print '*' for each column, increasing the number of '*' by 1 each row.
        for j in range(i+1):
            print("*", end=" ")
        # Move to a new line after printing each row.
        print()

# Define a function to print a right-angled triangle pattern of increasing numbers.
def task3(n):
    # Loop over each row.
    for i in range(n + 1):
        # Print numbers from 1 to i in each row.
        for j in range(i):
            print(j + 1, end=" ")
        # Move to a new line after printing each row.
        print()
        
# Define a function to print a right-angled triangle pattern where each row contains the same number, equal to the row number.
def task4(n):
    # Loop over each row.
    for i in range(1, n+1):
        # Print the row number 'i' for 'i' times.
        for j in range(i):
            print(i, end=" ")
        # Move to a new line after printing each row.
        print()

# Define a function to print an inverted right-angled triangle pattern of '*' characters.
def task5(n):
    # Loop over each row in reverse order.
    for i in range(n + 1, -1, -1):
        # Print '*' for each column in the row.
        for j in range(i):
            print("*", end=" ")
        # Move to a new line after printing each row.
        print()
        
# Define a function to print an inverted right-angled triangle pattern of decreasing numbers starting from n.
def task6(n):
    # Loop over each row in reverse order.
    for i in range(n, -1, -1):
        # Print numbers from 1 to i in each row.
        for j in range(i):
            print(j + 1, end=" ")
        # Move to a new line after printing each row.
        print()

# Define a function to print a pyramid pattern of '*' characters.
def task7(n):
    # Loop over each row.
    for i in range(n):
        # Print leading spaces to form the left side of the pyramid.
        for j in range(n-i-1):
            print(" ", end=" ")
        # Print '*' to form the middle of the pyramid.
        for j in range((2*i)+1):
            print("*", end=" ")
        # Print trailing spaces to form the right side of the pyramid (optional, for symmetry).
        for j in range(n-i-1):
            print(" ", end=" ")
        # Move to a new line after printing each row.
        print()

# Define a function to print an inverted pyramid pattern of '*' characters.
def task8(n):
    # Loop over each row in reverse order.
    for i in range(n, -1, -1):
        # Print leading spaces to form the inverted pyramid's left side.
        for j in range(n-i):
            print(" ", end=" ")
        # Print '*' to form the middle of the inverted pyramid.
        for j in range((2*i)-1):
            print("*", end=" ")
        # Print trailing spaces to form the inverted pyramid's right side (optional, for symmetry).
        for j in range(n-i):
            print(" ", end=" ")
        # Move to a new line after printing each row.
        print()
        
# Define a function to print a diamond pattern of '*' characters by combining task7 and task8.
def task9(n):
    # Print the upper half of the diamond.
    task7(n)
    # Print the lower half of the diamond.
    task8(n)
        
# Define a function to print a diamond pattern of '*' characters, optimized for fewer lines of code.
def task10(n):
    # Loop over each row for the entire diamond height.
    for i in range((n * 2)-1):
        # Determine the number of '*' to print based on the row's position relative to the diamond's center.
        if i < (n * 2)//2:
            for j in range(i+1):
                print("*", end=" ")
        else:
            for j in range((n*2) - i - 1):
                print("*", end=" ")
        # Move to a new line after printing each row.
        print()
        
# Set the size of the patterns to be printed.
n = 5
# Execute each task in sequence, printing a header for clarity.
print('Printing Task 1: ')
task1(n)
print("-"*(n + 1))
print('Printing Task 2: ')
task2(n)
print("-"*(n + 1))
print('Printing Task 3: ')
task3(n)
print("-"*(n + 1))
print('Printing Task 3: ')
task4(n)
print("-"*(n + 1))
print('Printing Task 5: ')
task5(n)
print("-"*(n + 1))
print('Printing Task 6: ')
task6(n)
print("-"*(n + 1))
print('Printing Task 7: ')
task7(n)
print("-"*((n*2) + 1))
print('Printing Task 8: ')
task8(n)
print("-"*((n*2) + 1))
print('Printing Task 9: ')
task9(n)
print("-"*((n*2) + 1))
print('Printing Task 10: ')
task10(n)
print("-"*((n*2) + 1))
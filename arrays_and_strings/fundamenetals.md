# Arrays and Strings

### Arrays
An array is a fundamental data structure found in nearly every programming language. It's a contiguous block of memory that stores a collection of elements of the same data type (e.g., numbers, characters, or even other arrays).

At the core, arrays can be thought of as fixed-size collection of elements stored in table like form with only one row.  

```
numbers = [5, 12, 8, 22, 1]  # Create an array of numbers
```
![Simple array representation](/arrays_and_strings/sample_array_primary.png)

### Strings: 
Many languages represent strings as arrays of characters.
While strings might seem like a separate data type, they are often implemented internally as arrays of characters. Each character in a string occupies a specific position (index) within this array. This underlying array-like structure enables efficient access to individual characters and substrings.

```
# Python: Strings are treated like immutable sequences (similar to arrays)
message = "Hello, world!"

print(message[0])      # Output: H (First character)
print(message[7:12])   # Output: world (Substring)

```

### Flexibility in Dynamically Typed Languages:

In dynamically typed languages like Python and JavaScript, arrays (often called lists in Python) are more flexible. They can store elements of different data types within the same array. This means you can mix numbers, strings, booleans, and even other objects in a single array.

```
mixed_data = [42, "Hello", True, [1, 2, 3]] 
```
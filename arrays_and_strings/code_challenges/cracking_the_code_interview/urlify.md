# Unraveling the URLify Mystery: A Tale of Strings and Spaces

## The Challenge

Given a string `s` containing alphanumeric characters and spaces, and an integer `true_length` representing the "true" length of the string, we need to replace all spaces with '%20' up to the `true_length`.

## Objective

Develop an efficient algorithm to perform the URLify operation, considering both simplicity and performance.

### Intriguing Examples:
1. 🧩 Input: s = "Mr Dominic Thompson    ", true_length = 19
   🎉 Output: "Mr%20Dominic%20Thompson"

2. 🧩 Input: s = "Hello World  ", true_length = 11
   🚫 Output: "Hello%20World"

3. 🧩 Input: s = "   Hello   ", true_length = 8
   🤔 Output: "%20%20%20Hello"

4. 🧩 Input: s = "NoSpaces", true_length = 8
   🕵️‍♂️ Output: "NoSpaces"

## The Algorithmic Adventure Begins:

### Understanding URLify

URLify is the process of replacing spaces in a string with '%20', which is how spaces are represented in URLs. This operation is crucial for creating valid URLs from user input or processing strings for web applications.


### The Sorting Snare: A Tempting Trap

You might think, "Aha! Let's split the string, replace spaces, and join it back!" Like this:

```python
def urlify_trap(s, true_length):
    return '%20'.join(s[:true_length].split())
```

Clever, agent, but not clever enough! 🕵️‍♂️
This approach creates new strings and doesn't modify the input in-place. We can do better!


### The Optimization Trap

In the world of algorithms, it's easy to fall into the trap of over-optimization. You might think, "We need to do this in-place!" or "We must minimize memory usage at all costs!" But hold on, intrepid problem-solver! Sometimes, the simplest solution is the best.

## The Common Solution Out There: URLify Pseudocode and Demonstration Cases

### URLify Pseudocode

```
FUNCTION urlify(string s, integer true_length)
    // Count spaces in the true length of the string
    space_count = COUNT spaces in s[0:true_length]
    
    // Calculate new length
    new_length = true_length + (space_count * 2)
    
    // Start from the end and work backwards
    FOR i = true_length - 1 DOWN TO 0
        IF s[i] is a space THEN
            s[new_length - 1] = '0'
            s[new_length - 2] = '2'
            s[new_length - 3] = '%'
            new_length = new_length - 3
        ELSE
            s[new_length - 1] = s[i]
            new_length = new_length - 1
        END IF
    END FOR
    
    RETURN s
```

### Demonstration Cases

#### Case 1: Basic URLify
Input: s = "Mr Dominic Thompson    ", true_length = 19
Expected Output: "Mr%20Dominic%20Thompson"

Pseudocode Execution:
1. Count spaces: space_count = 2
2. Calculate new length: new_length = 19 + (2 * 2) = 23
3. Start from index 18 (true_length - 1)
4. Move characters and replace spaces
5. Result: "Mr%20Dominic%20Thompson"

#### Case 2: No Spaces
Input: s = "NoSpaces", true_length = 8
Expected Output: "NoSpaces"

Pseudocode Execution:
1. Count spaces: space_count = 0
2. Calculate new length: new_length = 8 + (0 * 2) = 8
3. Start from index 7 (true_length - 1)
4. Move characters (no spaces to replace)
5. Result: "NoSpaces"

#### Case 3: Multiple Spaces
Input: s = "   Hello   ", true_length = 8
Expected Output: "%20%20%20Hello"

Pseudocode Execution:
1. Count spaces: space_count = 3
2. Calculate new length: new_length = 8 + (3 * 2) = 14
3. Start from index 7 (true_length - 1)
4. Move characters and replace spaces
5. Result: "%20%20%20Hello"

#### Case 4: Edge Case - All Spaces
Input: s = "          ", true_length = 5
Expected Output: "%20%20%20%20%20"

Pseudocode Execution:
1. Count spaces: space_count = 5
2. Calculate new length: new_length = 5 + (5 * 2) = 15
3. Start from index 4 (true_length - 1)
4. Replace all spaces
5. Result: "%20%20%20%20%20"

#### Case 5: Edge Case - Single Character
Input: s = "a         ", true_length = 1
Expected Output: "a"

Pseudocode Execution:
1. Count spaces: space_count = 0
2. Calculate new length: new_length = 1 + (0 * 2) = 1
3. Start from index 0 (true_length - 1)
4. No action needed
5. Result: "a"


### The Plot Twist: Simplicity Wins

Consider this straightforward approach:

```python
def urlify_simple(s, true_length):
    # print statements added to enhance learning
    result = ['%20'] * true_length
    print("Initial result =", result)
    i = 0
    for char in s:
        if char != " ":
            result[i] = char
        print(f'Step {i}:', result)
        i += 1
    return "".join(result)
```

Print Output :
```
Initial result = ['%20', '%20', '%20', '%20', '%20', '%20', '%20', '%20', '%20', '%20', '%20', '%20', '%20', '%20', '%20', '%20', '%20', '%20', '%20']
Step 0: ['M', '%20', '%20', '%20', '%20', '%20', '%20', '%20', '%20', '%20', '%20', '%20', '%20', '%20', '%20', '%20', '%20', '%20', '%20']
Step 1: ['M', 'r', '%20', '%20', '%20', '%20', '%20', '%20', '%20', '%20', '%20', '%20', '%20', '%20', '%20', '%20', '%20', '%20', '%20']
Step 2: ['M', 'r', '%20', '%20', '%20', '%20', '%20', '%20', '%20', '%20', '%20', '%20', '%20', '%20', '%20', '%20', '%20', '%20', '%20']
Step 3: ['M', 'r', '%20', 'D', '%20', '%20', '%20', '%20', '%20', '%20', '%20', '%20', '%20', '%20', '%20', '%20', '%20', '%20', '%20']
Step 4: ['M', 'r', '%20', 'D', 'o', '%20', '%20', '%20', '%20', '%20', '%20', '%20', '%20', '%20', '%20', '%20', '%20', '%20', '%20']
Step 5: ['M', 'r', '%20', 'D', 'o', 'm', '%20', '%20', '%20', '%20', '%20', '%20', '%20', '%20', '%20', '%20', '%20', '%20', '%20']
Step 6: ['M', 'r', '%20', 'D', 'o', 'm', 'i', '%20', '%20', '%20', '%20', '%20', '%20', '%20', '%20', '%20', '%20', '%20', '%20']
Step 7: ['M', 'r', '%20', 'D', 'o', 'm', 'i', 'n', '%20', '%20', '%20', '%20', '%20', '%20', '%20', '%20', '%20', '%20', '%20']
Step 8: ['M', 'r', '%20', 'D', 'o', 'm', 'i', 'n', 'i', '%20', '%20', '%20', '%20', '%20', '%20', '%20', '%20', '%20', '%20']
Step 9: ['M', 'r', '%20', 'D', 'o', 'm', 'i', 'n', 'i', 'c', '%20', '%20', '%20', '%20', '%20', '%20', '%20', '%20', '%20']
Step 10: ['M', 'r', '%20', 'D', 'o', 'm', 'i', 'n', 'i', 'c', '%20', '%20', '%20', '%20', '%20', '%20', '%20', '%20', '%20']
Step 11: ['M', 'r', '%20', 'D', 'o', 'm', 'i', 'n', 'i', 'c', '%20', 'T', '%20', '%20', '%20', '%20', '%20', '%20', '%20']
Step 12: ['M', 'r', '%20', 'D', 'o', 'm', 'i', 'n', 'i', 'c', '%20', 'T', 'h', '%20', '%20', '%20', '%20', '%20', '%20']
Step 13: ['M', 'r', '%20', 'D', 'o', 'm', 'i', 'n', 'i', 'c', '%20', 'T', 'h', 'o', '%20', '%20', '%20', '%20', '%20']
Step 14: ['M', 'r', '%20', 'D', 'o', 'm', 'i', 'n', 'i', 'c', '%20', 'T', 'h', 'o', 'm', '%20', '%20', '%20', '%20']
Step 15: ['M', 'r', '%20', 'D', 'o', 'm', 'i', 'n', 'i', 'c', '%20', 'T', 'h', 'o', 'm', 'p', '%20', '%20', '%20']
Step 16: ['M', 'r', '%20', 'D', 'o', 'm', 'i', 'n', 'i', 'c', '%20', 'T', 'h', 'o', 'm', 'p', 's', '%20', '%20']
Step 17: ['M', 'r', '%20', 'D', 'o', 'm', 'i', 'n', 'i', 'c', '%20', 'T', 'h', 'o', 'm', 'p', 's', 'o', '%20']
Step 18: ['M', 'r', '%20', 'D', 'o', 'm', 'i', 'n', 'i', 'c', '%20', 'T', 'h', 'o', 'm', 'p', 's', 'o', 'n']

Mr%20Dominic%20Thompson

```

At first glance, it might not seem "optimized". But let's break it down:

1. It handles all cases correctly, including multiple spaces and edge cases.
2. It's easy to understand and implement.
3. It performs the operation in a single pass through the string.
4. It doesn't require complex in-place manipulations.

### The Eureka Moment: Efficiency in Simplicity

Remember: "Simplicity is the ultimate sophistication." - Leonardo da Vinci

How can we leverage the power of simplicity to create an efficient and robust solution?

### Your Mission, Should You Choose to Accept It:

1. Implement the simple URLify function shown above.
2. Test it with various inputs, including edge cases.
3. Analyze its time and space complexity.
4. Consider: In what scenarios might a more complex, in-place solution be necessary?

Are you ready to embrace the power of simplicity and create an elegant URLify solution? The game is afoot! 🕵️‍♂️🔍

## The Solution: URLify Implementation and Analysis

```python
def urlify(s, true_length):
    result = ['%20'] * true_length
    i = 0
    for char in s:
        if char != " ":
            result[i] = char
        i += 1
        if i == true_length:
            break
    return "".join(result)

# Test cases
test_cases = [
    ("Mr Dominic Thompson    ", 19),
    ("Hello World  ", 11),
    ("   Hello   ", 8),
    ("NoSpaces", 8),
    ("          ", 5),
    ("a         ", 1)
]

for s, true_length in test_cases:
    print(f"Input: '{s}', true_length: {true_length}")
    print(f"Output: '{urlify(s, true_length)}'")
    print()
```

### Analysis

1. **Time Complexity**: O(n), where n is the true_length. We make a single pass through the string.
2. **Space Complexity**: O(n), we create a new list of length true_length.
3. **Simplicity**: The code is straightforward and easy to understand.
4. **Robustness**: Handles all edge cases correctly (multiple spaces, leading/trailing spaces, no spaces).
5. **Efficiency**: Performs the operation in a single pass, with no need for complex calculations or manipulations.

### Key Insights

1. **Simplicity Leads to Reliability**: The simple approach handles all cases correctly without complex logic.
2. **Pre-allocation is Powerful**: By pre-allocating the result array with '%20', we simplify our space replacement logic.
3. **Single Pass Efficiency**: We only need to iterate through the string once, replacing non-space characters as we go.
4. **Proper Use of Parameters**: The true_length parameter allows us to handle trailing spaces correctly without extra complexity.


## The Final Analysis

OOur URLify solution demonstrates that sometimes, the most straightforward approach is also the most effective. By pre-allocating space and using a simple replacement strategy, we've created a solution that is:

1. Easy to understand and implement
2. Efficient in both time and space
3. Robust against various edge cases
4. Easily adaptable to different programming languages

This solution serves as a reminder that in algorithm design, we should always consider simplicity alongside optimization. Often, a clear and straightforward solution can outperform more complex approaches in both efficiency and reliability.

Remember, in the world of coding, clarity and correctness should be our first priorities. Optimize only when necessary, and always measure the impact of your optimizations. Happy coding! 🚀💻

[Solution](/arrays_and_strings/code_challenges/cracking_the_code_interview/urlify.py)
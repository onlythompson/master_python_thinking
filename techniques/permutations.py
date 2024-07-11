def custom_permutations(s):
    """
    Function to generate all possible permutations of a string.
    Args:
        s: A string to be permuted.
    Returns:
        A list of all possible permutations of the string.
    """
    # The permutations function returns all possible permutations of the specified iterable object.
    result = []
    for char in s:
        print(f'Processing the {s.index(char)}: {char}')
        if result:
            new_result = []
            for perm in result:
                print(f'Processing the perm - {perm}')
                for i in range(len(perm)+1):
                    xters_before = perm[:i] # Get the characters before the current character.
                    xters_after = perm[i:] # Get the characters after the current character.
                    print(f'xters_before: {xters_before}')
                    print(f'xters_after: {xters_after}')
                    new_result.append(xters_before + char + xters_after)
            result = new_result
        else:
            result = [char]
        print(result)
        print()

    return result
    
print(custom_permutations("abc"))
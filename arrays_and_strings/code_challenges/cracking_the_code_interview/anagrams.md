# Unraveling the Anagram Mystery: A Tale of Two Strings

## The Challenge

Given two strings 's' and 't', we need to verify if the characters in 's' can be rearranged to form 't' while maintaining their respective frequencies.

## Objective

Develop an efficient algorithm to determine if string 's' is a permutation (anagram) of string 't'.

### Intriguing Examples:
1. 🧩 Input: s = 'abc', t = 'bac'
   🎉 Output: true (Anagram alert!)

2. 🧩 Input: s = 'xyz', t = 'xwz'
   🚫 Output: false (Close, but no cipher!)

## The Algorithmic Adventure Begins:  

### Understanding Permutations

A permutation is an arrangement of elements in different orders. For example, the permutations of "ABC" include "BCA", "CAB", "ACB", etc.  
[Permutations Technique](/techniques/permutations.md)  
Your first instinct might be to reach for the trusty Brute Force approach - our metaphorical craftsman's pliers. "Let's generate all permutations of 's' and see if 't' matches any of them!" you might think. But hold on, intrepid problem-solver! There's a twist in this tale...  

### The Brute Force Trap

Your first instinct might be to generate all permutations of 's' and check which matches 't'. But beware!

### The Plot Thickens: Why Brute Force Falters
Picture this: You're faced with strings composed of 20 unique characters. Sounds manageable, right? But wait! The number of permutations skyrockets to a mind-boggling 20! (that's 2,432,902,008,176,640,000 possibilities! 🤯). Suddenly, our brute force approach seems less like a clever solution and more like trying to empty the ocean with a teaspoon.  

For a 20-character string: 20! = 2,432,902,008,176,640,000 possibilities! 🤯  
For a 1000-character string: 1000! ≈ 4 × 10^2567 (that's more than the atoms in the known universe!)

### The Plot Twist: Edge Cases and Extreme Scenarios
Imagine tackling a string with 1000 characters! Our brute force hero would crumble under the weight of 1000!permutations. It's time to think smarter, not harder.  

#### Ponder Cases  

3. 🧩 Input: s = '', t = ''
   🤔 Output: true (The case of the invisible anagram!)

4. 🧩 Input: 
   s = 'xyzetwegwgfwefqefwefqefqefqwefqwefqwefqwefqwefawdhgherhdbsdfer'
   t = 'xwrgewgwqefqeqwefwwewvfdgqwhnhhkitlioomdgbesgsergasfdarafdsfsdfgsz'
   🕵️‍♂️ Output: false (A real cryptographic challenge!)


### The Sorting Snare: A Tempting Trap

"Aha!" you might exclaim, reaching for your sorting wand. "Let's just sort both strings and compare them!"

```python
def is_permutation_sorting_trick(s, t):
    return sorted(s) == sorted(t)
```


Clever, agent, but not clever enough! 🕵️‍♂️
While this sorting sleight of hand might dazzle rookies, seasoned code-crackers know better. Let's break it down:

-   Time Complexity: O(n log n) - The sorting serpent rears its logarithmic head!
- Space Complexity: Varies by sorting algorithm, but often O(n) or O(log n)

But wait! As Gayle Laakmann McDowell would ask:

>"Is this the Best Conceivable Runtime (BCR) for our anagram adventure?"

Spoiler alert: It's not even close! 🚀  

Remember, elite code agents don't just think outside the box - they obliterate the box entirely! We're after efficiency that would make even quantum computers blush.  

Can you devise a solution that makes this sorting trick look like a snail's pace? Hint: Think about what information we truly need to compare these strings. Do we really need them in order? 🤔  

Your mission, should you choose to accept it, is to craft an algorithm so swift, it leaves this sorting solution in the dust. The clock is ticking, agent. How low can you go?

### The Eureka Moment: Enter the Hash Table:
> Remember: "A Data Structure is a specialized way of organizing and storing data so that it can be used effectively."

Remember our old friend, the Hash Table? This data structure might just be the key to cracking our anagram conundrum in linear time - O(n). But how? 🤔

### Your Mission, Should You Choose to Accept It:

1. Ponder: How can a Hash Table help us compare two strings efficiently?
2. Challenge: Can you devise an algorithm that works in O(n) time?
3. Bonus: How would your solution handle unicode characters or very large strings?

Are you ready to unlock the secret of anagrams and harness the power of Hash Tables? The game is afoot! 🕵️‍♂️🔍

[Solution](/arrays_and_strings/code_challenges/cracking_the_code_interview/anagrams.py)
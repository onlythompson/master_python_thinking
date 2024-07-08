
# Foundational Concepts

These foundational concept provide a background into algorithimic thinking. I believe it provides the base knowledge to guide your reasoning and builds your intiution into problem solving.

The code challenges represented from this section are taken from strivers a2z-dsa course.  
Sources:https://takeuforward.org/strivers-a2z-dsa-course/must-do-pattern-problems-before-starting-dsa/  


## Always Remember this:

![Foundational Concept of Computation](/foundational_concepts/resources/master_ds_algo_1.png)

# Part 1: Understanding various looping constructs

##  Buidling Blocks of Repititive Tasks:

Looping constructs are fundamental programming concepts that allow you to repeat a block of code multiple times. They're essential for efficient programming and automating repetitive tasks.  

At the core, these are programming structures that repeat a set of instructions until a specific condition is met. They help you avoid writing the same code over and over again.  

Fundamentally, there are 3 kinds of loops. But python support 2 types of looping constructs:
1. `For loop`: This is used when you know in advance how many times you want to repeat something. Example counting from 1 to another number(n).  

>**Key Idea:** The for loop is like a precise counter that says, "Do this action this many times."

> **Note:** n in programming is usually used to refer to a size or quantity of input data. Think of it as an arbitrary number that represent any number that comes to mind.  

2. `While loop`: This is used to repeat and execution of a code block while a particular condition is satisfied(remains **TRUE**). It is you go-to-tool when repitition depends on a condition being true.  

The following examples(challenges), provide the basic for using and buidling the intituitive undestanding on how the `for loop` in python works and how you can use it to solve basic problems.

## Loop Anatomy:

Every loop, whether` for` or `while`, has the following essential components:

1. **Initialization (Optional):** Setting up any variables needed before the loop starts.
2. **Condition:** The logical expression that determines if the loop should continue running.
3. **Body:** The code block that gets executed repeatedly.
4. **Update (Optional):** Modifying variables within the loop to eventually make the condition false (in while loops).


## Print n number of patterns  

### Task 1:  

Write a code to print this pattern:  

```
* * * * *  
* * * * *  
* * * * *  
* * * * *  
* * * * *  
```
### Task 2:  

Write a program to print this:  

```
*  
* *  
* * *  
* * * *  
* * * * *  
* * * * * *  
```

### Task 3:  

```
Write a program to print this:  

1  
1 2  
1 2 3  
1 2 3 4  
1 2 3 4 5  
1 2 3,4,5,6  

```

### Task 4:  

```
Write a program to print this:  

1  
2 2  
3 3 3  
4 4 4 4  
5 5 5 5 5  
6 6 6 6 6 6  
```

### Task 5:  

Write a program to print this:  

```
* * * * *  
* * * *   
* * *   
* *   
*  
```

### Task 6:

Write a program to print this:  

```
1 2 3 4 5  
1 2 3 4  
1 2 3  
1 2  
1  
```

### Task 7:

Write a program to print this:  
```
        *  
      * * *  
    * * * * *  
  * * * * * * *  
* * * * * * * * *  
```
### Task 8:

Write a program to print this:  

```
* * * * * * * * *
  * * * * * * *
    * * * * *
      * * *
        *
```


### Task 9:

Write a program to print this:  

```
        *
      * * *
    * * * * *
  * * * * * * *
* * * * * * * * *
* * * * * * * * *
  * * * * * * *
    * * * * *
      * * *
        *
```

### Task 10:

Write a program to print this:  

```
*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*

```
[Part 1 Solutions](/foundational_concepts/logical_thinking.py)


# Part 2: Understanding various looping constructs

*Ever wondered how experienced programmers seem to effortlessly grasp complex algorithms? It often comes down to their ability to recognize patterns. :+1:*

As we dive into the fascinating world of algorithms, you'll discover that recognizing patterns is like unlocking a secret language. It's a skill that empowers you to understand problems more deeply and create elegant solutions. Let's embark on this journey together, sharpening our pattern recognition skills and building that intuition that makes problem-solving feel like a breeze!

### Task 11:  
Write a program to print this:  
```
1
0 1
1 0 1
0 1 0 1
1 0 1 0 1
```

### Task 12:
Write a program to print this:  
```
1 - - - - - - 1   
1 2 - - - - 2 1   
1 2 3 - - 3 2 1   
1 2 3 4 4 3 2 1   
```
### Task 13:
Write a program to print this:  
```
1
2 3
4 5 6
7 8 9 10
11 12 13 14 15    
```

### Task 14:
Write a program to print this:  
```
A
A B
A B C
A B C D
A B C D E
```   
### Task 15:
Write a program to print this:  
```
A B C D E
A B C D
A B C
A B
A
```       
### Task 16:
Write a program to print this:  
```
A
B B
C C C
D D D D
E E E E E
```
### Task 17:
Write a program to print this:  
```
- - - - A - - - - 
- - - A B A - - - 
- - A B C A B - - 
- A B C D A B C - 
A B C D E A B C D 
```
  
### Task 18:
Write a program to print this:  
```
E
D E
C D E
B C D E
A B C D E

```

### Task 19:
Write a program to print this:  
``` 
* * * * * * * * * *
* * * * - - * * * *
* * * - - - - * * *
* * - - - - - - * *
* - - - - - - - - *
* - - - - - - - - *
* * - - - - - - * *
* * * - - - - * * *
* * * * - - * * * *
* * * * * * * * * *

```
### Task 20:
Write a program to print this:  

```
* - - - - - - - - *
* * - - - - - - * *
* * * - - - - * * *
* * * * - - * * * *
* * * * * * * * * *
* * * * - - * * * *
* * * - - - - * * *
* * - - - - - - * *
* - - - - - - - - *
```

### Task 21:
Write a program to print this:  

```
* * * * *
*       *
*       *
*       *
* * * * *
```

[Part 2 Solutions](/foundational_concepts/logical_thinking2.py)
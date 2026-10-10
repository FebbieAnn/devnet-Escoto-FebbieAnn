"""
Module 2 — Lesson 4: Functions
Student: [Febbie Ann Escoto]
Date: [09/25/2026]

============================================
WHAT IS THIS TOPIC? (explain it like you're
teaching a friend who's never coded before)
============================================
Function is a reusable block of code, instead of typing a multiple line of identical code over and over again, and making the coder or a developer 
repeating the specific line of code just to get the similar output. Function is a great syntax when it comes to those kind of situations. You can make your own logic inside
the function and you may use it anywhere, just by calling the function. **def** is a keyword to define the function, and there is a **function name** it uses to call the function.
You always have to remember that in order for you to get the code inside the function it must be indented, that is the only way the python recognized the line of code is inside
the function.


============================================
KEY VOCABULARY
============================================
- def: A keyword used to define or create a function
- function_name(): function's name are use to call the functions 
- Return: return is inside the function and this will be used to return the data or the logic you made back to the program that called it
- index: The position of an item in a sequernce, such as a list or string. Python indexing starts at 0
- iteration: One complete repetition of a loop
-paremeter: a variable listed inside a function's parentheses tht  receives a value when then function is called
- argument: The actual value passed to a function when it is call or execute.
- global variable: AA varible defined outside a function that can generally be accessed
only inside the function
- local varible: A varible defined inside a function that is generally accessible only within 
that function


============================================
MY OWN EXAMPLE(S)
============================================
Write at least one working example below that you
came up with yourself — not copied from class.
"""

# --- your code example goes here ---

def count_vowels(word):
    count = 0       #This is use to count and have a track for vowels
    for letter in word:         #use for loop to check the word one character at a time
        if letter.lower() in "aeiou":
            count+=1
    return count

word = input("Enter a word: ")  #User input
result = count_vowels(word)     #Call the function
print(f"Number of vowels {result}")

"""
============================================
A MISTAKE I MADE (or one I want to avoid)
============================================
[what's something confusing or easy to get wrong
about this topic?]

I don't know how to properly use functions or call them in a way that avoids 
logical errors. I am still having a hard time understanding functions, especially when
there are multiple codes and problems. To avoid this, I just have to practice, keep trying
to understand how functions work, and use free resources related to this topic. 
One thing for sure is that I have to practice my logic.



============================================
HOW THIS CONNECTS TO SOMETHING ELSE
============================================
[optional]
"""

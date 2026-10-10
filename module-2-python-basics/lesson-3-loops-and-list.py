"""
Module 2 — Lesson 3: Loops & Lists
Student: Febbie Ann Escoto
Date: 10/03/2026

============================================
WHAT IS THIS TOPIC? (explain it like you're
teaching a friend who's never coded before)
============================================
[write your own explanation here]
A loop is a tool that repeats a set of instructions over and over again until 
a specific condtion is reached

============================================
KEY VOCABULARY
============================================
- list: store multiple items in a single variable []
- for loop: A loop used to step through items in a collection or sequence a specific number of times
- while loop: A loop that repeatedly executes code as long as a given condition evaluates to True
- index: The numerical position of an item in a list, starting at 0 for the first item
- iteration: One single pass or cycle through a loop's block of code
- append: A buil-in list methhod used to add a new item to the end of a list 


============================================
MY OWN EXAMPLE(S)
============================================
Write at least one working example below that you
came up with yourself — not copied from class.
"""

# --- your code example goes here ---
scores = [85, 72, 90, 660, 95, 48]

total = 0
passing = 0

for score in scores:
    total += score

    if score >= 75:
        passing += 1
Average = total/len(scores)

print(f"Total: {total}")
print(f"Average: {Average}")
print(f"Passing Scores: {score}")


"""
============================================
A MISTAKE I MADE (or one I want to avoid)
============================================
[what's something confusing or easy to get wrong
about this topic?]
I sometimes get confused about how loops work with lists, especially when to use variables like total
and passing. I also tend to make mistakes when using len() and choosing the correct variable to
display in the output. To avoid these mistakes, I need to practice tracing the loop step by step and 
understand the purpose of each variable and where to use it.

============================================
HOW THIS CONNECTS TO SOMETHING ELSE
============================================
[optional]
"""

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
time_study = [2.5, 2.9, 3.4, 5.5, 9.9]
total_time = 0


for day_num, hours in enumerate(time_study, start=1): #start to 1
    total_time += hours
    if hours >= 3.0:
        status = "Great job!"
    elif hours > 0:
        status = "Good effort."
    else:
        status = "Rest day."
    print(f"Day {day_num}: {hours} hrs - {status}")

print(f"\nTotal Hours Studied: {total_hours} hrs")

# Using a while loop as a countdown timer
timer = 3
print("\nStarting quiz in:")
while timer > 0:
    print(f"{timer}...")
    timer -= 1  # Decrement timer so the loop eventually stops!
print("Begin!")



"""
============================================
A MISTAKE I MADE (or one I want to avoid)
============================================
[what's something confusing or easy to get wrong
about this topic?]


============================================
HOW THIS CONNECTS TO SOMETHING ELSE
============================================
[optional]
"""

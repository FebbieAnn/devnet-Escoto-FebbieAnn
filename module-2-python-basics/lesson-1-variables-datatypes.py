"""
Module 2 — Lesson 1: Variables & Data Types
Student: Febbie Ann Escoto
Date: 10/02/2026

============================================
WHAT IS THIS TOPIC? (explain it like you're
teaching a friend who's never coded before)
============================================
[write your own explanation here]
Think the Variable as a labeled box storage where you can store your things
inside of that box, and you can put a piece of information inside of it and use it later. 
Value is the things inside that box, and data type is simply
the "kind" of item you are putting inside that box. 

============================================
KEY VOCABULARY
============================================
- variable: A named container used to store data in a memory so it can be reused or updated
- data type: A classification that tells what kind of value a variable holds
- int: integer represent the whole numbers
- float: floating numbers represent the number with decimal form
- string: used for text it needs to be inside the quotations to identify as a string
- boolean: it only  holds to possible options: true or false
- type casting: used for converting variable from one data type to another 


============================================
MY OWN EXAMPLE(S)
============================================
Write at least one working example below that you
came up with yourself — not copied from class.
"""

# --- your code example goes here ---

Name = "Godzilla"     #string
level = 67      #int
hp = 99.5       #float
alive = True     #Boolean

print(f"Name: {Name}")
print(f"Level: {level}")
print(f"Health Points: {hp}")
print(f"Status: {alive}")

level += 2
print("Updated Level:", level)

"""
============================================
A MISTAKE I MADE (or one I want to avoid)
============================================
[what's something confusing or easy to get wrong
about this topic?]

I used f formarting here, I always misplaced the quotation marks

============================================
HOW THIS CONNECTS TO SOMETHING ELSE
============================================
[optional]
"""

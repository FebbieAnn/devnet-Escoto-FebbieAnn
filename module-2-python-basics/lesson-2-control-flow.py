"""
Module 2 — Lesson 2: Control Flow (if / elif / else)
Student: Febbie Ann Escoto
Date: 10/03/2026

============================================
WHAT IS THIS TOPIC? (explain it like you're
teaching a friend who's never coded before)
============================================
[write your own explanation here]
Control flow with if, elif, and else is like giving a decision tree,
the computer read the code line by line, control flow lets your program ask question
along the way and decide which of the program decision needs to be execute.

============================================
KEY VOCABULARY
============================================
- condition: A statement or a question that evaluates to either True or False

- if / elif / else: keywords used to structure the decision making, "if" checks the 
first condition , "elif" for (else if) it will go down to elif if the earlier condition
is false, and "else" runs a fallback if no condition were met.

- comparison operator: Symbols used to compare two values, such as "==" (equal to),
"!=" (not equal to), ">", "<", ">=", and "<=".

- boolean expression: for true or false

- logical operator: Keywords like `and`, `or`, and `not` used to combine
multiple conditions into a single decision.



============================================
MY OWN EXAMPLE(S)
============================================
Write at least one working example below that you
came up with yourself — not copied from class.
"""

# --- your code example goes here ---
age = 17
student_id = True

if age < 12:
    ticket_price = 8.00
    category = "Child"
elif age >= 65:
    ticket_price = 9.00
    category = "Senior"
elif age <= 22 and student_id:
    ticket_price = 10.00
    category = "Student Discount"
else:
    ticket_price = 14.00
    category = "Standard Adult"

print(f"Ticket Category: {category}")
print(f"Final Price: ${ticket_price:.2f}")

"""
============================================
A MISTAKE I MADE (or one I want to avoid)
============================================
[what's something confusing or easy to get wrong
about this topic?]
The use of greater than and less than 

============================================
HOW THIS CONNECTS TO SOMETHING ELSE
============================================
[optional]
"""

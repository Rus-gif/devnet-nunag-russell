"""
Module 2 — Lesson 1: Variables & Data Types
Student: Russell C. Nunag
Date:  Sept. 27, 2026

============================================
WHAT IS THIS TOPIC? (explain it like you're
teaching a friend who's never coded before)
============================================
[write your own explanation here]
 variable like a labeled container that stores information so you can use it again later
 data type tells the computer what kind of valie its storing like a number, decimals, or text.
 this matters because you can do thinks like math on numbers not on a text.

============================================
KEY VOCABULARY
============================================
- variable: a nme where you store a value.
- data type: tells the computer what kinf of valie is being stored.
- int: whole number
- float: decimal number
- string: text  
- boolean: true or false value
(add more as needed)


============================================
MY OWN EXAMPLE(S)
============================================
Write at least one working example below that you
came up with yourself — not copied from class.
"""

# --- your code example goes here ---
Name = input("Enter your name: ")
age = int(input("Enter your age: "))
gpa = float(input("Enter your GPA: "))
is_enrolled = input("Are you enrolled? (yes/no): ").lower() == "yes"

print("Name:", Name)
print("Age:", age)
print("GPA:", gpa)
print("Is Enrolled:", is_enrolled)

year_until_20 = 20 - age
print("Years until 20:", year_until_20)

"""
============================================
A MISTAKE I MADE (or one I want to avoid)
============================================
[what's something confusing or easy to get wrong
about this topic?]

At first I wasn't sure why I needed int() and float() around the
input() calls. input() always returns a string, even if someone
types a number like "16". If I had left out int(), age would still
be the text "16" instead of the number 16, and the line
year_until_20 = 20 - age would crash with a TypeError, because
Python can't subtract a number from text. Wrapping it in int()
converts the string into a real number so the math works.


============================================
HOW THIS CONNECTS TO SOMETHING ELSE
============================================
This is similar to entering data into a spreadsheet or gradebook —
a grade column expects numbers, and if you accidentally type text
into it, formulas that rely on that column stop working. Python's
data types are doing the same kind of check, just automatically.

"""

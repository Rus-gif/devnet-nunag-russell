"""
Module 2 — Lesson 2: Control Flow (if / elif / else)
Student: Russell C. Nunag
Date: Sept. 27, 2026

============================================
WHAT IS THIS TOPIC? (explain it like you're
teaching a friend who's never coded before)
============================================
[write your own explanation here]

Control flow is how a program makes decisions. Instead of running
every line of code no matter what, you can tell it "only do this
IF something is true, otherwise do something ELSE." It's the same
logic you use every day: "if it's raining, bring an umbrella,
otherwise leave it home." Python checks a condition, and depending
on whether that condition is True or False, it decides which block
of code to run.

============================================
KEY VOCABULARY
============================================
- condition:a statement that evaluates to either True or False,
- if / elif / else:"if" checks the first condition, "elif" (short for "else if") checks
another condition only if the first one was False, and "else" 
runs when none of the conditions above it were True
- comparison operator:a symbol used to compare two values, like
== (equal to), != (not equal to), > (greater than), < (less than),
>= (greater than or equal to), <= (less than or equal to)
- boolean expression:a condition that evaluates to either True or False
(add more as needed)


============================================
MY OWN EXAMPLE(S)
============================================
Write at least one working example below that you
came up with yourself — not copied from class.
"""

# --- your code example goes here ---

score = int(input("Enter your test score: "))

if score >= 90:
    grade = "A"
elif score >= 85:
    grade = "B"
elif score >= 80:
    grade = "C"
elif score >= 75:
    grade = "D"
else:
    grade = "F"

print("Your grade is:", grade)

"""
============================================
A MISTAKE I MADE (or one I want to avoid)
============================================
[what's something confusing or easy to get wrong
about this topic?]
Using = instead of == when checking a condition. A single = is
for assigning a value to a variable, while == is for comparing
two values. Writing "if score = 90:" causes a syntax error.

============================================
HOW THIS CONNECTS TO SOMETHING ELSE
============================================
[optional]
"""

"""
Module 2 — Lesson 3: Loops & Lists
Student: Russell C. Nunag
Date: Sept. 27, 2026

============================================
WHAT IS THIS TOPIC? (explain it like you're
teaching a friend who's never coded before)
============================================
[write your own explanation here]
A list is a container that holds multiple pieces of information in
one variable, like a row of labeled boxes lined up in order — for
example, a list of student names instead of one variable per
student.

============================================
KEY VOCABULARY
============================================
- list:a variable that stores multiple values in order, written
with square brackets.
- for loop:a loop that goes through each item in something one at a time, running the same code for each item
- while loop:a loop that continues to run as long as a certain condition is true
- index:the position of an item in a list, starting from 0
- iteration:each time a loop runs through an item in a list
(add more as needed)


============================================
MY OWN EXAMPLE(S)
============================================
Write at least one working example below that you
came up with yourself — not copied from class.
"""

# --- your code example goes here ---

students = ["Alice", "Bob", "Charlie", "David"]
scores = [92, 85, 96 , 74]

for i in range (len(students)):
    print(f"{students[i]} scored {scores[i]} on the test.")

    while scores[i] < 75:
        print(f"{students[i]} needs to improve.")
        break

"""
============================================
A MISTAKE I MADE (or one I want to avoid)
============================================
[what's something confusing or easy to get wrong
about this topic?]

Forgetting that lists start at index 0, not 1 — so
students[1] is actually the second student, not the first,
which caused me to grab the wrong item at first.

============================================
HOW THIS CONNECTS TO SOMETHING ELSE
============================================
[optional]
"""

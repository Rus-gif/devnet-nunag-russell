"""
Module 2 — Activity: File Sorting with os and shutil
Student: Russell C. Nunag
Date: Sept. 27, 2026

============================================
WHAT DID YOU BUILD? (explain in your own words)
============================================
[Paste your working script below first, then come back and explain
it here: what does your script do, and what rule did you use to
sort the files? e.g. by extension, by name, by date, etc.]

My script goes through every file inside a folder specified by the user
and sorts each one into a subfolder named after its file extension.
For example, all .pdf files end up in test_folder/pdf/, all .jpg files
end up in test_folder/jpg/, and so on. Files with no extension get
dropped into a folder called "no_extension" instead of being skipped
or causing an error.

============================================
KEY VOCABULARY
============================================
- os module: a built-in Python module that provides functions for interacting with the operating system
such as reading or writing files and navigating directories
- shutil module: a built-in Python module that provides functions for high-level file operations
such as copying, moving, and deleting files and directories
- file path:  the location of a file or folder in the file system, which can be absolute or relative
- directory: a folder in the file system used to organize and store files and other directories

============================================
YOUR SCRIPT
============================================
Paste the code you already wrote for this activity below.
"""

import os
import shutil

# --- paste your existing code here ---
folder = input("Enter the path of the folder to sort: ")

for filename in os.listdir(folder):
    file_path = os.path.join(folder, filename)

    if os.path.isfile(file_path):
        
        ext = os.path.splitext(filename)[1].lstrip(".").lower()
        if not ext:
            ext = "no_extension"

        dest_folder = os.path.join(folder, ext)
        os.makedirs(dest_folder, exist_ok=True)

        shutil.move(file_path, os.path.join(dest_folder, filename))



"""
============================================
A MISTAKE I MADE (or one I want to avoid)
============================================
[what tripped you up while building this? e.g. a path that didn't
exist, a file that got overwritten, something that didn't work the
way you expected at first]
When I switched to a full Windows path, Python threw a
SyntaxError: "(unicode error) 'unicodeescape' codec can't decode
bytes... malformed \\N character escape". This happened because
the path contained "New folder", and Python interpreted "\N" as
the start of a special unicode escape sequence rather than a
literal backslash-N. The fix was to mark the string as a raw
string by putting an "r" right before the opening quote:
r"F:\Russell\New folder\devnet-nunag-russell\test_folder". This
tells Python to treat every backslash as a literal character
instead of trying to interpret it.

============================================
HOW THIS CONNECTS TO SOMETHING ELSE
============================================
[optional: how is this similar to what real automation scripts do?
think about your own gradebook/attendance workflow — could something
like this save you time there?]
"""

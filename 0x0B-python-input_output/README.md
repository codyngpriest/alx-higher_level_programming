0x0B. Python - Input/Output

Tasks

0. Read file
This is a function that reads a text file (UTF8) and prints it to stdout:

1. Write to a file
This is a function that writes a string to a text file (UTF8) and returns the number of characters written:

2. Append to a file
This is a function that appends a string at the end of a text file (UTF8) and returns the number of characters added:

3. To JSON string
This is a function that returns the JSON representation of an object (string):

4. From JSON string to Object
This is a function that returns an object (Python data structure) represented by a JSON string:

5. Save Object to a file
This is a function that writes an Object to a text file, using a JSON representation:

6. Create object from a JSON file
This is a function that creates an Object from a “JSON file”

7. Load, add, save
This is a script that adds all arguments to a Python list, and then save them to a file

8. Class to JSON
This is a function that returns the dictionary description with simple data structure (list, dictionary, string, integer and boolean) for JSON serialization of an object

9. Student to JSON
This is a class Student that defines a student by
Public instance attributes:
first_name
last_name
age
Instantiation with first_name, last_name and age: def __init__(self, first_name, last_name, age):
Public method def to_json(self): that retrieves a dictionary representation of a Student instance (same as 8-class_to_json.py)
You are not allowed to import any module

10. Student to JSON with filter

This is a class Student that defines a student by: (based on 9-student.py)

Public instance attributes:
first_name
last_name
age
Instantiation with first_name, last_name and age: def __init__(self, first_name, last_name, age):
Public method def to_json(self, attrs=None): that retrieves a dictionary representation of a Student instance (same as 8-class_to_json.py):
If attrs is a list of strings, only attribute names contained in this list must be retrieved.
Otherwise, all attributes must be retrieved
You are not allowed to import any module

11. Student to disk and reload
This is a class Student that defines a student by: (based on 10-student.py)

12. Pascal's Triangle
This is a function def pascal_triangle(n): that returns a list of lists of integers representing the Pascal’s triangle of n

13. Search and update
This is a function that inserts a line of text to a file, after each line containing a specific string (see example):

14. Log parsing
This is a script that reads stdin line by line and computes metrics:

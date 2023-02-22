# Create a Python Program that perform following tasks for any problem of your choice:
# Task 1: Introduction
# Task 2: Terminal
# Task 3: Python Interpreter
# Task 4: Variables
# Task 5: Text Editor
# Task 6: Functions
# Task 7: Lists and Tuples
# Task 8: Conditional Statements
# Task 9: The For Loop
# Task 10: User Input and the While Loop

# Program to determine if Student will be prmoted or not

def courses_marks(courses):
    course_list = []
    for x in range(courses):
        name = input("Enter Course Name: ")
        marks = input("Enter Course Marks: ")
        course = (name, int(marks))
        course_list.append(course)
    return course_list 

def promoted(c_list):
    c = 0
    promoted = 0
    while c < len(c_list):
        if c_list[c][1] >= 50:
            promoted = promoted + 1
        c = c + 1
    
    if (promoted / len(c_list)) >= 0.75:
        print("You are promoted")
    else:
        print("Sorry, you are not promoted")

lis = courses_marks(2)
promoted(lis)
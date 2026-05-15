"""
Objects are used to access member functions and attributes.
"""

class Student():
    def __init__(self):
        print('Object Created')

"""
to create an object,
write an object name and after assignment operator, write class name with parenthesis.
if you want to pass default values to any member variables, it can be passed in these parenthesis.
notice that as the object is created the default constructor is invoked automatically.
"""
std = Student()
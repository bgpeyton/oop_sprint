"""
A module for handling school students related information
"""


class Student(object):
    """Basic student class"""
    
    # init is sort of like a constructor
    def __init__(self, name, ID, GPA): 
        self.name = name
        self._GPA = GPA # _protected (won't be imported with import *)
        self.__ID = ID # __private

    # Define a "getter"
    def get_GPA(self): 
        return self._GPA

    # Define a "setter"
    def set_GPA(self):
        self._GPA = GPA

    def __str__(self):
        return "Student Name " + self.name

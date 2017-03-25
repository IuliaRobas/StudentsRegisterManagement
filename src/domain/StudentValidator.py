'''
Created on Dec 16, 2016

@author: User
'''

from domain.Exceptions import FacultyException

class ValidatorException(FacultyException):
    pass

class StudentValidatorException(ValidatorException):
    pass

class StudentValidator:
    """
    Validator class for Student
    """
    def __init__(self):
        pass
    @staticmethod
    def validate(student):
        """
        Validate the given student
        
        input: 
            student - the student instance to be validated
        output: 
            None
        raises: 
            ValidationException in case of validation error
        """
#         errorMsg = []
#         if student.studentID < 0:
#             errorMsg.append("ID must be positive!")
#         if student.studentName == "":
#             errorMsg.append("Name can not be empty")
#         if errorMsg != []:
#             raise StudentValidatorException(errorMsg)
       
        if student.studentID < 0:
            raise StudentValidatorException("ID must be positive!")
        if student.studentName == "":
            raise StudentValidatorException("Name can not be empty")
        

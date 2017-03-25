'''
Created on Dec 16, 2016

@author: User
'''

from domain.Exceptions import FacultyException

class ValidatorException(FacultyException):
    pass

class DisciplineValidatorException(ValidatorException):
    pass

class DisciplineValidator:
    """
    Validator class for Discipline
    """
    def __init__(self):
        pass
    @staticmethod
    def validate(discipline):
        """
        Validate the given discipline
        
        input: 
            discipline - the discipline instance to be validated
        output: 
            None
        raises: 
            ValidationException in case of validation error
        """
#         errorMsg = []
#         if discipline.disciplineID < 0:
#             errorMsg.append("ID must be positive!")
#         if discipline.disciplineName == "":
#             errorMsg.append("Name can not be empty")
#         if errorMsg != []:
#             raise DisciplineValidatorException(errorMsg)
       
        if discipline.disciplineID < 0:
            raise DisciplineValidatorException("ID must be positive!")
        if discipline.disciplineName == "":
            raise DisciplineValidatorException("Name can not be empty")
        

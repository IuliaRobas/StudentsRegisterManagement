'''
Created on Dec 16, 2016

@author: User
'''
 
from domain.Exceptions import FacultyException 
from domain.Grade import Grade
 
class ValidatorException(FacultyException):
    pass

class GradeValidatorException(ValidatorException):
    pass

class GradeValidator:
    """
        Validator class for grades
    """
    @staticmethod
    def validate(grade):
        """
        Validate the given grade
         
        input: 
            grade - the grade to be validated
        output: 
            None
        raises:
            ValidationException in case of validation error
        """
        if grade.studentID < 0:
            raise GradeValidatorException("Student ID must be positive!")
        if grade.disciplineID < 0:
            raise GradeValidatorException("Discipline ID must be positive!")
        if grade.gradeValue < 0 or grade.gradeValue > 10:
            raise GradeValidatorException("Grade value must be between 1 and 10")

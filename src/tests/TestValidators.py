'''
Created on Dec 17, 2016

@author: User
'''
import unittest
from domain.StudentValidator import StudentValidator, StudentValidatorException
from domain.DisciplineValidator import DisciplineValidator, DisciplineValidatorException
from domain.Student import Student
from domain.Discipline import Discipline


class TestDisciplineValidator(unittest.TestCase):


    def setUp(self):
        self.__validator = DisciplineValidator()
        
    def tearDown(self):
        del self.__validator

    def testName(self):
        "Discipline ID must be positive"       
        
        discipline = Discipline(-1, "Ana")
        try:
            self.__validator.validate(discipline)
        except DisciplineValidatorException:
            pass
        
        "Discipline name cannot be empty"
        discipline = Discipline(1, "")
        try:
            self.__validator.validate(discipline)
        except DisciplineValidatorException:
            pass
        
class TestStudentValidator(unittest.TestCase):


    def setUp(self):
        self.__validator = StudentValidator()
        
    def tearDown(self):
        del self.__validator

    def testName(self):
        "Student ID must be positive"       
        
        discipline = Student(-1, "Ana")
        try:
            self.__validator.validate(discipline)
        except StudentValidatorException:
            pass
        
        "Student name cannot be empty"
        discipline = Student(1, "")
        try:
            self.__validator.validate(discipline)
        except StudentValidatorException:
            pass
    #testGradeValidator

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
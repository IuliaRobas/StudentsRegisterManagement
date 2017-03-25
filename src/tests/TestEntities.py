'''
Created on Dec 17, 2016

@author: User
'''
import unittest
from domain.Student import Student
from domain.Discipline import Discipline
from domain.Grade import Grade

class TestStudent(unittest.TestCase):


    def setUp(self):
        self.__student = Student(1, "Ana")
        

    def tearDown(self):
        del self.__student


    def testName(self):
        assert(self.__student.studentName == "Ana")
        assert(self.__student.studentID == 1)
        
class TestDiscipline(unittest.TestCase):


    def setUp(self):
        self.__discipline = Discipline(1, "Algebra")
        

    def tearDown(self):
        del self.__discipline


    def testName(self):
        assert(self.__discipline.disciplineName == "Algebra")
        
class TestGrade(unittest.TestCase):


    def setUp(self):
        self.__grade = Grade(1, 2, 10)
        

    def tearDown(self):
        del self.__grade


    def testName(self):
        assert(self.__grade.disciplineID == 1)
        assert(self.__grade.studentID == 2)
        assert(self.__grade.gradeValue == 10)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
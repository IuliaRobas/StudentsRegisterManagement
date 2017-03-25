'''
Created on Dec 17, 2016

@author: User
'''
import unittest
from controller.StudentController import StudentController,\
    StudentControllerException
from domain.Student import Student
from repository.StudentRepository import StudentRepository
from domain.StudentValidator import StudentValidatorException


class TestStudentController(unittest.TestCase):


    def setUp(self):
        self.__repo = StudentRepository()
        self.__ctrl = StudentController(self.__repo)
        self.__student1 = Student(1, "Anna")
        self.__student2 = Student("", "Mary")

    def tearDown(self):
        del self.__repo
        del self.__ctrl
        del self.__student1
        del self.__student2 

    def testController(self):
        assert(len(self.__ctrl.getAll())==0)
        self.__ctrl.add(self.__student1.studentID, self.__student1.studentName)
        assert(len(self.__ctrl.getAll())==1)
        try:
            self.__ctrl.add(self.__student2.studentID, self.__student2.studentName)
        except StudentControllerException:
            pass
        
    
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
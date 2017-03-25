'''
Created on Dec 17, 2016

@author: User
'''
import unittest

from repository.StudentRepository import StudentRepository
from repository.DisciplineRepository import DisciplineRepository
from repository.GradeRepository import GradeRepository 
from domain.Student import Student
from domain.Discipline import Discipline
from domain.Grade import Grade

class TestStudentRepository(unittest.TestCase):


    def setUp(self):
        self.__repo = StudentRepository()
        self.__student = Student(1,"Anna")    


    def tearDown(self):
        del self.__repo
        del self.__student

    def testRepository(self):
        assert(len(self.__repo.getAll())==0)
        self.__repo.add(self.__student)
        assert(len(self.__repo.getAll())==1)
        
class TestDisciplineRepository(unittest.TestCase):


    def setUp(self):
        self.__repo = DisciplineRepository()
        self.__discipline = Discipline(1,"Anna")    


    def tearDown(self):
        del self.__repo
        del self.__discipline

    def testRepository(self):
        assert(len(self.__repo.getAll())==0)
        self.__repo.add(self.__discipline)
        assert(len(self.__repo.getAll())==1)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
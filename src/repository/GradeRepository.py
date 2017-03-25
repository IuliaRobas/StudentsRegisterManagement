'''
Created on Nov 28, 2016

@author: peacegabi
'''
from domain.Exceptions import FacultyException
from copy import deepcopy

class GradeRepositoryException(FacultyException):
    pass

class GradeRepository:
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self._grades ={}
        self.__undoList = []
        self.__redoList = []
      
    def undo(self):
        try:
            self._grades = self.__undoList.pop()
        except IndexError:
            raise GradeRepositoryException("There are no operations that you can undo!")
        
    def redo(self):
        try:
            self._grades = self.__redoList.pop()
        except IndexError:
            raise GradeRepositoryException("There are no operations that you can redo!")
        
    def add(self, grade):
#         if grade.gradeID in self._grades:
#             raise GradeRepositoryException("ID already existent!")
        self.__undoList.append(deepcopy(self._grades))
        self._grades[grade.gradeID] = grade
        self.__redoList.append(deepcopy(self._grades))
        
    def remove(self, grade_id):
        if grade_id not in self._grades:
            raise GradeRepositoryException("ID is inexistent!")
        self.__undoList.append(deepcopy(self._grades))
        del self._grades[grade_id]
        self.__redoList.append(deepcopy(self._grades))
        
    def update(self, grade):
        if grade.gradeID not in self._grade:
            raise GradeRepositoryException("ID is inexistent!")
        self.__undoList.append(deepcopy(self._grades))
        self._grades[grade.gradeID] = grade
        self.__redoList.append(deepcopy(self._grades))
        
    def getAllGrades(self):
        return [x for x in self._grades.values()]
    
    def getAllforStudent(self, studentID):
          

        result = []
        for grade in self._grades:
            if grade.studentID == studentID:
                result.append(studentID)
        return result
    
    def findById(self,grade_id):
        if grade_id not in self._grades:
            raise GradeRepositoryException("ID is inexistent!")
        return self._grades[grade_id]
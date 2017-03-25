
from domain.Exceptions import FacultyException
from copy import deepcopy

class RepositoryException(FacultyException):
    pass

class StudentRepositoryException(RepositoryException):
    pass

class StudentRepository(object):
    '''
    classdocs
    '''
    def __init__(self):
        '''
        Constructor
        '''
        self._students ={}
        self.__undoList = []
        self.__redoList = []
      
    def undo(self):
        try:
            self._students = self.__undoList.pop()
        except IndexError:
            raise StudentRepositoryException("There are no operations that you can undo!")
        
    def redo(self):
        try:
            self._students = self.__redoList.pop()
        except IndexError:
            raise StudentRepositoryException("There are no operations that you can redo!")
          
    def add(self, student):
        if student.studentID in self._students:
            raise StudentRepositoryException("Student ID already existent!")
        self.__undoList.append(deepcopy(self._students))
        self._students[student.studentID] = student
        self.__redoList.append(deepcopy(self._students))
        
    def remove(self, student_id):
        if student_id not in self._students:
            raise StudentRepositoryException("Student ID is inexistent!")
        self.__undoList.append(deepcopy(self._students))
        del self._students[student_id]
        self.__redoList.append(deepcopy(self._students))
        
    def update(self, student):
        if student.studentID not in self._students:
            raise StudentRepositoryException("Student ID is inexistent!")
        self.__undoList.append(deepcopy(self._students))
        self._students[student.studentID] = student
        self.__redoList.append(deepcopy(self._students))
        
    def getNameByID(self, studentID):
        studs = self.getAll()
        for stud in studs:
            if stud.studentID == studentID:
                return stud.studentName
        
    def getAll(self):
        return [x for x in self._students.values()]
    
    def findByID(self,student_id):
        if student_id not in self._students:
            return None
            #raise StudentRepositoryException("Student ID is inexistent!")
        return self._students[student_id]
        


from domain.Grade import Grade
from repository.GradeRepository import GradeRepository
from domain.Exceptions import FacultyException

class FileRepositoryException(FacultyException):
    pass

class GradeFileRepositoryException(FileRepositoryException):
    pass

class GradeFileRepository(GradeRepository):
    def __init__(self, fileName):        
        
        GradeRepository.__init__(self)
        self.__fileName = fileName
        self.__loadFromFile()
    
    def add(self, grade):
        GradeRepository.add(self, grade)
        self.__storeToFile()
    
    def remove(self, gradeID):
        GradeRepository.remove(self, gradeID)
        self.__storeToFile()       
    
    def update(self, gradeID, newName):
        GradeRepository.update(self, gradeID, newName)
        self.__storeToFile()
    
    def __loadFromFile(self):
        try:
            f = open(self.__fileName, "r")
            line = f.readline().strip()
            while line != "":
                attrs = line.split(",")
                grade = Grade(int(attrs[0]), int(attrs[1]), int(attrs[2]))
        
                GradeRepository.add(self, grade)
                line = f.readline().strip()
                                 
        except IOError:
            raise FileRepositoryException()
        finally:
            f.close()

        
    def __storeToFile(self):
        f = open(self.__fileName, "w")
        sts = GradeRepository.getAllGrades(self)
        for st in sts:
            strf = str(stdisciplineID) + "," + str(st.studentID) + "," +str(st.gradeValue)
            strf = strf + "\n"
            f.write(strf)
        f.close()

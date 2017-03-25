

from domain.Student import Student
from repository.StudentRepository import StudentRepository
from domain.Exceptions import FacultyException

class FileRepositoryException(FacultyException):
    pass

class StudentFileRepositoryException(FileRepositoryException):
    pass

class StudentFileRepository(StudentRepository):
    def __init__(self, fileName):        
        
        StudentRepository.__init__(self)
        self.__fileName = fileName
        self.__loadFromFile()
    
    def add(self, student):
        StudentRepository.add(self, student)
        self.__storeToFile()
    
    def remove(self, studentID):
        StudentRepository.remove(self, studentID)
        self.__storeToFile()       
    
    def update(self, studentID, newName):
        StudentRepository.update(self, studentID, newName)
        self.__storeToFile()
    
    def __loadFromFile(self):
        try:
            f = open(self.__fileName, "r")
            line = f.readline().strip()
            while line != "":
                attrs = line.split(",")
                student = Student(int(attrs[0]), attrs[1])
                StudentRepository.add(self, student)
                line = f.readline().strip()
                                 
        except IOError:
            raise StudentFileRepositoryException()
        finally:
            f.close()

        
    def __storeToFile(self):
        f = open(self.__fileName, "w")
        sts = StudentRepository.getAll(self)
        for st in sts:
            strf = str(st.studentID) + "," + st.studentName
            strf = strf + "\n"
            f.write(strf)
        f.close()

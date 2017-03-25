
from repository.StudentRepository import StudentRepository

import pickle

class StudentPickleFileRepository(StudentRepository):
    
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
    

#     def __storeAStudent(self):
#         f = open(self.__fName, "wb")        
#         student = Student(1, "Ana")
#         pickle.dump(student, f)
#         f.close()
        
    def __loadFromFile(self):
        f = open(self.__fileName, "rb")
        
        """
        You cannot unpickle an empty file
            - EOFError means the file is empty
            - Exception means no file, not accessible and so on...
            - finally makes sure we close the input file, regardless of error
        """
        
        try:
            self._students = pickle.load(f)
        except EOFError:
            self._students = {}
        except Exception as e:
            raise e
        finally:
            f.close()

    def __storeToFile(self):
        f = open(self.__fileName, "wb")
        pickle.dump(self._students, f)
        f.close()
        
        

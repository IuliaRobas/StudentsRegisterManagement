
from repository.GradeRepository import GradeRepository

import pickle

class GradePickleFileRepository(GradeRepository):
    
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
    

#     def __storeAGrade(self):
#         f = open(self.__fName, "wb")        
#         grade = Grade(1, "Ana")
#         pickle.dump(grade, f)
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
            self._grades = pickle.load(f)
        except EOFError:
            self._grades = {}
        except Exception as e:
            raise e
        finally:
            f.close()

    def __storeToFile(self):
        f = open(self.__fileName, "wb")
        pickle.dump(self._grades, f)
        f.close()
        
        

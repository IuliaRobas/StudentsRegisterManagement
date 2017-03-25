
from repository.DisciplineRepository import DisciplineRepository

import pickle

class DisciplinePickleFileRepository(DisciplineRepository):
    
    def __init__(self, fileName):
    
        DisciplineRepository.__init__(self)
        self.__fileName = fileName
        self.__loadFromFile()
    
    def add(self, discipline):
        DisciplineRepository.add(self, discipline)
        self.__storeToFile()
    
    def remove(self, disciplineID):
        DisciplineRepository.remove(self, disciplineID)
        self.__storeToFile()       
    
    def update(self, disciplineID, newName):
        DisciplineRepository.update(self, disciplineID, newName)
        self.__storeToFile()
    

#     def __storeADiscipline(self):
#         f = open(self.__fName, "wb")        
#         discipline = Discipline(1, "Ana")
#         pickle.dump(discipline, f)
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
            self._disciplines = pickle.load(f)
        except EOFError:
            self._disciplines = {}
        except Exception as e:
            raise e
        finally:
            f.close()

    def __storeToFile(self):
        f = open(self.__fileName, "wb")
        pickle.dump(self._disciplines, f)
        f.close()
        
        

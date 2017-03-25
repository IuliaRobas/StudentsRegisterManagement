

from domain.Discipline import Discipline
from repository.DisciplineRepository import DisciplineRepository
from domain.Exceptions import FacultyException

class FileRepositoryException(FacultyException):
    pass

class DisciplineFileRepositoryException(FileRepositoryException):
    pass

class DisciplineFileRepository(DisciplineRepository):
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
    
    def __loadFromFile(self):
        try:
            f = open(self.__fileName, "r")
            line = f.readline().strip()
            while line != "":
                attrs = line.split(",")
                discipline = Discipline(int(attrs[0]), attrs[1])
                DisciplineRepository.add(self, discipline)
                line = f.readline().strip()
                                 
        except IOError:
            raise FileRepositoryException()
        finally:
            f.close()

        
    def __storeToFile(self):
        f = open(self.__fileName, "w")
        sts = DisciplineRepository.getAll(self)
        for st in sts:
            strf = str(st.disciplineID) + "," + st.disciplineName
            strf = strf + "\n"
            f.write(strf)
        f.close()

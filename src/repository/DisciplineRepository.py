
from domain.Exceptions import FacultyException
from copy import deepcopy

class RepositoryException(FacultyException):
    pass

class DisciplineRepositoryException(RepositoryException):
    pass

class DisciplineRepository(object):
    '''
    classdocs
    '''
    def __init__(self):
        '''
        Constructor
        '''
        self._disciplines ={}
        self.__undoList = []
        self.__redoList = []
      
    def undo(self):
        try:
            self._disciplines = self.__undoList.pop()
        except IndexError:
            raise DisciplineRepositoryException("There are no operations that you can undo!")
        
    def redo(self):
        try:
            self._disciplines = self.__redoList.pop()
        except IndexError:
            raise DisciplineRepositoryException("There are no operations that you can redo!")
        
          
    def add(self, discipline):
        if discipline.disciplineID in self._disciplines:
            raise DisciplineRepositoryException("ID already existent!")
        self.__undoList.append(deepcopy(self._disciplines))
        self._disciplines[discipline.disciplineID] = discipline
        self.__redoList.append(deepcopy(self._disciplines))
        
    def remove(self, discipline_id):
        if discipline_id not in self._disciplines:
            raise DisciplineRepositoryException("ID is inexistent!")
        self.__undoList.append(deepcopy(self._disciplines))
        del self._disciplines[discipline_id]
        self.__redoList.append(deepcopy(self._disciplines))
        
    def update(self, discipline):
        if discipline.disciplineID not in self._disciplines:
            raise DisciplineRepositoryException("ID is inexistent!")
        self.__undoList.append(deepcopy(self._disciplines))
        self._disciplines[discipline.disciplineID] = discipline
        self.__redoList.append(deepcopy(self._disciplines))
        
    def getNameByID(self, disciplineID):
        discs = self.getAll()
        for disc in discs:
            if disc.disciplineID == disciplineID:
                return disc.disciplineName    
    def getAll(self):
        return [x for x in self._disciplines.values()]
    def getAllIDs(self):
        return [x for x in self._disciplines.keys()]
    def findByID(self,discipline_id):
        if discipline_id not in self._disciplines:
            return None
            #raise DisciplineRepositoryException("ID is inexistent!")
        return self._disciplines[discipline_id]
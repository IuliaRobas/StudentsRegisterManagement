
from domain.Discipline import Discipline
from domain.DisciplineValidator import DisciplineValidator


from domain.Exceptions import FacultyException

class ControllerException(FacultyException):
    pass

class DisciplineControllerException(ControllerException):
    pass

class DisciplineController:
    """
      Class responsible with the use cases related to Discipline CRUD
      GRASP Controller
    """
    def __init__(self, disciplineRepo):
        self.__disciplineRepo = disciplineRepo
        self.__validator = DisciplineValidator
        
    def undo(self):
        self.__disciplineRepo.undo()
                
    def redo(self):
        self.__disciplineRepo.redo()
        
    def add(self, disciplineID, disciplineName):   
        try:
            disciplineID = int(disciplineID)
        except ValueError:
            raise DisciplineControllerException ("Discipline ID must be an integer")
        if not disciplineName.isalpha():
            raise DisciplineControllerException("Name must contain only letters")            
        discipline = Discipline(disciplineID, disciplineName)
        self.__validator.validate(discipline)
        self.__disciplineRepo.add(discipline)
        
    def update(self, disciplineID, newName): 
        try:
            disciplineID = int(disciplineID)
        except ValueError:
            raise DisciplineControllerException ("Discipline ID must be an integer")  
        if not newName.isalpha():
            raise DisciplineControllerException("Name must contain only letters")  
        newSt = Discipline(disciplineID, newName)
        self.__validator.validate(newSt)
        self.__disciplineRepo.update(newSt)
        
    def getAll(self):
        return self.__disciplineRepo.getAll()
    
    def setUp(self):
        self.__disciplineRepo.add(Discipline(1,"Algebra"))
        self.__disciplineRepo.add(Discipline(2,"Mathematical Analysis"))
        self.__disciplineRepo.add(Discipline(3,"Fundamentals of Programming"))
        self.__disciplineRepo.add(Discipline(4,"Computational Logic"))
        self.__disciplineRepo.add(Discipline(5,"Computer System Architecture"))
        self.__disciplineRepo.add(Discipline(14, "Sports"))
        
    def remove(self, disciplineID):     
        try:
            disciplineID = int(disciplineID)
        except ValueError:
            raise DisciplineControllerException ("Discipline ID must be an integer")   
        return self.__disciplineRepo.remove(disciplineID)
    
    def searchDisciplinesByName(self, disciplineName):
        if not disciplineName.isaplha():
            raise DisciplineControllerException("Discipline name must contain only letters")  
        
        disciplines = self.__disciplineRepo.getAll()
        if disciplineName == "":
            return disciplines
        studs = []
        for discipline in disciplines:
            if disciplineName.lower() in discipline.disciplineName.lower():
                studs.append(discipline.disciplineName)
        return studs
    
    def searchDisciplinesByID(self, disciplineID):
        disciplines = self.__disciplineRepo.getAll()
        if disciplineID == "":
            return disciplines
        try:
            disciplineID = int(disciplineID)
        except ValueError:
            raise DisciplineControllerException ("Discipline ID must be an integer")  
        
        studs = []
        for discipline in disciplines:
            if str(disciplineID) in str(discipline.disciplineID):
                studs.append(discipline.disciplineName)
                
        return studs
    def search(self, criteria):
        """
          Search disciplines with name containing criteria
          criteria string
          return list of disciplines, where the name contains criteria
        """
        disciplineList = self.__disciplineRepo.getAll()
        if criteria == "":
            return disciplineList

        rez = []
        for st in disciplineList:
            if criteria in st.getName():
                rez.append(st)
        return rez


      

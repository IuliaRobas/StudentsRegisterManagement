
from domain.Student import Student
from domain.StudentValidator import StudentValidator

from utilities.utilFunctions import filterf

from domain.Exceptions import FacultyException
from repository.StudentRepository import StudentRepositoryException

class ControllerException(FacultyException):
    pass

class StudentControllerException(ControllerException):
    pass

class StudentController:
    """
      Class responsible with the use cases related to Student CRUD
      GRASP Controller
    """
    def __init__(self, studentRepo):
        self.__studentRepo = studentRepo
        self.__validator = StudentValidator

    def undo(self):
        self.__studentRepo.undo()
                
    def redo(self):
        self.__studentRepo.redo()
        
    def add(self, studentID, studentName):   
        try:
            studentID = int(studentID)
        except ValueError:
            raise StudentControllerException ("Student ID must be an integer")
        if not studentName.isalpha():
            raise StudentControllerException("Name must contain only letters")            
        student = Student(studentID, studentName)
        self.__validator.validate(student)
        self.__studentRepo.add(student)
        
    def update(self, studentID, newName): 
        try:
            studentID = int(studentID)
        except ValueError:
            raise StudentControllerException ("Student ID must be an integer")  
        if not newName.isaplha():
            raise StudentControllerException("Name must contain only letters")  
        newSt = Student(studentID, newName)
        self.__validator.validate(newSt)
        self.__studentRepo.update(newSt)
        
    def getAll(self):
        return self.__studentRepo.getAll()
    
    def setUp(self):
        self.__studentRepo.add(Student(1, "Ana"))
        self.__studentRepo.add(Student(2, "Bianca"))
        self.__studentRepo.add(Student(3, "Andrei"))
        self.__studentRepo.add(Student(4, "Cristian"))
        self.__studentRepo.add(Student(5, "Diana"))
        self.__studentRepo.add(Student(6, "Mara"))
        
    def remove(self, studentID):     
        try:
            studentID = int(studentID)
        except ValueError:
            raise StudentControllerException ("Student ID must be an integer")   
        return self.__studentRepo.remove(studentID)
    
    
   
    def searchStudentsByName(self, studentName):
        if not studentName.isalpha():
            raise StudentControllerException("Student name must contain only letters")  
        
        students = self.__studentRepo.getAll()
        if studentName == "":
            return students
        studs = []
#         def f(studentName):
#             return studentName in students
        print(studentName)
        return filterf(lambda st: st.studentName.lower()==studentName.lower(),students)
#         for student in students:
#             if studentName.lower() in student.studentName.lower():
#                 studs.append(student.studentName)
#         return studs
    
    def searchStudentsByID(self, studentID):
        students = self.__studentRepo.getAll()
        if studentID == "":
            return students
        try:
            studentID = int(studentID)
        except ValueError:
            raise StudentControllerException ("Student ID must be an integer")  
        
        studs = []
        for student in students:
            if str(studentID) in str(student.studentID):
                studs.append(student.studentName)
        return studs
            
    def search(self, criteria):
        """
          Search students with name containing criteria
          criteria string
          return list of students, where the name contains criteria
        """
        studentList = self.__studentRepo.getAll()
        if criteria == "":
            return studentList

        rez = []
        for st in studentList:
            if criteria in st.getName():
                rez.append(st)
        return rez


      

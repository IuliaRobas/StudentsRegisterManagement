from domain.StudentValidator import StudentValidator
from domain.DisciplineValidator import DisciplineValidator
from domain.GradeValidator import GradeValidator

from repository.StudentRepository import StudentRepository
from repository.GradeRepository import GradeRepository
from repository.DisciplineRepository import DisciplineRepository

from controller.StudentController import StudentController
from controller.DisciplineController import DisciplineController
from controller.GradeController import GradeController

from repository.StudentFileRepository import StudentFileRepository
from repository.DisciplineFileRepository import DisciplineFileRepository
from repository.GradeFileRepository import GradeFileRepository

from repository.StudentPickleFileRepository import StudentPickleFileRepository
from repository.DisciplinePickleFileRepository import DisciplinePickleFileRepository
from repository.GradePickleFileRepository import GradePickleFileRepository

from utilities.PersistancyHandler import PersistancyHandler


from ui.Console import ConsoleUI
 
"""
    1. Set up entity validators
"""
 
studentValidator = StudentValidator()
disciplineValidator = DisciplineValidator()
gradeValidator = GradeValidator()
 
# """
#     2. Initialize the repositories
# """
# studentRepo = StudentFileRepository("C:\\Users\\PC\\Desktop\\University\\Fundamentals of Programming\\Fundamentals of Programming_LAB\\Homework_LAB05-07\\Final\\data\\Students")
# #studentRepo = StudentRepository()
# disciplineRepo = DisciplineFileRepository("C:\\Users\\PC\\Desktop\\University\\Fundamentals of Programming\\Fundamentals of Programming_LAB\\Homework_LAB05-07\\Final\\data\\Disciplines")
# # gradeRepo = GradeCSVFileRepository(studentRepo, "grades.txt")
# gradeRepo = GradeFileRepository("C:\\Users\\PC\\Desktop\\University\\Fundamentals of Programming\\Fundamentals of Programming_LAB\\Homework_LAB05-07\\Final\\data\\Grades")
#  
# """
#     3. Initialize GRASP controllers
# """
# studentController = StudentController(studentRepo)
# disciplineController = DisciplineController(disciplineRepo)
# gradeController = GradeController(gradeRepo, disciplineRepo, studentRepo)
#  
#  
# """
#     4. Start up the UI
# """
# ui = ConsoleUI(studentController, disciplineController, gradeController)
# ui.runApp()

while True:
        print("\nChoose what kind of repository you want to use \n")
        print("1 - inmemory repository" )
        print("2 - text file repository")
        print("3 - binary file repository")
        print("0 - to exit")
        repository_mode = int(input("\nYour choice for repository is: "))
        if repository_mode == 1:
            studentValidator = StudentValidator()
            disciplineValidator = DisciplineValidator()
            gradeValidator = GradeValidator()
 
            studentRepo = StudentRepository()
            disciplineRepo = DisciplineRepository()
            gradeRepo = GradeRepository()
 
            studentController = StudentController(studentRepo)
            disciplineController = DisciplineController(disciplineRepo)
            gradeController = GradeController(gradeRepo, disciplineRepo, studentRepo)
             
            ui = ConsoleUI(studentController, disciplineController, gradeController)
            opt = ui.runApp()
            if opt==0:
                break
             
        elif repository_mode == 2:
            studentValidator = StudentValidator()
            disciplineValidator = DisciplineValidator()
            gradeValidator = GradeValidator()
 
            studentRepo = StudentFileRepository("C:\\Users\\Utilizator\\Desktop\\University\\Semester 1\\FP\\Final\\data\\Students")
            disciplineRepo = DisciplineFileRepository("C:\\Users\\Utilizator\\Desktop\\University\\Semester 1\\FP\\Final\\data\\Disciplines")
            gradeRepo = GradeFileRepository("C:\\Users\\Utilizator\\Desktop\\University\\Semester 1\\FP\\Final\\data\\Grades")
 
            studentController = StudentController(studentRepo)
            disciplineController = DisciplineController(disciplineRepo)
            gradeController = GradeController(gradeRepo, disciplineRepo, studentRepo)
             
            ui = ConsoleUI(studentController, disciplineController, gradeController)
            opt=ui.runApp()
            if opt==0:
                break
        elif repository_mode == 3:
            studentValidator = StudentValidator()
            disciplineValidator = DisciplineValidator()
            gradeValidator = GradeValidator()
 
            studentRepo = StudentPickleFileRepository("C:\\Users\\PC\\Desktop\\University\\Fundamentals of Programming\\Fundamentals of Programming_LAB\\Homework_LAB05-07\\Final\\data\\Students.pickle")
            disciplineRepo = DisciplinePickleFileRepository("C:\\Users\\PC\\Desktop\\University\\Fundamentals of Programming\\Fundamentals of Programming_LAB\\Homework_LAB05-07\\Final\\data\\Disciplines.pickle")
            gradeRepo = GradePickleFileRepository("C:\\Users\\PC\\Desktop\\University\\Fundamentals of Programming\\Fundamentals of Programming_LAB\\Homework_LAB05-07\\Final\\data\\Grades.pickle")
 
            studentController = StudentController(studentRepo)
            disciplineController = DisciplineController(disciplineRepo)
            gradeController = GradeController(gradeRepo, disciplineRepo, studentRepo)
             
            ui = ConsoleUI(studentController, disciplineController, gradeController)
            opt=ui.runApp()
            if opt==0:
                break
        elif repository_mode==0:
            print("Thank you for using the app! Bye!")
            break     
        else:
            print("Your option is not valid! Please type in again!")
            
                    
# persistancyHandler = PersistancyHandler()
# [studentRepo, disciplineRepo, gradeRepo] = persistancyHandler.createPersistancySource()
# studentController = StudentController(studentRepo)
# disciplineController = DisciplineController(disciplineRepo)
# gradeController = GradeController(gradeRepo, disciplineRepo, studentRepo)
#              
# ui = ConsoleUI(studentController, disciplineController, gradeController)
# opt = ui.runApp()
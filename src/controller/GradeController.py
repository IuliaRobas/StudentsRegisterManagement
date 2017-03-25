'''
Created on Nov 21, 2016

@author: Arthur
'''

from domain.Grade import Grade
from domain.GradeValidator import GradeValidator
from domain.Exceptions import FacultyException

class ControllerException(FacultyException):
    pass

class GradeControllerException(ControllerException):
    pass

class GradeController:
    """
    Controller class for student grades 
    """
    def __init__(self, gradeRepo, disciplineRepo, studentRepo ):
        """
          Initialise
          gradeRepo - GradeRepository
          gradeValidator - GradeValidator
          studentRepo - StudentRepository
        """
        self.__gradeRepo = gradeRepo
        self.__disciplineRepo = disciplineRepo
        self.__studentRepo = studentRepo
        self.__validator = GradeValidator
        
    def undo(self):
        self.__gradeRepo.undo()
        
    def redo(self):
        self.__gradeRepo.redo()
        
    def add(self, disciplineID, studentID, gradeValue):
        """
        Assign a grade for a student at a given discipline

        input:
            studentId - id of the student receiving the grade
            discipline - the discipline they are graded in
            gradeValue - numerical value of the grade. Must be an integer between 1 and 10
        output:
            The created Grade object
        raises:
            ValidateException for invalid gradeValue
            StudentNotFound if there is no student for the given id
        """
#         student = self.__studentRepo.find(studentId)
#         if student == None:
#             raise StudentNotFoundException("Student with id = " + str(studentId) + " not found.")

        """
            Create new Grade object
            Validate it
            Store it
            Return it
        """
        try:
            studentID = int(studentID)
        except ValueError:
            raise GradeControllerException ("Student ID must be an integer")
        if self.__studentRepo.findByID(studentID) == None:
            
            raise GradeControllerException("Inexistent student ID")
        try:
            disciplineID = int(disciplineID)
        except ValueError:
            raise GradeControllerException ("Discipline ID must be an integer")
        if self.__disciplineRepo.findByID(disciplineID) == None:
            raise GradeControllerException("Inexistent discipline ID")
        
        try:
            gradeValue = int(gradeValue)
        except ValueError:
            raise GradeControllerException("Grade Value must be an integer")
        newGrade = Grade(studentID, disciplineID, gradeValue)
        self.__validator.validate(newGrade)
        self.__gradeRepo.add(newGrade)
        
    def getAll(self):
        return self.__gradeRepo.getAllGrades()
    
    def setUp(self):
        self.__gradeRepo.add(Grade(1,2,10))
        self.__gradeRepo.add(Grade(1,3,9))
        self.__gradeRepo.add(Grade(2,2,10))
        self.__gradeRepo.add(Grade(2,2,8))
        self.__gradeRepo.add(Grade(3,4,4))
        self.__gradeRepo.add(Grade(4,4,2))
        self.__gradeRepo.add(Grade(4,4,1))
    
    
    def EnrolledStudentsAtDiscipline(self, disciplineID):
        grades = self.__gradeRepo.getAllGrades()
        studs = []
        for grade in grades:
            if grade.disciplineID == disciplineID:
                studs.append(grade.studentID)
        return studs
    
    def EnrolledStudentsAtDisciplineAlphabetically(self, disciplineID):
        studsIDs = self.EnrolledStudentsAtDiscipline(disciplineID)    
        studsnames = []
        for studID in studsIDs:
            studname = self.__studentRepo.getNameByID(studID)
            studsnames.append(studname)
        studsnames = sorted(studsnames)
        return studsnames
    
    def getAverageForStudent(self, studentID):
        grades = self.__gradeRepo.getAllGrades()
        studgrades = []
        for grade in grades:
            if grade.studentID == studentID:
                studgrades.append(grade.gradeValue)                
        avg = float(sum(studgrades))/max(len(studgrades),1)
        return avg
                   
    def EnrolledStudentsAtDisciplineDescending(self, disciplineID):
        studsIDs = self.EnrolledStudentsAtDiscipline(disciplineID) 
        studs = []
        for studID in studsIDs:
            studname = self.__studentRepo.getNameByID(studID)
            avg = self.getAverageForStudent(studID)
            studs.append([studname, avg])
            
        studs = sorted(studs, key= lambda x:x[1], reverse=True)
        return studs
    
    
                
#     def getGradedDisciplineIDs(self):
#         discIDs = []
#         grades = self.__gradeRepo.getAll()
#         for grade in grades:
#             discIDs.append(grade.discipineID)
#         return discIDs
    
    def getAverageForStudentAtDiscipline(self, studentID, disciplineID):
        grades = self.__gradeRepo.getAllGrades()
        avg = []
        for grade in grades:
            if grade.discipineID == disciplineID and grade.studentID == studentID:
                avg.append(grade.gradeValue)
        avg = float(sum(avg))/max(len(avg),1)
        return avg
    
    def BestStudents(self):
        studentIDs = self.GradedStudentIDs()
        disciplineIDs = self.GradedDisciplineIDs()
        best = []
        for studentID in studentIDs:
            avgTotal = []
            for disciplineID in disciplineIDs:
                avgAtDisc = self.getAverageForStudentAtDiscipline(studentID, disciplineID)
                if avgAtDisc > 0:
                    avgTotal.append(avgAtDisc)
            avgTotal = float(sum(avgTotal))/max(len(avgTotal),1)
            best.append([self.__studentRepo.getNameByID(studentID), avgTotal])
        best = sorted(best, key= lambda x:x[1], reverse=True)
        return best
     
    def BestDisciplines(self):
        studentIDs = self.GradedStudentIDs()
        disciplineIDs = self.GradedDisciplineIDs()
        best = []  
        for disciplineID in disciplineIDs:
            avgTotal = []
            for studentID in studentIDs:
                avgAtDisc = self.getAverageForStudentAtDiscipline(studentID, disciplineID)
                if avgAtDisc > 0:
                    avgTotal.append(avgAtDisc)
            avgTotal = float(sum(avgTotal))/max(len(avgTotal),1)
            best.append([self.__disciplineRepo.getNameByID(disciplineID), avgTotal])
        best = sorted(best, key= lambda x:x[1], reverse=True)
        return best
            
                
                    
    def GradedStudentIDs(self):
        grades = self.__gradeRepo.getAllGrades()
        studIDs = []
        for grade in grades:
            if grade.studentID not in studIDs:
                studIDs.append(grade.studentID)
        return studIDs
    
    def GradedDisciplineIDs(self):
        grades = self.__gradeRepo.getAllGrades()
        disciplines = []
        for grade in grades:
            if grade.discipineID not in disciplines:
                disciplines.append(grade.discipineID)
        return disciplines
    
    def FailingStudents(self):
        students=self.GradedStudentIDs()
        disciplines=self.GradedDisciplineIDs()
        fail=[]
        for s in students:
            for d in disciplines:
                avg=self.getAverageForStudentAtDiscipline(s, d)
                if avg<5 and avg>0:
                    if s not in fail:
                        fail.append(s)
        return fail
    
#     def FailingStudents(self):
#         failing = []
#         disciplinesIDs = self.__disciplineRepo.getAllIDs()
#         studsIDs = self.GradedStudentIDs()
#         for studID in studsIDs:
#             for disciplineID in disciplinesIDs:
#             
#                 avg = self.getAverageForStudentAtDiscipline(studID, disciplineID)
#                 if avg<5:
#                     failing.append(studID)
#                     break
#         return failing               
                
#     def listGrades(self, studentIS):
#         """
#         Get all the grades of a student
# 
#         input:
#             The id of the student for whom the grades are listed
#         output:
#             The list of grades for the given student
#         raises:
#             StudentNotFoundException, if there is no student for the given id
#         """
#         student = self.__studentRepo.findByID(studentID)
#         if student == None:
#             raise GradeControllerException("Inexistent Student ID")
# 
#         return self.__gradeRepo.getAll(student)

    def getTop5(self, discipline):
        """
        Get the best 5 students at a given discipline

        NB!
            Here we use Data Transfer Objects (DTO)
        
        input:
            The discipline for which the best grades are returned
        output:
            The list of the highest grades
        """

        """
            Get all grades for the given discipline
        """
        studentGradeList = self.__gradeRepo.getAllForDisc(discipline)

        """
            Sort it decreasing by grade value, retain top 5 
        """
        sortedStudentGradeList = sorted(studentGradeList, key=lambda studentGrade: studentGrade.getGradeValue(), reverse=True)[:5]
        return sortedStudentGradeList

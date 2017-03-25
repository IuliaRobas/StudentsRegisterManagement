from copy import deepcopy

class Grade:
    '''
    represents the entity of a grade
    propities:
        studentID - the id of the student
        disciplineID - the id of the Discipline
        grade - the value of the grade
    '''
    
    def __init__(self,disciplineID,studentID,gradeValue):
        self.__disciplineID = disciplineID
        self.__studentID = studentID
        self.__gradeID = id(self)
        self.__gradeValue = gradeValue
#         self.__grade = []
        
        
    def __str__(self):
        '''
        This function represents the student
        '''       
    
        return 'DisciplineID: {0} StudentID: {1}  GradeValue: {2}'.format(self.__disciplineID, self.__studentID, self.__gradeValue)
    
    def __gt__(self, other):
        '''
        Function to compare two instances
        :param: other - other instance
        '''
        return self.__studentID > other.__studentID
    
    def __eq__(self, other):
        '''
        Function to compare two instances
        :param: other - other instance
        '''
        return self.__studentID == other.__studentID and self.__disciplineID == other.__disciplineID
        
#     def addGrade(self,gradeValue):
#         '''
#         function to add a grade
#         param: gradeValue - grade to be added
#         '''
#         self.__grade.append(gradeValue)

    @property
    def disciplineID(self):
        '''
        Getter for the id of the student
        :return: an integer representing the id of the student
        '''
        return self.__disciplineID
    

    @disciplineID.setter
    def disciplineID(self,newID):
        '''
        Setter for the discipline Id
        :parameter: the new Id 
        '''
        self.__disciplineID = newID
    
    @disciplineID.deleter
    def discipineID(self):
        del self.__disciplineID
        
    @property
    def studentID(self):
        '''
        Getter for the Name of the student
        :return: a string: the name of the student
        '''
        return self.__studentID 
    
    @studentID.setter
    def studentID(self,newID):
        '''
        Setter for the student Id
        :parameter: the new Id
        '''
        self.__studentID = newID
        
    @studentID.deleter
    def studentID(self):
        del self.___studentID
        
    @property
    def gradeValue(self):
        return self.__gradeValue
    
    @gradeValue.setter
    def gradeValue(self, gradeValue):
        self.__gradeValue = gradeValue
        
    @gradeValue.deleter
    def gradeValue(self):
        del self.__gradeValue
        
    @property
    def gradeID(self):
        return self.__gradeID
    
#     @property
#     def Grade(self):
#         '''
#         Getter for the grade of the student
#         :return: a float: value of the grade
#         '''
#         return self.__grade 
#     
#     @Grade.setter
#     def Grade(self,newGrade):
#         '''
#         Setter for the grade
#         :parameter: the new grade 
#         '''
#         self.__grade = deepcopy(newGrade)
#         
#     def getGradeSize(self):
#         '''
#         Getter for the size of the grade list
#         '''
#         return len(self.getGrade())
    
    
        
    


    
    
        
    
        